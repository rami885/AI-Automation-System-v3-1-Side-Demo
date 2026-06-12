# DRFONE AI OS — Core (skeleton)

المرحلة A من خطة التنفيذ (v1.1): **القلب channel-agnostic**، كود محلي فقط — **لا نشر، لا credentials، لا اتصال خارجي**.

## ما المبني حتى الآن

| الخطوة | المكوّن | الملف |
|---|---|---|
| A1 | Multi-tenancy (tenant_id من اليوم الأول، DRFONE = Tenant 0) | `src/tenant/tenant.ts` |
| A2 | Canonical Message Schema + تحقق | `src/schema/canonical.ts` |
| A3 | Policy Engine (PDP): الدور × التصنيف × القناة، افتراضي = رفض | `src/policy/policy-engine.ts`, `src/policy/classification.ts` |
| A4 (أساس) | Audit append-only + hash-chain | `src/audit/audit.ts` |
| القلب | AI Operation Room: validate → decide → audit | `src/core/operation-room.ts` |

## التشغيل

```bash
npm install      # يثبّت @types/node فقط (لا تبعيات تشغيل)
npm test         # يبني ويشغّل 16 اختبارًا
npm run typecheck
```

## القرارات المعمارية المثبّتة في الكود

- **عزل المستأجرين**: أي وصول عبر مستأجر مختلف = رفض فوري (قبل أي فحص آخر).
- **الصلاحيات server-side**: القرار في `decide()` المركزي — لا في الواجهة.
- **حدود الثقة**: القناة العامة لا تتجاوز `public`؛ الداخلية لا تتجاوز `internal`؛ الخاصة (رامي) كل شيء.
- **Escalation**: طلب موظف/مالك لمورد أعلى من سقف قناته = `escalate` (موافقة رامي) لا رفض صامت.
- **العميل**: لا يتجاوز `public` على أي قناة.
- **التدقيق**: كل قرار (بما فيه الرفض والتصعيد) يُسجَّل في سلسلة هاش غير قابلة للتلاعب.

## ما هو **ليس** هنا بعد (خطوات لاحقة)

- A5: محوّل Telegram (وضع اختبار، بلا إرسال حيّ).
- A6: أول تجربة — Daily Operations Brief فوق المعرفة المحلية.
- ربط Supabase/Postgres كـsink فعلي للـaudit والهوية (المرحلة B — تحتاج بوابة).
