# Install Brief — Agent Reach + PixelRAG (Light) — for LOCAL Claude Code

> هذا الـ brief موجَّه لـ **Claude Code المحلي على جهاز Windows** اللي عنده وصول لـ `D:\DRFONE-WORKSPACE`.
> ما ينفّذ من بيئة سحابية — يحتاج وصول للقرص المحلي والـ ZIP files.

## الهدف

تثبيت **Agent Reach (base only)** و **PixelRAG (root/light only)** من ملفات ZIP مرفوعة، بأمان، بدون لمس production.

## المدخلات (ZIP)

- ✅ `Agent-Reach-main.zip`
- ✅ `PixelRAG-main.zip`
- ❌ `woocommerce-direct-checkout.3.6.6.zip` — **لا تثبّته إطلاقًا**

## الأمر المطلوب تشغيله

```powershell
D:\DRFONE-WORKSPACE\00-INBOX\TOOLS\DRFONE_INSTALL_AGENT_REACH_PIXELRAG_LIGHT.ps1
```

> قبل التشغيل: افتح الـ script واقرأه للتأكد إنه يطابق هالقواعد. لو الـ script بيعمل أي شي خارج النطاق (يلمس WordPress/WooCommerce/production)، **أوقف** ولا تشغّله — بلّغ بالحالة `FAIL_WITH_ERROR` مع السبب.

## القواعد الصارمة (Guardrails)

- التثبيت **فقط** داخل: `D:\DRFONE-WORKSPACE\02-LOCAL-AI-TOOLS\`
- ممنوع لمس **WordPress**.
- ممنوع لمس **WooCommerce**.
- ممنوع الوصول لـ **production admin**.
- ممنوع إعداد **cookies**.
- ممنوع استخدام **حسابات شخصية**.
- **Agent Reach**: base فقط.
- **PixelRAG**: root/light فقط.
- ممنوع تثبيت إضافات PixelRAG الثقيلة: `embed`, `serve`, `index`, `all`, `train`.
- **اختبارات آمنة فقط** (safe tests) — لا اختبارات تلمس شبكة/إنتاج/بيانات حقيقية.

## خطوات التنفيذ

1. تأكد إنك على جهاز Windows وعندك وصول لـ `D:\DRFONE-WORKSPACE`.
2. تأكد من وجود الـ ZIP المسموحة فقط، وتجاهل `woocommerce-direct-checkout.3.6.6.zip`.
3. شغّل الـ script `DRFONE_INSTALL_AGENT_REACH_PIXELRAG_LIGHT.ps1` (بعد قراءته).
4. ثبّت داخل `02-LOCAL-AI-TOOLS\` فقط، base/light فقط.
5. شغّل safe tests فقط.
6. لو ظهر نقص اعتمادية (dependency مفقودة) → **لا تجبر التثبيت**، أوقف بحالة `HOLD_NEEDS_DEPENDENCY` ووثّق شو الناقص.

## التقرير

احفظ تقرير بصيغة Markdown إلى:

```
D:\DRFONE-WORKSPACE\08-REPORTS\AGENT_REACH_PIXELRAG_LIGHT_INSTALL_REPORT.md
```

يحتوي التقرير:
- ملخص ما تم تثبيته (Agent Reach base / PixelRAG light) + المسارات.
- تأكيد إنه ما انثبتت الإضافات الثقيلة ولا WooCommerce plugin.
- نتائج الـ safe tests.
- أي تحذيرات/اعتماديات ناقصة.
- **الحالة النهائية** (سطر واضح بالأعلى).

## الحالة النهائية (واحدة فقط)

- `PASS_INSTALL_SAFE` — انثبت كل شي base/light بنجاح والـ safe tests نجحت.
- `HOLD_NEEDS_DEPENDENCY` — وقف بسبب اعتمادية ناقصة، بدون أي تثبيت قسري.
- `FAIL_WITH_ERROR` — صار خطأ يمنع الإكمال (وثّق الخطأ).
