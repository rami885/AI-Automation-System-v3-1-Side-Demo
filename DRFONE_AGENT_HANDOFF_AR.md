# DRFONE Telegram AI Agent — Handoff / سياق كامل للمتابعة

## الهدف
البوت على Telegram (لرامي فقط) لازم يجيب بياناتي الخاصة لما أسأله، بدل ما يخترع
اعتذار خصوصية. تم إصلاح المشكلة الأساسية جزئياً عبر n8n، وباقي بناء الـ RAG.

## البنية (n8n على https://n8n.drfone.eu)
- **Agent رئيسي:** `DRFONE_AI_AGENT_ROOM_V3.24_STAGING`  (workflow id: `pzYcFv1ETTwKzzTw`) — active، 54 node.
- **Brain Router (sub-workflow):** `DRFONE_BRAIN_ROUTER_v1.0_RAMI_FILL` (id: `vx7EVhnIA2kOcPJN`).
  يستقبل `{prompt, system}` ويجرّب بالترتيب:
  PC GPU `https://ollama.drfone.eu` (qwen2.5:7b، يحتاج bearer) → VPS CPU `http://ollama:11434` (qwen2.5:3b)
  → Gemini free → OpenRouter → "AI offline". **لا يحقن أي بيانات — مجرّد relay للموديل.**
- **Health monitor:** `DRFONE_HEALTH_MONITOR_v1.0` (id: `vrwv4SzWCMJ9LLus`) — inactive، ينبّه عند سقوط الدماغ.
- **Tasks Data Table:** `DRFONE_AI_OPERATIONS_ROOM_TASKS` (id: `3tc3lE6EZpxCfQuH`) — 24 عمود (task_id, state,
  risk_level, safety_status, next_action, ...). مصدر منظَّم جاهز للربط.

## السبب الجذري للمشكلة
أسئلة الدردشة الحرّة (`/ai_chat`) كانت تُرسل للموديل **بدون أي سياق/بيانات**. الدماغ الرئيسي كان نازل،
فوقع على VPS CPU (qwen2.5:3b) الضعيف، فاخترع رد "خصوصية" (هلوسة). الـ agent لا يعرف إلا ما يُغذّى به.

## ما تم تعديله (في workflow pzYcFv1ETTwKzzTw — node code فقط، بدون تغيير ربط)
1. **`AI Brain Context Builder`** (code, runs before Brain Router):
   - يحقن المصادر المتاحة (مجلدات Drive 01-TO-REVIEW / 02-APPROVED-TO-MOVE / 04-AGENT-HANDOFFS + سياق أونلاين)
     مع **كل** سؤال، بما فيه `/ai_chat`.
   - system prompt صارم: أجب من السياق فقط؛ إن لم تتوفر الإجابة قل «ما عندي بيانات عن هذا في مصادري الحالية»
     واقترح `/status` أو `/review`؛ **ممنوع اختراع أعذار خصوصية/قانونية أو ادّعاء أن البيانات محمية**.
   - يضبط flag `is_status_question` ويوجّه لأسئلة حالة النظام نحو `/status`.
   - يحافظ على المخرجات: `ai_prompt`, `ai_system`, `chat_id`, `from_id`, `output`, `nl_intent`.
2. **`Status Reply`** (code v2): فحص حيّ متوازٍ عبر `this.helpers.httpRequest` عند `/status`:
   - `https://ollama.drfone.eu/api/tags` (PC GPU)
   - `http://ollama:11434/api/tags` (VPS CPU + عدد الموديلات)
   - `https://chat.drfone.eu/` (واجهة الدردشة)
   يعرض 🟢/🔴 + كود الحالة + آخر فحص. بدون أي تغيير على ربط الـ workflow.

## مؤجّل: RAG / Qdrant (المطلوب لـ "البحث الدلالي بكل وثائقي")
غير قابل للتفعيل حالياً: **لا credential لـ Qdrant، لا workflow فهرسة (ingestion)، لا collections مفهرسة.**
ربطه الآن = نتائج فارغة. المتطلبات:
1. تشغيل Qdrant (self-hosted على نفس VPS) + إضافة credential في n8n.
2. workflow فهرسة: قراءة الوثائق (Drive/ملاحظات) → embeddings (OpenAI/Gemini موجودة) → تخزين في Qdrant.
3. عقدة بحث Qdrant داخل الـ agent تحقن النتائج في `AI Brain Context Builder` قبل الموديل.
بديل جاهز فوراً: ربط `DRFONE_AI_OPERATIONS_ROOM_TASKS` كمصدر منظَّم (data table read → ضمّه للسياق).

## الموارد المتاحة (credentials في n8n)
- `DRFONE Brain Token` (httpBearerAuth, id `K037wzKEDaF11cXF`) — للـ ollama.drfone.eu
- Telegram: `DRFONE AI Operations Room Telegram` (id `2p0PISHmYwO7xm16`)
- Gemini (`wNxTNtJnYeYbrwGO`), OpenAI (`ghzI2LWKwCbDdumq`), OpenRouter، DeepSeek، Google Drive.
- **لا يوجد** Qdrant ولا Postgres credential.

## وضع الأمان (يجب احترامه)
الـ agent flag-gated، safe-by-default، Rami-only. ممنوع: كتابة إنتاجية، رسائل لزبائن، حذف/استبدال،
API خارجي بدون موافقة منفصلة. أي تعديل لازم يبقى ضمن هذا الإطار.

## التحقق
1. Telegram → `/status` → حالة حيّة للمسارات الثلاثة.
2. أعد السؤال الأصلي → إجابة من السياق أو اعتراف صريح بعدم توفر البيانات (بدل اعتذار خصوصية).

## المرجع في GitHub
- repo: `rami885/AI-Automation-System-v3-1-Side-Demo`
- branch: `claude/telegram-ai-agent-data-dkmy4h`
- ملف التوثيق: `DRFONE_AGENT_DATA_FIX_AR.md` — draft PR #3.

## المهمة التالية المقترحة لـ Claude Code المحلي
(أ) ربط `DRFONE_AI_OPERATIONS_ROOM_TASKS` كمصدر سياق منظَّم في الـ agent.
(ب) بناء pipeline فهرسة Qdrant + عقدة بحث (RAG كامل).
(ج) اختبار end-to-end عبر Telegram (لم أتمكّن منه — يحتاج رسالة فعلية من رامي).
