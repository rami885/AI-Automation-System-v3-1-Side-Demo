# DRFONE AI Business OS — دليل التنفيذ (Implementation Runbook)

**يرافق:** `DRFONE_AI_BUSINESS_OS_WORK_PLAN_V1_1.md`
**القاعدة:** ما لا يحتاج نشرًا/credentials/DNS يبدأ الآن؛ الباقي خلف بوابات.

---

## المرحلة A — بناء القلب (يبدأ الآن · بلا بوابة)

كود محلي داخل `core/`. لا اتصال خارجي، لا credentials.

| الخطوة | الوصف | الحالة |
|---|---|---|
| A1 | الهيكل + Docker + `tenant_id` (DRFONE = Tenant 0) | ✅ منجز |
| A2 | Canonical Message Schema + تحقق | ✅ منجز |
| A3 | Policy Engine (PDP): الدور × التصنيف × القناة، افتراضي رفض | ✅ منجز |
| A4 | Audit append-only + hash-chain | ✅ أساس منجز |
| A5 | محوّل Telegram (وضع اختبار، بلا إرسال حيّ) + طبقة هوية | ✅ منجز |
| A6 | أول تجربة — Daily Operations Brief (قراءة فقط) | ✅ منجز |

**نهاية A:** ✅ دماغ يعمل محليًا، tenant-aware، قابل للاختبار — 22 اختبار ناجح + عرض توضيحي (`npm run demo`). بلا لمس أي شيء حقيقي.

---

## المرحلة B — التشغيل الداخلي

**🔑 يحتاج: بوابة الإطلاق الداخلي + وصول VPS + credentials**

| الخطوة | الوصف |
|---|---|
| B1 | تجهيز Hostinger VPS → Docker compose: Supabase + backend + LibreChat خلف Cloudflare (بلا DNS عام) |
| B2 | Supabase Auth مربوط بـ EMPLOYEE_ACCESS_MATRIX + Telegram حيّ + Web UI داخلي للموظف |
| B3 | تشغيل التجارب الثلاث وقياس KPIs (وقت موفّر · adoption · جودة) |

---

## المرحلة C — المنتجة والبيع (Horizon 2)

**🔑 بوابات منفصلة**

| الخطوة | الوصف | البوابة |
|---|---|---|
| C1 | entitlements للباقات + عدّاد استخدام + تقوية عزل المستأجرين | تصميم |
| C2 | الإطلاق العام: DNS لـ ai.drfone.eu + واجهة Next.js مخصصة + PWA | `APPROVE_PUBLIC_WEB_CHANNEL_GO_LIVE` |
| C3 | تغليف plugins + onboarding آلي + أول 3 عملاء | `APPROVE_FIRST_3_CLIENTS_OUTREACH` |

---

## ملخص البوابات

| المرحلة | تحتاج إذنًا؟ |
|---|---|
| A — القلب (كود) | ❌ لا — يبدأ فورًا |
| B — تشغيل داخلي | ✅ VPS + بوابة |
| C — منتجة وبيع | ✅ بوابات منفصلة |
