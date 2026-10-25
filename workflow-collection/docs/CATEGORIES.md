# Category taxonomy (16 categories)

Categories were chosen to match how buyers search on Gumroad / Etsy / Lemon Squeezy, not how n8n names its nodes. Assignment is automatic (node types weigh 3, name keywords weigh 2; highest score wins; `utilities-building-blocks` only when nothing else matches). Secondary categories are stored in `catalog.csv` for cross-listing.

| ID | Category | Buyer persona | Sellable count |
|---|---|---|---:|
| 01 | ai-agents-llm | agencies, founders building AI assistants, RAG and agents | 694 |
| 02 | content-social-media | creators, social media managers | 119 |
| 03 | marketing-email-crm | marketers, email/CRM operators | 188 |
| 04 | sales-lead-gen | SDRs, lead-gen agencies | 63 |
| 05 | ecommerce-retail | Shopify / WooCommerce store owners | 56 |
| 06 | customer-support-chatbots | support teams, WhatsApp/Telegram bot builders | 191 |
| 07 | data-sheets-databases | ops people living in Google Sheets / Airtable / SQL | 609 |
| 08 | documents-pdf-files | back-office, invoices, PDF extraction, Drive | 289 |
| 09 | devops-it-monitoring | IT admins, SREs, security teams | 169 |
| 10 | hr-recruitment | HR, recruiters | 5 |
| 11 | finance-invoicing | finance, bookkeeping | 11 |
| 12 | productivity-project-management | Notion / Jira / Trello / calendar users | 260 |
| 13 | communication-notifications | anyone routing alerts to Slack / Discord / Telegram | 294 |
| 14 | web-scraping-research | researchers, growth hackers | 63 |
| 15 | seo-analytics | SEO specialists, analytics | 12 |
| 16 | utilities-building-blocks | n8n learners, patterns and snippets | 281 |

Thin categories (HR, finance, SEO) are the gaps to fill with **original** workflows: they are also the ones with the highest willingness to pay.

## Tiers

- **premium**: license OK, score ≥ 75, uses AI nodes. Gets a per-workflow setup guide and a higher price.
- **standard**: license OK, score ≥ 50.
- **variants**: same name and structure as a better copy; kept out of the bundle to avoid "4 copies of Google analytics template".
- **skeletons**: synthetic 5-node fillers with no integration; never sold.
- **review-only**: license OK but failed the quality gate (fix and re-run to promote).
- **rights-needed**: unlicensed source.

## Quality score (0-100)

| Signal | Points |
|---|---:|
| valid parseable n8n export | +10 |
| has a trigger node | +15 |
| ≥3 functional nodes / ≥6 | +10 / +5 |
| nodes are connected | +10 |
| sticky-note documentation (≥1 / ≥3) | +10 / +5 |
| has description | +5 |
| specific, non-generic name | +10 |
| ≥1 / ≥2 real integrations | +10 / +5 |
| uses AI nodes | +5 |
| legacy nodes (Function, Cron, Item Lists…) | −5 each (max −10) |
| hardcoded secret had to be redacted | −10 |

Change the gate with `python3 scripts/collect.py --min-score 60`.
