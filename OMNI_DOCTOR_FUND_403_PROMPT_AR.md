# Brief لـ Claude Code المحلي — تشخيص وإصلاح خطأ 403 "Forbidden: trusted endpoint"

> هذا الملف موجَّه لـ Claude Code اللي عنده وصول لكود الـ backend الحقيقي على `agent.drfone.eu`.
> ريبو الـ demo هذا (`AI-Automation-System-v3-1-Side-Demo`) **ما فيه** الكود اللي بيرمي الخطأ — هو صفحات عرض فقط.

## الأعراض

- تشغيل أداة/workflow اسمها **"Omni Doctor Fund"** من تطبيق **Codex**.
- Codex بيوصل لـ backend على: **`agent.drfone.eu`**.
- النتيجة: **`Forbidden: this endpoint requires a trusted...`** (الأغلب `trusted origin` أو `trusted client`) — وهي **HTTP 403** من السيرفر نفسه، مش من الواجهة.

## المطلوب (نفّذ بالترتيب — لا تعدّل أي شي قبل ما تفهم السبب)

1. **لاقي الـ endpoint المسؤول عن "Omni Doctor Fund"**
   - دوّر على route/handler يخص `fund` أو `omni` أو `doctor`.
   - حدد الملف + رقم السطر.

2. **لاقي مصدر رسالة "trusted"**
   - `grep -rin` على: `trusted`, `Forbidden`, `trusted origin`, `trusted client`.
   - حدد أي middleware/guard بيرمي الـ 403 (auth middleware؟ origin allowlist؟ CORS؟ IP filter؟).

3. **افحص شرط الرفض بالضبط**
   - شو القيمة المتوقعة (header اسمه إيش؟ token؟ origin؟ IP allowlist؟).
   - شو اللي Codex فعليًا بيبعته (قارن مع لوج الطلب لو متوفر).
   - صنّف السبب: (أ) header/token ناقص، (ب) origin مش بالـ allowlist، (ج) IP محظور، (د) CORS، (هـ) سلوك مقصود.

4. **انتبه للتصميم الأمني**
   - بمعمارية النظام في tier: `T1 read · T2 draft · T3 write+confirm · T4 destructive+double · **Forbidden = banking**`.
   - إذا "Omni Doctor Fund" عملية مالية/صندوق → الرفض **سلوك صحيح** ولازم يمرّ من مسار موافقة (`confirm_token` / PIN / approval) مش من الـ agent مباشرة. وضّح هاي النقطة قبل أي تعديل.

5. **رجّع تقرير قبل الإصلاح**
   - السبب الجذري بسطر واحد.
   - الملف + السطر.
   - هل الرفض مقصود (أمان) ولا bug/إعداد ناقص.
   - الحل المقترح + أي مخاطر أمنية فيه.

## قيود مهمة

- ما تفتح أي endpoint مالي/banking بدون موافقة صريحة.
- لا تعطّل أي auth أو trusted-origin check مشان "تمشّي" الطلب — هذا يكسر الأمان.
- لا تطبع أو تكتب أي secret/token/API key بالكود أو بالـ output.
- بعد الموافقة على الحل، طبّقه + اعمل commit برسالة واضحة.

## مرجع من معمارية النظام (للسياق)

طبقة الأمان `L7` في `D2_Stack_Architecture_Map.html`:

- **Tool Tiers (T1–T4):** `T1 read · T2 draft · T3 write+confirm · T4 destructive+double · Forbidden = banking`.
- **GDPR Gate:** أي export/delete لبيانات شخصية = PIN + سبب قانوني + log.
- **confirm_tokens:** TTL 5 دقائق + rate limiting + session cache.
