# WORKFLOW_LOCATION_REPORT

Generated: 2026-10-26 13:06 UTC  
Environment: **Claude Code cloud container** (hostname `vm`, user root). This is NOT the user's personal computer; nothing on the user's PC was scanned (see section 8).

## 1. Where the collection lives (full paths)

| Path | Role | JSON files | Workflow files | Size |
|---|---|---:|---:|---:|
| `/tmp/claude-0/-home-user-AI-Automation-System-v3-1-Side-Demo/7255c058-9a75-5e0e-86fb-a8a4a68fbd6b/scratchpad/src/n8n-workflows` | raw git clone of Zie619/n8n-workflows (MIT) | 2077 | 2066 | 39.2 MB |
| `/tmp/claude-0/-home-user-AI-Automation-System-v3-1-Side-Demo/7255c058-9a75-5e0e-86fb-a8a4a68fbd6b/scratchpad/src/ultimate-n8n-ai-workflows` | raw git clone of oxbshw/ultimate-n8n-ai-workflows (MIT) | 3663 | 3187 | 47.9 MB |
| `/tmp/claude-0/-home-user-AI-Automation-System-v3-1-Side-Demo/7255c058-9a75-5e0e-86fb-a8a4a68fbd6b/scratchpad/src/awesome-n8n-templates` | raw git clone of enescingoz/awesome-n8n-templates (CC-BY-4.0) | 369 | 361 | 5.5 MB |
| `/tmp/claude-0/-home-user-AI-Automation-System-v3-1-Side-Demo/7255c058-9a75-5e0e-86fb-a8a4a68fbd6b/scratchpad/src/n8n-free-templates` | raw git clone of wassupjay/n8n-free-templates (NONE) | 202 | 202 | 1.4 MB |
| `/tmp/claude-0/-home-user-AI-Automation-System-v3-1-Side-Demo/7255c058-9a75-5e0e-86fb-a8a4a68fbd6b/scratchpad/src/n8n-ai-workflows` | raw git clone of lucaswalter/n8n-ai-workflows (NONE) | 38 | 38 | 1.4 MB |
| `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/collection/sellable` | **PRIMARY organized collection** (license-cleared, sanitized) | 3304 | 3304 | 47.4 MB |
| `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/collection/review-only` | derived bucket: license OK, below quality gate | 336 | 336 | 1.1 MB |
| `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/collection/variants` | derived bucket: same-name duplicates | 356 | 356 | 7.2 MB |
| `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/collection/skeletons` | derived bucket: synthetic skeletons | 441 | 441 | 1.8 MB |
| `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/collection/rights-needed` | derived bucket: unlicensed sources, not redistributable | 230 | 230 | 2.0 MB |
| `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/catalog` | catalog / index / stats (not workflows) | 2 | 0 | 6.5 MB |
| `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/scripts` | pipeline + `sources.json` | 1 | 0 | 0.00 MB |

Symlinks: `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/collection_src/<id>` -> the raw clones above (zie619, oxbshw, enescingoz, wassupjay, lucaswalter).

Also found: `SOURCES.md` at `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/docs/SOURCES.md`, `sources.json` at `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/scripts/sources.json`.

**ZIP archives:** none belonging to the collection exist in this environment (the only .zip files on disk are Go toolchain test fixtures under /usr/local/go*). The sources were obtained with `git clone --depth 1`, not as ZIP downloads.

## 2. File counts and classification

| Root | workflow | workflow-empty | index | config | other-json | invalid-json |
|---|---:|---:|---:|---:|---:|---:|
| catalog | 0 | 0 | 1 | 1 | 0 | 0 |
| collection:review-only | 336 | 0 | 0 | 0 | 0 | 0 |
| collection:rights-needed | 230 | 0 | 0 | 0 | 0 | 0 |
| collection:sellable | 3304 | 0 | 0 | 0 | 0 | 0 |
| collection:skeletons | 441 | 0 | 0 | 0 | 0 | 0 |
| collection:variants | 356 | 0 | 0 | 0 | 0 | 0 |
| raw-source:enescingoz | 361 | 0 | 0 | 0 | 0 | 8 |
| raw-source:lucaswalter | 38 | 0 | 0 | 0 | 0 | 0 |
| raw-source:oxbshw | 3187 | 0 | 5 | 4 | 467 | 0 |
| raw-source:wassupjay | 202 | 0 | 0 | 0 | 0 | 0 |
| raw-source:zie619 | 2066 | 0 | 2 | 6 | 3 | 0 |
| scripts | 0 | 0 | 0 | 1 | 0 | 0 |

- Total JSON files inventoried: **11019**
- Actual n8n workflow files (nodes + types present): **10521**
- Distinct workflow files by SHA-256 across all roots: **10206** (raw copies and sanitized copies differ by hash because sanitizing rewrites the file)
- Distinct SHA-256 among raw sources only: **5539** (byte-identical duplicates between repos: 315)
- Content-level unique workflows after the pipeline's node-fingerprint dedupe: **4667** (from 5843 valid exports in 6283 scanned files; 1176 exact duplicates removed)

Classification rules: `workflow` = JSON object with a non-empty `nodes` list of typed nodes; `index` = catalog/category/index files (e.g. oxbshw `catalog/*.index.json`, zie619 `context/*categories.json`, our `catalog/catalog.json`); `config` = package.json/schemas/settings; `invalid-json` = parse error.

## 3. Which folder is the primary collection

- **Primary:** `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/collection/sellable` — 3304 unique, license-cleared, sanitized workflows in 16 category folders. This is the only set meant for distribution and the one committed to git (PR #6).
- **Derived / excluded buckets** (same parent folder, git-ignored): review-only (1133), variants (356), skeletons (459), rights-needed (230).
- **Additional sources / copies:** the five raw clones in the scratchpad are the inputs. oxbshw and zie619 overlap heavily (oxbshw contains most of zie619's files plus its own 'generated' library). They are copies of upstream, not independent collections.
- The user's own 83 business workflows live only on the n8n instance (reached via MCP), **not on disk here**. None were exported or included anywhere in this environment.

## 4. Template link lists

- No standalone 'list of template links' file exists. Links to n8n.io templates appear only inside README files and sticky notes: **27 unique n8n.io template IDs** across 58 files (enescingoz READMEs: 11 unique; oxbshw workflows: 26 unique; overlap brings the total to 27).
- Index files that enumerate workflows (not links): `/tmp/claude-0/-home-user-AI-Automation-System-v3-1-Side-Demo/7255c058-9a75-5e0e-86fb-a8a4a68fbd6b/scratchpad/src/ultimate-n8n-ai-workflows/catalog/unified-workflows.index.json` (3,181 entries, fields: id, title, category, sourcePath, integrations, qualityScore; 0 external links), `workflows.index.json`, `generated-workflows.index.json`; `/tmp/claude-0/-home-user-AI-Automation-System-v3-1-Side-Demo/7255c058-9a75-5e0e-86fb-a8a4a68fbd6b/scratchpad/src/n8n-workflows/context/search_categories.json` (category map).
- GitHub repositories referenced in the READMEs (unique): `https://github.com/Trusera/ai-bom`, `https://github.com/YOUR_USERNAME/n8n-workflows.git`, `https://github.com/Zie619/n8n-workflows`, `https://github.com/Zie619/n8n-workflows.git`, `https://github.com/comfyanonymous/ComfyUI`, `https://github.com/enescingoz/awesome-n8n-templates`, `https://github.com/frdel/agent-zero`, `https://github.com/wassupjay/n8n-free-templates.git`.

## 5. n8n version

- **Not readable from this environment.** There is no n8n binary, Docker container, or `~/.n8n` directory here. The N8N MCP connection exposes workflow tools but no server-version field (the `"version":"1.1.0"` in its logs is the MCP server's own version, not n8n's). The user's workflows use node typeVersions scheduleTrigger 1.3, httpRequest 4.4, telegram 1.2 and settings such as `availableInMCP`, `activeVersionId`, `binaryMode`, which indicate a recent 2026 n8n release, but the exact number must be read on the host (`n8n --version`, `docker exec <container> n8n --version`, or Settings > About in the UI).

## 6. Private data separation

- The library on disk here comes from public repositories only. No files from the user's private business n8n instance are on disk, so none could leak into the inventory. The inventory CSV contains paths, names, sizes, sources and hashes only, never workflow content.
- The pipeline redacted hardcoded secrets in 27 public files; the raw clones still contain those original values and must not be shared as-is.

## 7. Files produced by this audit

- `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/audit/WORKFLOW_LOCATION_REPORT.md` (this file)
- `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/audit/WORKFLOW_INVENTORY.csv` (11019 rows: path, root, role, kind, name, size_bytes, known_source, license, sha256, node_count, parse_error)
- `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/audit/inventory_summary.json`, `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/audit/inventory.py` (read-only script, re-runnable)
- `/home/user/AI-Automation-System-v3-1-Side-Demo/workflow-collection/audit/WORKFLOW_AUDIT_HANDOFF.zip` (report + CSV + summary only)

## 8. Not found / could not be verified

- The user's personal computer, its Downloads folder, and any ZIPs or clones there: **not reachable** from this cloud container. The ~6,000-file figure matches what was cloned here (6,283 JSON files in the 5 raw clones), but nothing confirms a copy exists on the user's PC.
- Exact n8n version (see section 5).
- Any pre-existing ZIP archive of the collection.
- Any dedicated link-list file beyond README links.
- `wassupjay/n8n-free-templates` and `lucaswalter/n8n-ai-workflows` have no LICENSE file; rights status is unknown, not assumed.