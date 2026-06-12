# DRFONE AI Business Operating System — خطة العمل التنفيذية

**النسخة:** v1.1
**تاريخ التحديث:** 2026-06-12
**النسخة السابقة:** v1.0 (2026-06-10)
**حالة هذه النسخة:** `HOLD_PENDING_RAMI_REVIEW_CHANNELS_ACCESS_V1_1`
**نطاق التحديث:** إضافة طبقة **Channels & Access Governance** — تصميم وحوكمة فقط. لا تفعيل قناة عامة، لا نشر ai.drfone.eu، لا ربط بيانات حساسة، لا تغيير production.

---

## 0. سجل التغييرات من v1.0 إلى v1.1

| # | التغيير | القسم |
|---|---|---|
| 1 | إضافة طبقة سابعة: **Channels & Access Governance Layer** | 4.7 (جديد) |
| 2 | تحديث المخطط المعماري: Channels → Channel Adapter → Auth + Policy Engine → Core | 3 |
| 3 | اعتماد مبدأ **Channel-Agnostic Core** رسميًا | 2، 3 |
| 4 | تحويل التفويض من RBAC فقط إلى **RBAC × Data Classification × Channel** (ABAC) | 4.5، 4.7 |
| 5 | توسيع Audit ليكون append-only ويسجّل القناة + حالات الرفض + سبب القرار | 4.5، 4.7 |
| 6 | إضافة بوابة جديدة + فصل بوابة الخطة عن بوابة الإطلاق العام | 8 |
| 7 | حسم القرارات الثلاثة + تثبيت الحزمة المرجعية (VPS أونلاين مملوك) | 13 (محسوم) |
| 8 | تأكيد أن Telegram أيضًا يخضع لنفس Auth + Policy (لا باب مميّز) | 4.7 |
| 9 | إضافة طبقة **Scale & SaaS Readiness**: multi-tenancy، entitlements، metering، سلّم توسع | 14 (جديد) |

> كل ما لم يُذكر هنا يبقى كما في v1.0 دون تغيير (الطبقات 4.1–4.6، خطة الأشهر الستة، التسويق، التسعير).

---

## 1. الحكم التنفيذي (محدّث)

الخطة هي بناء **AI Business Operating System** يخدم DRFONE داخليًا أولًا ثم يتحول إلى حلول قابلة للبيع.

التحديث الجوهري في v1.1: النظام يُبنى على مبدأ **دماغ واحد، عدة واجهات (Channel-Agnostic Core)**. القلب — AI Operation Room + Claude Code + الحوكمة — يُبنى **مرة واحدة**، وتتصل به كل القنوات (Telegram، Web UI، PWA، وأي قناة مستقبلية) كواجهات رفيعة. الصلاحيات والحوكمة تُفرض في القلب (server-side)، لا في الواجهة.

> القرار المعتمد: `APPROVE_CHANNEL_AGNOSTIC_CORE_AND_CHANNELS_ACCESS_V1_1` — اعتماد التصميم والحوكمة فقط. الإطلاق العام يحتاج بوابة منفصلة.

---

## 2. المبادئ المعمارية المعتمدة (محدّث)

| المبدأ | القرار |
|---|---|
| مصدر الحقيقة | DRFONE-WORKSPACE / AI_AGENT_ROOM_OPERATIONS |
| **بنية القنوات** | **Channel-Agnostic Core — دماغ واحد، عدة واجهات** |
| **موضع الصلاحيات** | **server-side في Policy Engine — وليس UI-only** |
| قناة رامي الأساسية (Horizon 1) | Telegram |
| المنسّق التقني | Claude Code |
| لوحة المتابعة | Kanboard Cloud كـ visual mirror |
| التنفيذ | عبر AI Operation Room + gates فقط |
| البيانات الحساسة | local/private أو pointer-only في السحابة |
| **التفويض** | **RBAC × Data Classification × Channel (ABAC)** |
| العملاء | لا تواصل/إرسال بدون موافقة رامي |
| البيع الخارجي | بعد إثبات داخلي ووجود governance |

---

## 3. الهيكل العام للنظام (محدّث)

```text
القنوات (thin clients):
   Telegram   |   Web UI @ ai.drfone.eu   |   PWA (موبايل)   |   قنوات مستقبلية
        │                  │                      │
        └──────────────────┼──────────────────────┘
                           ▼
                   Channel Adapter
        (تطبيع كل طلب إلى Canonical Message Schema)
                           ▼
                Auth + Policy Engine (PDP)
   (هوية، جلسة، RBAC × Data Classification × Channel)
                           ▼
              AI Operation Room — Core
            (gates, routing, safety, audit)
                           ▼
              Claude Code Orchestration Lead
                           ▼
        Local AI Brain / Knowledge Base / Agent Memory
                           ▼
        n8n / Micro-Tools / Reports / Kanboard
                           ▼
        Business Outputs / Productized Client Solutions
```

**مبدأ حاكم:** القنوات «غبية»؛ القلب + الحوكمة موجودان مرة واحدة. إضافة قناة جديدة لا تلمس الحوكمة. **Telegram ليس استثناءً** — يمرّ بنفس Auth + Policy (هوية رامي = role=owner مُصادَقة).

---

## 4.7 Channels & Access Governance Layer — طبقة القنوات والوصول (جديد)

**الهدف:** السماح بعدة واجهات (Telegram / Web / PWA) دون تكرار الحوكمة أو فتح ثغرات، مع فرض الصلاحيات server-side.

### 4.7.1 المكوّنات

| المكوّن | الدور |
|---|---|
| Channel Adapters | استقبال من كل قناة وتطبيعه إلى Canonical Message Schema |
| Auth Provider | مصادقة الهوية وإدارة الجلسات (انظر سجل القرارات §13) |
| Policy Engine (PDP) | نقطة قرار تفويض **واحدة مركزية** تُستدعى من كل المحوّلات |
| Trust Boundary Map | تعريف ما تراه كل قناة حسب تصنيف البيانات |
| Channel Audit | سجل append-only لكل طلب/قرار عبر كل القنوات |
| Escalation Gate | تصعيد طلبات البيانات الحساسة من القنوات العامة إلى موافقة رامي |

### 4.7.2 Canonical Message Schema (تطبيع موحّد)

كل قناة تحوّل طلبها قبل دخول القلب إلى:

```json
{
  "request_id": "uuid",
  "identity": { "user_id": "string", "role": "owner|employee|client" },
  "channel": { "type": "telegram|web|pwa", "exposure": "private|internal|public" },
  "intent": "read|review|write|code|report|execute",
  "payload": { "text": "string", "attachments": [] },
  "timestamp": "iso8601"
}
```

### 4.7.3 نموذج التفويض: RBAC × Data Classification × Channel

القاعدة «القناة العامة لا ترى الحساس» قائمة على **الخاصية** لا الدور وحده. القرار = دالة في ثلاثة أبعاد:

| البُعد | القيم |
|---|---|
| الدور (RBAC) | owner / employee / client |
| تصنيف المورد | public / internal / confidential / rami_private / finance_private |
| انكشاف القناة | private (Telegram رامي) / internal (Web موظفين) / public (ai.drfone.eu) |

**مصفوفة مبسّطة (الافتراضي = رفض):**

| المورد \ القناة | Telegram (رامي) | Web داخلي (موظف) | Web عام (عميل) |
|---|---|---|---|
| public | ✅ | ✅ | ✅ |
| internal | ✅ | ✅ (حسب الدور) | ❌ |
| confidential | ✅ | ❌ | ❌ |
| finance_private / rami_private | ✅ | ❌ | ❌ |

> أي طلب لمورد أعلى من انكشاف القناة → **يُرفض أو يُصعّد عبر Escalation Gate** (§4.7.5).

### 4.7.4 Trust Boundary Map (حدود الثقة)

```text
Public Web Channel (ai.drfone.eu)  →  pointer-only / non-sensitive فقط
Internal Employee Channel          →  internal حسب EMPLOYEE_ACCESS_MATRIX
Rami Private Channel (Telegram)    →  كل شيء، مع تدقيق كامل
Local AI Operation Room            →  العمليات الحساسة محليًا
Sensitive Data Stores              →  لا تُلمس من القنوات العامة إطلاقًا
```

### 4.7.5 Escalation Gate

عند طلب مورد حساس من قناة عامة/داخلية لا تملك صلاحيته:
1. يُمنع الإرجاع المباشر.
2. يُنشأ طلب موافقة يُوجّه إلى **Telegram رامي**.
3. لا يُسلّم شيء قبل موافقة صريحة، وتُسجّل الموافقة في Audit.

### 4.7.6 Audit Schema (موسّع، append-only)

```json
{
  "audit_id": "uuid",
  "user_id": "string",
  "role": "string",
  "channel": "telegram|web|pwa",
  "action": "string",
  "resource": "string",
  "data_classification": "public|internal|confidential|private",
  "decision": "allow|deny|escalated",
  "decision_reason": "string",
  "timestamp": "iso8601",
  "prev_hash": "string",
  "hash": "string"
}
```

- **append-only / hash-chain** (غير قابل للتلاعب) — شرط لحوكمة قابلة للبيع.
- تُسجّل **حالات الرفض** لا القبول فقط (الرفض إشارة أمنية).

### 4.7.7 سياسة تخزين الجهاز (Device Cache Policy) — للـ PWA

- منع تخزين أي رد مصنّف internal فأعلى على الجهاز (no offline cache للحساس).
- تشفير أي تخزين محلي مسموح + انتهاء جلسة تلقائي.
- إبطال الجلسة عن بُعد عند فقد الجهاز.

### 4.7.8 ملاحظات تقنية معتمدة

- **PWA أولًا:** كود ويب واحد متجاوب → PWA مثبّتة على الشاشة. Native (Capacitor/React Native) يؤجَّل إلى Horizon 2 عند طلب تجاري واضح. تنبيه: push على iOS يتطلب 16.4+ والتثبيت على الشاشة.
- **الموبايل مغطّى الآن مجانًا عبر Telegram** لرامي في Horizon 1؛ إلحاح PWA حقيقته Horizon 2 (المنتجة).
- **واجهة جاهزة أولًا:** تقييم LibreChat / Open WebUI / Vercel AI Chatbot. الشرط: تتحدث **فقط** مع backend الخاص بنا (لا نداء نموذج مباشر)، وتُعطّل أي ميزة تتجاوز الحوكمة أو تخزّن الرسائل خارج تدقيقنا. توقّع استبدالها بواجهة مخصصة في Horizon 2.

### 4.7.9 المخرجات المطلوبة

```text
CHANNELS_ACCESS_ARCHITECTURE_V1_1.md
CANONICAL_MESSAGE_SCHEMA.json
POLICY_ENGINE_RULES.md
TRUST_BOUNDARY_MAP.md
CHANNEL_AUDIT_SCHEMA.json
DEVICE_CACHE_POLICY.md
AUTH_PROVIDER_DECISION.md  (مفتوح — §13)
```

---

## 4.5 Governance / Security Layer — إضافات v1.1

تُضاف إلى قواعد v1.0:

- التفويض server-side عبر **Policy Engine (PDP) واحد** — لا فحوص أدوار متناثرة، لا UI-only.
- **كل القنوات** (بما فيها Telegram) تخضع للمصادقة والتفويض — لا باب مميّز.
- Audit **append-only** يسجّل القناة + التصنيف + سبب القرار + حالات الرفض.
- متطلبات إلزامية قبل أي نشر عام: Auth provider حقيقي، ربط الهوية بـ EMPLOYEE_ACCESS_MATRIX، Rate limiting، TLS، WAF/reverse proxy، authorization middleware، منع البيانات الحساسة من القنوات العامة إلا عبر Escalation Gate.

---

## 8. Gates المعتمدة (محدّث)

```text
APPROVE_AI_BUSINESS_SYSTEM_PRODUCTIZATION_PLAN_BUILD
APPROVE_INTERNAL_PILOT_USE_CASES_SELECTION
APPROVE_DRFONE_INTERNAL_PILOT_START
APPROVE_CHAMPION_PILOT_WITH_EMPLOYEES
APPROVE_PRODUCT_PACKAGING_BUILD
APPROVE_FIRST_3_CLIENTS_OUTREACH
APPROVE_CHANNEL_AGNOSTIC_CORE_AND_CHANNELS_ACCESS_V1_1   ← جديد (اعتماد التصميم/الحوكمة)
APPROVE_PUBLIC_WEB_CHANNEL_GO_LIVE                       ← جديد (منفصل: الإطلاق العام)
```

### ممنوع قبل البوابات (محدّث)

```text
No production changes
No customer contact
No live external API
No credentials
No automatic sending
No employee access expansion
No cloud sensitive data
No n8n publish/activation
No public DNS for ai.drfone.eu        ← جديد (حتى APPROVE_PUBLIC_WEB_CHANNEL_GO_LIVE)
No managed-auth PII egress            ← معتمد: Auth = Supabase self-hosted على VPS (لا خروج PII)
```

> **فصل البوابتين:** اعتماد الخطة (`..._V1_1`) لا يعني الإطلاق العام. ai.drfone.eu لا يُنشر ولا يُربط DNS قبل `APPROVE_PUBLIC_WEB_CHANNEL_GO_LIVE`.

---

## 13. سجل القرارات — محسوم (v1.1)

تم حسم القرارات الثلاثة المفتوحة بتفويض من رامي، بمعيار: **online ومتاح من أي مكان + سيادة البيانات**. الحل: **VPS واحد أونلاين تملكه** يجمع الوصول من أي مكان مع بقاء البيانات تحت سيطرتك.

| القرار | الاختيار المعتمد | السبب |
|---|---|---|
| مكان الـ backend | **Hostinger VPS** (أونلاين) | وصول من أي مكان + ملكية كاملة للبيانات؛ سحابة مُدارة تكسر الميزة البيعية الأساسية (الخصوصية) |
| Auth + DB | **Supabase self-hosted على نفس الـVPS** | Auth + Postgres + Storage + RLS في حزمة واحدة أونلاين مملوكة؛ يخدم أيضًا الـaudit والمعرفة؛ قطع متحركة أقل من Keycloak |
| واجهة الـchat (Horizon 1) | **LibreChat** self-hosted | جاهزة، أونلاين، متعددة المستخدمين، custom endpoints، بعلامتك — أسرع إطلاق داخلي |
| واجهة الـchat (Horizon 2) | **Next.js مخصص (نمط Vercel AI Chatbot)** | تحكم كامل بالحوكمة والعلامة + مسار PWA نظيف للمنتجة |
| TLS / WAF / Proxy | **Cloudflare أمام Caddy/Nginx** | TLS + حماية + وصول أونلاين عالمي |

### 13.1 الحزمة المرجعية (Reference Stack) — Stage 1 (Pilot)

> هذه **المرحلة الأولى** من سلّم التوسع (§14.5). تُبنى الخدمات **stateless + Docker + tenant-aware** من الآن حتى تتوسّع لاحقًا دون إعادة كتابة.

```text
                Cloudflare (DNS + TLS + WAF)
                          │
              Caddy / Nginx reverse proxy
                          │
   ┌──────────────────────┼──────────────────────┐
   │                      │                       │
 LibreChat            Backend API            Supabase (self-hosted)
 (Web/PWA UI)     (Channel Adapter +         Auth + Postgres +
 ai.drfone.eu     Policy Engine + Core)      Storage + RLS + Audit
                          │
                  Claude Code Orchestration
                          │
          Local AI Brain / Knowledge / Agent Memory
                  ── كل ما سبق على Hostinger VPS ──
```

> **بديل احتياطي للسرعة فقط:** إن لزم إطلاق pilot سريع قبل تجهيز self-host، يجوز استخدام Supabase Cloud (منطقة EU) **لبيانات غير حساسة فقط**، مع الهجرة إلى self-host قبل ربط أي بيانات حساسة. الافتراضي يبقى self-host.

### 13.2 ملاحظة على الحدود (مهمة)

هذه القرارات **تصميمية ومعتمدة في الخطة**، لكن التنفيذ الفعلي (تجهيز الـVPS، نشر Supabase/LibreChat، ربط DNS، شهادات، credentials) لا يبدأ قبل بوابة `APPROVE_PUBLIC_WEB_CHANNEL_GO_LIVE`. القرار محسوم؛ التنفيذ ينتظر البوابة.

---

## 14. Scale & SaaS Readiness — جاهزية التوسع والـSaaS (جديد)

**المبدأ:** النظام سينتهي كـ **SaaS باستخدامات كبيرة + بيع packages**. لذا نبني بسيطًا الآن لكن بـ«مفاصل» تمنع إعادة الكتابة (Evolutionary Architecture). **ابنِ الرخيص-الآن الذي يحفظ الغالي-لاحقًا.**

### 14.1 Multi-Tenancy — القرار الأهم (يُبنى من اليوم الأول)

- **`tenant_id` في كل جدول وكل طلب وكل سجل audit** — منذ أول سطر كود.
- DRFONE نفسها = **Tenant 0** (أول مستأجر، لا حالة خاصة).
- العزل عبر **Postgres RLS** (row-level security per tenant) في المرحلة المشتركة.
- نموذج هجين حسب الباقة:
  - **Starter / Business** → shared instance + عزل بالـRLS.
  - **Enterprise / Private** → dedicated instance أو local mode (يطابق باقة Enterprise في v1.0).
- تحويل single-tenant → multi-tenant لاحقًا = إعادة كتابة خطيرة، لذا نتجنبه بالبناء الصحيح الآن.

### 14.2 Entitlements & Package Mapping

- الباقات (Starter/Business/Enterprise) = **مجموعات صلاحيات/إضافات (feature flags + plugin sets) لكل tenant**.
- طبقة entitlements مركزية تقرأها كل القنوات والقلب (لا فحص باقة متناثر).
- ربط مباشر مع §4.7 (Policy Engine يقرأ tenant + tier + role + classification).

### 14.3 Metering & Billing

- **عدّاد استخدام per-tenant** من اليوم الأول (رسائل، مهام، tokens) — حتى لو لم نُفعّل الفوترة بعد.
- حدود/حصص (quotas) per tier لمنع تجاوز التكلفة.
- تكامل فوترة لاحق (مثل Stripe) — يُجهّز كـseam، يُفعّل في Horizon 2.

### 14.4 Statelessness & Containerization (مسار التوسع)

- الـbackend **stateless + 12-factor + Docker** من الآن → يسمح بالانتقال من VPS واحد إلى عدة نسخ/تنسيق حاويات دون إعادة كتابة.
- الحالة كلها في Postgres / Storage / Cache، لا في ذاكرة العملية.
- مهام الوكلاء الطويلة عبر **queue (async jobs)** — يُجهّز كـseam مبكرًا.

### 14.5 سلّم التوسع (Scaling Ladder)

| المرحلة | البنية | متى |
|---|---|---|
| Stage 1 — Pilot | VPS واحد (الحزمة المرجعية §13) | Horizon 1 — DRFONE داخليًا |
| Stage 2 — أول عملاء | فصل الخدمات + managed/clustered Postgres + object storage + cache + queue | Horizon 2 — أول 3 عملاء |
| Stage 3 — SaaS بمقياس | تنسيق حاويات + auto-scaling + per-region + multi-region residency | عند الطلب الحقيقي |

> لا نبني Stage 2/3 الآن — لكن لا نتّخذ أي قرار في Stage 1 يمنعهما.

### 14.6 Observability & Admin (احترافي + قابل للبيع)

- **Per-tenant usage analytics + admin console** (يطابق توصية دليل Anthropic: admin marketplace, role-based access, spend controls, usage analytics).
- **OpenTelemetry** للمراقبة والتدقيق القابل للتنظيم — جاهزية تنظيمية للبيع.
- لوحة admin للتحكم بالإضافات المتاحة per-tenant (plugin governance).

### 14.7 ملخص «صمّم الآن مقابل ابنِ لاحقًا»

| صمّم/ابنِ الآن (رخيص، يمنع إعادة الكتابة) | أجّل (غالٍ، يُبنى عند الطلب) |
|---|---|
| `tenant_id` + RLS في كل شيء | dedicated instances per enterprise |
| stateless + Docker | تنسيق حاويات / auto-scaling |
| طبقة entitlements + عدّاد استخدام | تكامل فوترة كامل / multi-region |
| seams للـqueue والـcache | clustering فعلي للـPostgres |
| Policy Engine يقرأ tenant+tier | admin console كامل الميزات |

---

## الحالة النهائية لهذه النسخة

```text
STATUS: HOLD_PENDING_RAMI_REVIEW_CHANNELS_ACCESS_V1_1
SCOPE:  تصميم + حوكمة + PR للمراجعة فقط
لا تفعيل قناة عامة. لا نشر ai.drfone.eu. لا ربط بيانات حساسة. لا تغيير production.
```
