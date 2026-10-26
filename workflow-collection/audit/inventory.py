#!/usr/bin/env python3
"""Read-only inventory of every JSON file belonging to the n8n workflow collection in this environment."""
import csv, hashlib, json, os, re, sys
from collections import Counter, defaultdict
from pathlib import Path

PROJECT = Path("/home/user/AI-Automation-System-v3-1-Side-Demo")
WC = PROJECT / "workflow-collection"
SP = Path("/tmp/claude-0/-home-user-AI-Automation-System-v3-1-Side-Demo/7255c058-9a75-5e0e-86fb-a8a4a68fbd6b/scratchpad/src")
SRC_META = {s["id"]: s for s in json.load(open(WC / "scripts/sources.json"))["sources"]}
LINK = {"zie619": "n8n-workflows", "oxbshw": "ultimate-n8n-ai-workflows", "enescingoz": "awesome-n8n-templates",
        "wassupjay": "n8n-free-templates", "lucaswalter": "n8n-ai-workflows"}

ROOTS = []  # (label, role, path, source_id or None)
for sid, folder in LINK.items():
    ROOTS.append((f"raw-source:{sid}", "raw clone (additional source)", SP / folder, sid))
for bucket, role in [("sellable", "PRIMARY organized collection (license-cleared)"),
                     ("review-only", "derived: license OK, below quality gate"),
                     ("variants", "derived: same-name structural duplicates"),
                     ("skeletons", "derived: synthetic skeletons"),
                     ("rights-needed", "derived: unlicensed, NOT redistributable")]:
    ROOTS.append((f"collection:{bucket}", role, WC / "collection" / bucket, None))
ROOTS.append(("catalog", "index / metadata (not workflows)", WC / "catalog", None))
ROOTS.append(("scripts", "configuration", WC / "scripts", None))

CONFIG_NAMES = {"package.json", "package-lock.json", "tsconfig.json", "manifest.json", "composer.json", "sources.json",
                "def_categories.json", "search_categories.json", "unique_categories.json", "stats.json", "renovate.json",
                ".eslintrc.json", "pyrightconfig.json", "settings.json", "launch.json"}

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def classify(p: Path, d, err):
    name = p.name
    if err:
        return "invalid-json"
    if isinstance(d, dict) and isinstance(d.get("nodes"), list) and d["nodes"] and all(isinstance(n, dict) and "type" in n for n in d["nodes"]):
        return "workflow"
    if name in CONFIG_NAMES or "/schemas/" in str(p) or "/.vscode/" in str(p) or "/.github/" in str(p):
        return "config"
    if re.search(r"(index|catalog|categor|manifest|registry|list)", name, re.I) or "/catalog/" in str(p) or "/context/" in str(p):
        return "index"
    if isinstance(d, dict) and "nodes" in d:
        return "workflow-empty"
    return "other-json"

rows, per_root, fp_seen = [], defaultdict(Counter), {}
for label, role, root, sid in ROOTS:
    if not root.exists():
        per_root[label]["MISSING"] = 1
        continue
    for p in sorted(root.rglob("*.json")):
        if "/.git/" in str(p) or "/node_modules/" in str(p):
            continue
        err = None; d = None
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception as e:
            try: d = json.load(open(p, encoding="utf-8-sig"))
            except Exception as e2: err = str(e2)[:80]
        kind = classify(p, d, err)
        digest = sha256(p)
        wf_name = (d.get("name") if isinstance(d, dict) and isinstance(d.get("name"), str) else "") or ""
        prov = ""
        if isinstance(d, dict) and isinstance(d.get("meta"), dict) and isinstance(d["meta"].get("collectionProvenance"), dict):
            prov = d["meta"]["collectionProvenance"].get("source", "")
        src = SRC_META[sid]["repo"] if sid else (prov or label)
        lic = SRC_META[sid]["license"] if sid else ("" if not prov else next((m["license"] for m in SRC_META.values() if m["attribution"] == prov), ""))
        rows.append({"path": str(p), "root": label, "role": role, "kind": kind, "name": wf_name or p.stem,
                     "size_bytes": p.stat().st_size, "known_source": src, "license": lic, "sha256": digest,
                     "node_count": len(d["nodes"]) if kind == "workflow" else "", "parse_error": err or ""})
        per_root[label][kind] += 1
        if kind == "workflow":
            fp_seen.setdefault(digest, []).append(label)

out = WC / "audit"
with open(out / "WORKFLOW_INVENTORY.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

# link lists
links = Counter(); link_files = Counter()
for p in SP.rglob("*"):
    if p.is_file() and p.suffix.lower() in (".md", ".json", ".csv", ".txt", ".html") and "/.git/" not in str(p):
        try: txt = p.read_text(encoding="utf-8", errors="ignore")
        except Exception: continue
        found = set(re.findall(r"n8n\.io/workflows/(\d+)", txt))
        if found:
            links.update(found); link_files[str(p.relative_to(SP))] = len(found)
gh = set()
for p in SP.rglob("README*.md"):
    gh.update(re.findall(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", p.read_text(encoding="utf-8", errors="ignore")))

summary = {
    "roots": {l: dict(c) for l, c in per_root.items()},
    "total_json_files": len(rows),
    "total_workflow_files": sum(1 for r in rows if r["kind"] == "workflow"),
    "unique_workflow_sha256_all_roots": len(fp_seen),
    "unique_workflow_sha256_raw_sources": len({r["sha256"] for r in rows if r["kind"] == "workflow" and r["root"].startswith("raw-source")}),
    "unique_n8n_io_template_links": len(links),
    "files_containing_n8n_io_links": len(link_files),
    "top_link_files": link_files.most_common(15),
    "unique_github_repo_links_in_readmes": sorted(gh),
    "total_bytes": sum(r["size_bytes"] for r in rows),
}
json.dump(summary, open(out / "inventory_summary.json", "w"), indent=2, ensure_ascii=False)
print(json.dumps(summary, indent=2, ensure_ascii=False))
