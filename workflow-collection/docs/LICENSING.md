# Licensing & legal checklist

Short version: **you can legally sell MIT and CC BY workflows, you cannot sell unlicensed ones, and n8n.io templates are off-limits for bundling.** What you sell is the curation, cleaning, organisation, documentation and support, not the raw files (anyone can download those for free).

## Rules the pipeline enforces

1. Only sources with `license_ok: true` in `scripts/sources.json` can reach `collection/sellable/`.
2. Sources without a LICENSE file go to `collection/rights-needed/` and are git-ignored, so they never ship.
3. Every file keeps its provenance in `meta.collectionProvenance`.
4. Hardcoded API keys, tokens, webhook URLs, passwords and JWTs are replaced with `<<REDACTED-REPLACE-WITH-YOUR-OWN>>` (27 files were affected).
5. `pinData`, instance ids, webhook ids, credential ids and owner data are stripped.

## What each license requires from you

| License | Can sell? | You must | You must not |
|---|---|---|---|
| MIT | Yes | Include the MIT notice + copyright line of the source in the bundle (a `THIRD_PARTY_LICENSES.txt`) | Claim the original authors endorse you |
| CC BY 4.0 | Yes | Credit the source (repo name + link), state the license, say if you modified it | Add DRM; remove attribution |
| No license | **No** | Get written permission (an email is enough) or leave it out | Redistribute at all |
| n8n Sustainable Use License | n/a | This is n8n's *software* license. It does not cover template JSON, but n8n.io template pages have their own terms that do not grant resale | Bundle n8n.io templates |

## Residual risk and how to limit it

- An aggregator that says "MIT" may have included files it did not have the right to relicense. Zie619's repo already had one DMCA episode. Mitigation: keep provenance, honour takedown requests within 48 hours, and prefer your own original workflows for the premium tier.
- Workflows can embed other people's prompts, copy or brand names in sticky notes. The review checklist asks you to read sticky notes of every premium item.
- Sell under clear buyer terms: personal and commercial use allowed, **no resale or redistribution of the files**. That matches what the market does.

## Files to ship with every bundle

- `LICENSE-BUNDLE.txt` : your terms for the buyer.
- `THIRD_PARTY_LICENSES.txt` : MIT text + copyright lines for Zie619 and oxbshw, CC BY 4.0 notice for enescingoz.
- `PROVENANCE.csv` : id, name, source, source path (export from `catalog/catalog.csv`).
