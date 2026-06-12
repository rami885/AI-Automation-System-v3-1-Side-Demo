# DRFONE AI OS — Core (skeleton)

المرحلة A من خطة التنفيذ (v1.1): **القلب channel-agnostic**، كود محلي فقط — **لا نشر، لا credentials، لا اتصال خارجي**.

## ما المبني حتى الآن

| الخطوة | المكوّن | الملف |
|---|---|---|
| A1 | Multi-tenancy (tenant_id من اليوم الأول، DRFONE = Tenant 0) | `src/tenant/tenant.ts` |
| A2 | Canonical Message Schema + تحقق | `src/schema/canonical.ts` |
| A3 | Policy Engine (PDP): الدور × التصنيف × القناة، افتراضي = رفض | `src/policy/policy-engine.ts`, `src/policy/classification.ts` |
| A4 (أساس) | Audit append-only + hash-chain | `src/audit/audit.ts` |
| A5 | طبقة هوية + محوّل Telegram (وضع اختبار، بلا إرسال) | `src/auth/identity-directory.ts`, `src/channels/telegram.ts` |
| A6 | المعرفة + تجربة Daily Operations Brief (قراءة فقط) | `src/knowledge/knowledge-base.ts`, `src/pilots/daily-brief.ts` |
| القلب | AI Operation Room + composition root | `src/core/operation-room.ts`, `src/app/build-app.ts` |

## التشغيل

```bash
npm install      # يثبّت @types/node فقط (لا تبعيات تشغيل)
npm test         # يبني ويشغّل 22 اختبارًا
npm run demo     # عرض توضيحي محلي للتدفّق كاملًا
npm run typecheck
```

## القرارات المعمارية المثبّتة في الكود

- **عزل المستأجرين**: أي وصول عبر مستأجر مختلف = رفض فوري (قبل أي فحص آخر).
- **الصلاحيات server-side**: القرار في `decide()` المركزي — لا في الواجهة.
- **حدود الثقة**: القناة العامة لا تتجاوز `public`؛ الداخلية لا تتجاوز `internal`؛ الخاصة (رامي) كل شيء.
- **Escalation**: طلب موظف/مالك لمورد أعلى من سقف قناته = `escalate` (موافقة رامي) لا رفض صامت.
- **العميل**: لا يتجاوز `public` على أي قناة.
- **التدقيق**: كل قرار (بما فيه الرفض والتصعيد) يُسجَّل في سلسلة هاش غير قابلة للتلاعب.

## ما هو **ليس** هنا بعد (المرحلة B — تحتاج بوابة)

- إرسال Telegram الحيّ (token + Bot API).
- ربط Supabase/Postgres كـsink فعلي للـaudit والهوية بدل النسخة في الذاكرة.
- Web UI داخلي (LibreChat) + ربط المعرفة بملفات DRFONE الحقيقية.
