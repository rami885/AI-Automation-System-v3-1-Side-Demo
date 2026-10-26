# Sources

Where the workflows come from, what license each source carries, and how that decides whether a file can be sold.

| # | Source | License | Unique workflows found | In sellable set? | Notes |
|---|---|---|---:|---|---|
| 1 | [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) | MIT | 1,961 | Yes | Largest community aggregator (2,000+ files, 188 integration folders). ~420 of its files are synthetic "(Template)" skeletons which the pipeline demotes. Repo history was rewritten once after a DMCA notice, so provenance is recorded per file. |
| 2 | [oxbshw/ultimate-n8n-ai-workflows](https://github.com/oxbshw/ultimate-n8n-ai-workflows) | MIT | 2,369 | Yes | 3,600+ files, strongest AI/agent coverage. Heavy overlap with #1 (dedupe removes ~1,100 exact copies). |
| 3 | [enescingoz/awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) | CC BY 4.0 | 107 | Yes, with attribution | Curated by integration (Gmail, Notion, Telegram, WhatsApp…). CC BY requires crediting the source in the product. |
| 4 | [wassupjay/n8n-free-templates](https://github.com/wassupjay/n8n-free-templates) | **none** | 202 | **No** (rights-needed) | 25 industry verticals (healthcare, legal, real estate, agriculture…). No LICENSE file means all rights reserved. Ask the author for written permission before selling. |
| 5 | [lucaswalter/n8n-ai-workflows](https://github.com/lucaswalter/n8n-ai-workflows) | **none** | 28 | **No** (rights-needed) | 38 high-value AI agent builds (voice agent, Gmail agent, lead gen). Review-only; good benchmark for what "premium" looks like. |

Totals after processing: 6,283 files scanned, 5,843 valid n8n exports, 1,176 exact duplicates removed, **4,667 unique workflows**, **3,304 cleared for sale**.

## Candidate sources to evaluate next (run on your computer, see `LOCAL_PROMPT.md`)

Check the LICENSE file first. Only MIT / Apache-2.0 / BSD / CC BY / CC0 / Unlicense are safe for resale.

- GitHub topics: `n8n-workflows`, `n8n-templates`, `n8n-workflow`, `n8n-automation` (sort by stars, skip forks of #1 and #2).
- Your own n8n instance (83 workflows at the time of writing). These are the only ones you own outright and can sell at any price, but they contain business data (DRFONE, Wolt, Kanboard) and must be generalized and sanitized first.
- n8n.io official template library (3,000+). n8n's template terms do **not** grant resale rights; use it as inspiration or link to it, do not bundle.
- Make.com public blueprints and Zapier templates: different platform, different license per blueprint. Only consider if you want a multi-platform product.

## Provenance inside each file

Every sellable JSON carries `meta.collectionProvenance = {source, sourcePath, id}` so that any file can be traced back to its origin if a rights question ever comes up.
