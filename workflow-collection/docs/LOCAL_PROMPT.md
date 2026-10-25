# البرومبت الجاهز لجهازك (Claude Code / Cowork)

انسخ النص بين الخطوط كما هو. الأجزاء بين `[...]` عدّلها إذا لزم.

---

```text
أنت تعمل في مستودع AI-Automation-System-v3-1-Side-Demo على الفرع
claude/workflow-collection-online-sale-9pgbb9. داخل المجلد workflow-collection/ يوجد
pipeline جاهز (scripts/collect.py) وكتالوج مبني (catalog/) ومجموعة قابلة للبيع
(collection/sellable/، 3,304 ورك فلو n8n في 16 كاتيجوري). اقرأ أولاً:
workflow-collection/README.md ثم docs/LICENSING.md ثم docs/REVIEW_CHECKLIST.md.

الهدف: تحويل هذه المجموعة إلى منتج رقمي جاهز للبيع (Gumroad / Lemon Squeezy).
نفّذ المراحل بالترتيب، وبعد كل مرحلة اعرض لي ملخصاً قصيراً بالأرقام، ولا تسألني
أسئلة يمكنك الإجابة عنها من الملفات.

المرحلة 1 — إعادة البناء والتوسعة
1. شغّل: cd workflow-collection && python3 scripts/collect.py --fetch
2. ابحث في GitHub topics (n8n-workflows, n8n-templates, n8n-automation) عن مستودعات
   إضافية فيها ≥ 50 ملف JSON. لكل مستودع: اقرأ LICENSE. أضف فقط MIT / Apache-2.0 /
   BSD / CC-BY / CC0 / Unlicense إلى scripts/sources.json مع license_ok=true.
   المستودعات بدون LICENSE تُضاف مع license_ok=false (للمراجعة فقط).
   تجاهل forks لمستودعات Zie619 و oxbshw.
3. أعد التشغيل واعرض لي الفرق في catalog/stats.json (قبل/بعد).

المرحلة 2 — ورك فلوزي الأصلية (الطبقة Premium الحقيقية)
1. صدّر ورك فلوز n8n الخاص بي إلى مجلد خارج المستودع:
   [n8n export:workflow --all --separate --output=~/n8n-export/]  أو عبر REST API.
2. لكل ورك فلو: احذف كل ما يخص DRFONE / Wolt / Kanboard / أرقام هواتف / إيميلات /
   أسماء أشخاص / روابط داخلية / معرفات Google Sheets. استبدلها بقيم عامة
   ({{ $env.SHOP_URL }}، "Your Telegram chat id"، إلخ). غيّر الأسماء إلى أسماء
   عامة تصف النتيجة. أضف Sticky Note "Setup" في أول كل ورك فلو.
3. ضع النتيجة في ~/n8n-export-clean/ ثم شغّل:
   python3 scripts/collect.py --extra ~/n8n-export-clean/
   تأكد أنها ظهرت بـ license=OWN و tier=premium.
4. لا تنشر أي ملف منها قبل أن أراجع قائمة الأسماء التي ستعرضها لي.

المرحلة 3 — الأسماء والوصف
1. افتح catalog/rename_queue.csv (≈1,800 ورك فلو بأسماء مولّدة آلياً).
2. لكل صف: اقرأ node_types و integrations و description_hint وافتح الملف إذا لزم،
   واكتب اسماً تسويقياً من 4-9 كلمات يصف النتيجة (مثال: "Summarize New Gmail Threads
   into Notion Every Morning")، ووصفاً من جملتين، و3 كلمات مفتاحية.
   اكتب النتائج في catalog/renames.csv (id, new_name, description, keywords)
   ثم طبّقها على ملفات JSON (حقل name) وعلى catalog.json/csv.
   اعمل على دفعات 100 واحفظ بعد كل دفعة.

المرحلة 4 — المراجعة الفنية
1. شغّل n8n محلياً: docker run -it --rm -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n
2. استورد عشوائياً 5% من كل كاتيجوري + كل الـ premium عبر CLI أو API
   وسجّل أي "unknown node" أو خطأ استيراد في catalog/import_errors.csv.
3. أي ملف يفشل: حاول إصلاحه (ترقية Function→Code، Cron→Schedule Trigger)، وإلا
   انقله إلى review-only.
4. راجع كل Sticky Notes في الـ premium واحذف أي أسماء أشخاص/شركات/روابط خاصة.

المرحلة 5 — التغليف
1. لكل كاتيجوري: README.md (ماذا يوجد، المتطلبات، كيفية الاستيراد، قائمة الملفات).
2. أنشئ THIRD_PARTY_LICENSES.txt (نص MIT + حقوق Zie619 و oxbshw، وإشعار CC BY 4.0
   لـ enescingoz) و LICENSE-BUNDLE.txt (استخدام شخصي وتجاري، ممنوع إعادة البيع)
   و PROVENANCE.csv من catalog.csv.
3. أنشئ في dist/: 
   - sampler.zip (30 ورك فلو، 2 من كل كاتيجوري، الأعلى تقييماً)
   - pack-<category>.zip لكل كاتيجوري
   - complete-library.zip (كل sellable + catalog + docs)
   - pro-bundle.zip (complete + ورك فلوزي الأصلية + أدلة الإعداد)
   تأكد أن كل zip يُفتح على Windows (لا مسارات > 200 حرف).
4. أنشئ catalog/index.html نسخة standalone (البيانات مضمّنة داخل الصفحة) لرفعها
   كمعاينة على صفحة المنتج.

المرحلة 6 — صفحات البيع
1. اكتب نصوص صفحة المنتج لـ Gumroad و Lemon Squeezy (عنوان، وصف، bullets،
   FAQ، الترخيص) بالإنجليزية ونسخة عربية، باستخدام الأرقام من catalog/stats.json.
2. اكتب 3 نصوص إعلانات قصيرة لـ LinkedIn/X و سكربت فيديو 60 ثانية.
3. حضّر 3 صور للمنتج (شبكة الكاتيجوريز بالأعداد، سكرين شوت الكتالوج، مثال AI agent)
   [استخدم Canva MCP إن كان متاحاً، وإلا HTML→PNG عبر Playwright].

قواعد صارمة:
- لا تنشر ولا تضمّن أي ملف من collection/rights-needed/ أو من n8n.io templates.
- لا تحذف provenance من أي ملف.
- لا تدفع (commit) ملفات أكبر من 5MB ولا مجلد dist/ إلى git.
- أي ملف فيه مفتاح أو كلمة سر حقيقية: احذف القيمة ولا تكتفِ بإخفائها.
- في نهاية كل مرحلة: git add + commit برسالة واضحة على نفس الفرع.
```

---

## نصائح تشغيل
- المرحلة 3 هي الأطول (≈1,800 اسم). دعها تعمل على دفعات واحفظ بعد كل دفعة.
- إذا أردت تشديد الجودة قبل البيع: `python3 scripts/collect.py --min-score 60` يقلل العدد ويرفع المتوسط.
- احتفظ بنسخة من `catalog/catalog.csv` قبل كل إعادة بناء للمقارنة.
