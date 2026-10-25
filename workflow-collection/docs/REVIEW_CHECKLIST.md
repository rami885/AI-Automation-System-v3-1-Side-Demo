# Review checklist

The pipeline does the mechanical review. A human (or Claude on your computer) does the rest. Work from `catalog/review_report.md` and `catalog/catalog.csv`.

## A. Automatic (already done by `collect.py`)
- [x] Valid n8n JSON with nodes + connections
- [x] Exact duplicates removed (content fingerprint ignoring sticky notes and positions)
- [x] Same-name structural variants demoted
- [x] Synthetic skeletons demoted
- [x] Secrets redacted, pinData / ids / webhook ids stripped, `active` forced to false
- [x] Category, tier, quality score, integrations, trigger type extracted
- [x] Provenance embedded

## B. Per premium workflow (591 items, ~3 min each)
- [ ] Open in n8n (import JSON) and confirm it renders without "unknown node" errors
- [ ] Read every sticky note: remove personal names, client names, internal URLs, foreign-language leftovers you do not want
- [ ] Confirm the display name describes the outcome ("Summarize Gmail threads to Notion daily"), not the nodes
- [ ] Confirm credentials are referenced by generic names ("OpenAI account") and nothing is hardcoded
- [ ] Note required credentials and any paid API in the setup guide
- [ ] Deprecated nodes: replace Function → Code, Cron → Schedule Trigger, Item Lists → Split Out/Aggregate where easy
- [ ] Write a 2-line value statement for the listing

## C. Per standard workflow (sampling is fine)
- [ ] Rename the 1,793 auto-named items (see `catalog/rename_queue.csv`); an LLM pass does this in one go
- [ ] Spot-check 5% per category for import errors
- [ ] Anything that fails twice goes back to review-only (`--min-score` or manual move)

## D. Bundle level
- [ ] `THIRD_PARTY_LICENSES.txt` and `PROVENANCE.csv` present
- [ ] One `README.md` per category folder (what is inside, requirements, how to import)
- [ ] Master `INDEX.md` with search-friendly names
- [ ] Zip opens cleanly on Windows and macOS (no paths > 200 chars; slugs are capped at 70)
- [ ] Test-import 10 random files on a fresh n8n (docker `n8nio/n8n:latest`)
