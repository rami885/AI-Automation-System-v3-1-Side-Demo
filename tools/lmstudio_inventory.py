#!/usr/bin/env python3
"""
LM Studio / Local LLM inventory — يفحص جهازك ويطبع تقريرًا:
  • أي مُشغّل منزّل (LM Studio / Ollama)
  • أين مجلد النماذج وما هيكله
  • أسماء النماذج المنزّلة (هل فيها Hermes أو غيره) + أحجامها
  • هل السيرفر المحلي شغّال الآن وما النماذج المحمّلة

تشغيل:  python lmstudio_inventory.py
يعمل على Windows / macOS / Linux — مكتبات بايثون القياسية فقط، بلا تثبيت أي شيء.
لا يرسل أي بيانات لأي مكان — قراءة محلية فقط.
"""

import json
import os
import platform
import sys
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError

HOME = Path.home()


def human(size: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} PB"


def hr(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def section_system() -> None:
    hr("١) معلومات النظام")
    print(f"النظام   : {platform.system()} {platform.release()}")
    print(f"المعالج  : {platform.machine()}")
    print(f"المستخدم : {HOME}")


def find_model_dirs() -> list[Path]:
    candidates = [
        HOME / ".lmstudio" / "models",
        HOME / ".cache" / "lm-studio" / "models",
        HOME / ".cache" / "lmstudio" / "models",
        HOME / "AppData" / "Local" / "lm-studio" / "models",  # Windows older
        HOME / ".ollama" / "models",  # Ollama
    ]
    return [p for p in candidates if p.exists()]


def scan_lmstudio_models() -> None:
    hr("٢) النماذج المنزّلة على القرص (الهيكل)")
    dirs = [p for p in find_model_dirs() if "ollama" not in str(p)]
    if not dirs:
        print("لم يُعثر على مجلد نماذج LM Studio في الأماكن المعتادة.")
        print("افتح LM Studio → أيقونة المجلّد (My Models) → فوق يظهر مسار المجلد، أرسله لي.")
        return

    found_any = False
    hermes_hits = []
    for base in dirs:
        print(f"\n📁 مجلد النماذج: {base}")
        gguf = sorted(base.rglob("*.gguf"))
        if not gguf:
            print("   (لا توجد ملفات .gguf هنا)")
            continue
        for f in gguf:
            found_any = True
            rel = f.relative_to(base)
            try:
                size = f.stat().st_size
            except OSError:
                size = 0
            print(f"   • {rel}  [{human(size)}]")
            if "hermes" in f.name.lower():
                hermes_hits.append(str(rel))

    if found_any:
        if hermes_hits:
            print("\n✅ تم العثور على نموذج Hermes:")
            for h in hermes_hits:
                print(f"   → {h}")
        else:
            print("\nℹ️ لم يظهر اسم 'Hermes' في أسماء الملفات — النموذج المنزّل شيء آخر (انظر القائمة أعلاه).")


def scan_ollama() -> None:
    hr("٣) Ollama (إن وُجد)")
    od = HOME / ".ollama" / "models"
    if not od.exists():
        print("لا يوجد Ollama منصّب (أو لا نماذج).")
        return
    manifests = od / "manifests"
    print(f"📁 {od}")
    if manifests.exists():
        for p in sorted(manifests.rglob("*")):
            if p.is_file():
                print(f"   • {p.relative_to(manifests)}")


def query_api(name: str, url: str) -> None:
    try:
        with urlopen(url, timeout=2) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except (URLError, TimeoutError, ConnectionError, json.JSONDecodeError, OSError):
        print(f"   {name}: السيرفر غير شغّال على {url}")
        return
    ids = []
    if isinstance(data, dict):
        if "data" in data:  # OpenAI-style
            ids = [m.get("id", "?") for m in data["data"]]
        elif "models" in data:  # Ollama-style
            ids = [m.get("name", "?") for m in data["models"]]
    print(f"   ✅ {name}: شغّال — النماذج المتاحة:")
    for i in ids or ["(لا شيء)"]:
        print(f"        - {i}")


def section_servers() -> None:
    hr("٤) السيرفرات المحلية الشغّالة الآن")
    query_api("LM Studio (OpenAI API)", "http://localhost:1234/v1/models")
    query_api("LM Studio (native)", "http://localhost:1234/api/v0/models")
    query_api("Ollama", "http://localhost:11434/api/tags")


def main() -> None:
    print("تقرير فحص النماذج المحلية — DRFONE")
    section_system()
    scan_lmstudio_models()
    scan_ollama()
    section_servers()
    hr("تم")
    print("انسخ كل ما ظهر أعلاه وأرسله لي حتى أحدّد بالضبط ماذا لديك وكيف نربطه.")


if __name__ == "__main__":
    sys.exit(main())
