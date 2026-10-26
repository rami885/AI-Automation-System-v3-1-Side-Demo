#!/usr/bin/env python3
"""
n8n Workflow Collection pipeline
================================
One command: fetch public sources -> parse every workflow JSON -> dedupe ->
sanitize (strip ids, pinData, hardcoded secrets) -> auto-categorize ->
quality-score -> write the organized collection + catalog + review report.

Usage:
  python3 collect.py --fetch                 # clone/refresh sources (git, shallow)
  python3 collect.py                         # process what is in collection_src/
  python3 collect.py --min-score 60          # stricter sellable gate
  python3 collect.py --extra /path/to/my/exports  # add your own exported workflows (license: OWN)

Only the Python standard library is used.
"""
import argparse, csv, hashlib, json, os, re, shutil, subprocess, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SRC_DIR = ROOT / "collection_src"
OUT_DIR = ROOT / "collection"
CATALOG_DIR = ROOT / "catalog"

# --------------------------------------------------------------------------- taxonomy
# Order matters only for tie-breaks. Each category: keywords matched against node types
# (lowercased, without the n8n-nodes-base. / @n8n/n8n-nodes-langchain. prefix) and the
# workflow name. Node-type hits weigh 3, name hits weigh 2.
CATEGORIES = [
  ("ai-agents-llm", "AI Agents & LLM Automation", {
     "nodes": ["agent", "lmchat", "openai", "anthropic", "gemini", "ollama", "mistral", "groq", "huggingface",
               "chainllm", "chainsummarization", "memorybuffer", "outputparser", "embeddings", "vectorstore",
               "pinecone", "qdrant", "supabasevector", "toolworkflow", "toolcode", "informationextractor",
               "sentimentanalysis", "textclassifier", "chattrigger", "deepseek", "openrouter", "perplexity", "cohere"],
     "name": ["ai ", "agent", "gpt", "llm", "rag", "chatbot", "assistant", "openai", "claude", "gemini", "embedding", "vector"]}),
  ("content-social-media", "Content Creation & Social Media", {
     "nodes": ["twitter", "linkedin", "instagram", "facebook", "youtube", "tiktok", "reddit", "medium", "wordpress",
               "ghost", "pinterest", "buffer", "elevenlabs", "runway", "replicate", "stabilityai", "dalle", "leonardo"],
     "name": ["post", "tweet", "social", "video", "youtube", "blog", "article", "content", "caption", "image generation",
              "thumbnail", "newsletter", "podcast", "linkedin", "instagram", "tiktok", "shorts", "reel"]}),
  ("marketing-email-crm", "Marketing, Email & CRM", {
     "nodes": ["mailchimp", "hubspot", "activecampaign", "sendgrid", "mailgun", "brevo", "sendinblue", "convertkit",
               "klaviyo", "mailerlite", "lemlist", "customerio", "drip", "getresponse", "mautic", "pipedrive",
               "salesforce", "zohocrm", "copper", "keap", "agilecrm", "freshworkscrm", "emailsend", "emailreadimap"],
     "name": ["email", "newsletter", "campaign", "crm", "marketing", "drip", "outreach", "mailchimp", "hubspot",
              "subscriber", "lead nurtur", "cold email"]}),
  ("sales-lead-gen", "Sales & Lead Generation", {
     "nodes": ["apollo", "hunter", "clearbit", "lemlist", "calendly", "cal.com", "cal", "pipedrive", "closecrm",
               "linkedin", "phantombuster", "dropcontact", "uplead", "typeform", "jotform", "tally"],
     "name": ["lead", "prospect", "sales", "deal", "pipeline", "qualif", "enrich", "scrape linkedin", "booking",
              "appointment", "demo request", "quote", "proposal", "crm"]}),
  ("ecommerce-retail", "E-commerce & Retail", {
     "nodes": ["shopify", "woocommerce", "stripe", "paypal", "magento", "bigcommerce", "gumroad", "lemonsqueezy",
               "paddle", "chargebee", "squarespace", "etsy", "amazon", "wix"],
     "name": ["order", "product", "shop", "store", "inventory", "stock", "cart", "checkout", "sku", "price",
              "ecommerce", "e-commerce", "woocommerce", "shopify", "customer review", "refund", "shipment"]}),
  ("customer-support-chatbots", "Customer Support & Chatbots", {
     "nodes": ["zendesk", "freshdesk", "intercom", "helpscout", "crisp", "chatwoot", "zohodesk", "frontapp",
               "whatsapp", "telegram", "line", "twilio", "messagebird", "vonage", "facebookmessenger"],
     "name": ["support", "ticket", "chatbot", "customer service", "faq", "helpdesk", "whatsapp bot", "telegram bot",
              "reply", "inbound", "complaint", "voice agent", "receptionist"]}),
  ("data-sheets-databases", "Data, Spreadsheets & Databases", {
     "nodes": ["googlesheets", "airtable", "postgres", "mysql", "mongodb", "supabase", "redis", "snowflake",
               "bigquery", "microsoftexcel", "nocodb", "baserow", "seatable", "coda", "grist", "stackby", "quickbase",
               "mssql", "crateDb", "questdb", "timescaledb", "elasticsearch", "spreadsheetfile", "converttofile"],
     "name": ["sheet", "spreadsheet", "database", "sql", "sync", "export", "import", "csv", "excel", "airtable",
              "table", "etl", "backup", "dedupe", "report"]}),
  ("documents-pdf-files", "Documents, PDF & File Processing", {
     "nodes": ["googledocs", "googledrive", "dropbox", "box", "onedrive", "nextcloud", "s3", "awss3", "ftp", "readpdf",
               "extractfromfile", "pdfco", "docusign", "pandadoc", "mindee", "microsoftonedrive", "readbinaryfile",
               "writebinaryfile", "compression", "googleslides", "microsoftword", "readwritefile"],
     "name": ["pdf", "document", "invoice", "receipt", "ocr", "file", "contract", "resume", "cv", "transcri",
              "summar", "upload", "drive", "docs", "attachment"]}),
  ("devops-it-monitoring", "DevOps, IT & Monitoring", {
     "nodes": ["github", "gitlab", "bitbucket", "jenkins", "travisci", "circleci", "docker", "kubernetes", "aws",
               "awslambda", "awsses", "awssns", "awssqs", "googlecloud", "azure", "digitalocean", "vercel", "netlify",
               "cloudflare", "uptimerobot", "pagerduty", "opsgenie", "sentry", "grafana", "prometheus", "datadog",
               "ssh", "executecommand", "git", "rabbitmq", "kafka", "mqtt", "n8n", "n8ntrigger", "errortrigger",
               "homeassistant", "philipshue", "crowdsec", "theHive", "cortex", "misp", "virustotal", "shodan"],
     "name": ["deploy", "server", "monitor", "uptime", "alert", "incident", "backup", "github", "gitlab", "ci/cd",
              "docker", "kubernetes", "log", "error", "security", "vulnerab", "devops", "ssl", "domain", "dns",
              "n8n workflow", "health check"]}),
  ("hr-recruitment", "HR & Recruitment", {
     "nodes": ["bamboohr", "workable", "greenhouse", "lever", "personio", "gusto", "humaans", "bamboo"],
     "name": ["hr", "recruit", "candidate", "applicant", "hiring", "interview", "job", "onboard", "employee",
              "resume", "cv screening", "payroll", "leave request", "vacation"]}),
  ("finance-invoicing", "Finance, Accounting & Invoicing", {
     "nodes": ["quickbooks", "xero", "stripe", "paypal", "wise", "invoiceninja", "freshbooks", "zohobooks",
               "coinbase", "binance", "plaid", "revolut", "mollie", "splitwise"],
     "name": ["invoice", "expense", "payment", "accounting", "bookkeep", "tax", "budget", "crypto", "bitcoin",
              "stock price", "trading", "finance", "financial", "receipt", "reconcil", "subscription billing"]}),
  ("productivity-project-management", "Productivity & Project Management", {
     "nodes": ["notion", "asana", "trello", "clickup", "monday", "jira", "linear", "todoist", "googlecalendar",
               "microsofttodo", "microsoftoutlook", "googletasks", "basecamp", "wrike", "taiga", "kanboard",
               "microsoftteams", "zoom", "googlemeet", "calendly", "toggl", "clockify", "harvest", "evernote",
               "onenote", "obsidian", "ticktick", "beeminder"],
     "name": ["task", "todo", "to-do", "project", "meeting", "calendar", "schedule", "reminder", "notion", "jira",
              "trello", "asana", "daily", "weekly", "standup", "agenda", "note"]}),
  ("communication-notifications", "Team Communication & Notifications", {
     "nodes": ["slack", "discord", "mattermost", "rocketchat", "telegram", "microsoftteams", "pushover", "pushbullet",
               "gotify", "ntfy", "signal", "matrix", "twilio", "sms", "vonage", "msg91", "plivo", "gmail", "emailsend"],
     "name": ["notify", "notification", "alert", "slack", "discord", "message", "announce", "digest", "sms",
              "broadcast", "channel"]}),
  ("web-scraping-research", "Web Scraping & Research", {
     "nodes": ["htmlextract", "rssfeedread", "rssfeedreadtrigger", "firecrawl", "apify",
               "scrapingbee", "brightdata", "serpapi", "jina", "browserless", "puppeteer", "playwright", "crawl",
               "wikipedia", "hackernews", "newsapi", "googlesearch", "bing", "tavily", "exa"],
     "name": ["scrap", "crawl", "extract", "rss", "news", "research", "monitor website", "price track", "competitor",
              "search", "web", "trend", "hacker news", "reddit"]}),
  ("seo-analytics", "SEO & Analytics", {
     "nodes": ["googleanalytics", "googlesearchconsole", "searchconsole", "ahrefs", "semrush", "matomo", "plausible",
               "posthog", "mixpanel", "segment", "googleads", "facebookads", "metaads", "linkedinads", "googletagmanager"],
     "name": ["seo", "keyword", "rank", "serp", "analytics", "traffic", "backlink", "search console", "ads",
              "campaign performance", "utm", "conversion", "ga4"]}),
  ("utilities-building-blocks", "Utilities & Building Blocks", {
     "nodes": ["set", "code", "function", "if", "switch", "merge", "splitinbatches", "wait", "datetime",
               "crypto", "itemlists", "renamekeys", "limit", "sort", "aggregate", "splitout", "filter", "compare",
               "executeworkflow", "noop", "stopanderror", "respondtowebhook", "webhook", "manualtrigger"],
     "name": ["example", "demo", "test", "template", "how to", "pattern", "loop", "batch", "merge", "error handling",
              "rate limit", "pagination", "retry", "utility", "helper", "sub-workflow", "subworkflow"]}),
]
CAT_IDS = [c[0] for c in CATEGORIES]
CAT_TITLES = {c[0]: c[1] for c in CATEGORIES}
# generic nodes that must not count as "integrations"
CORE_NODES = {"set", "code", "function", "functionitem", "if", "switch", "merge", "splitinbatches", "wait", "datetime",
              "crypto", "itemlists", "renamekeys", "limit", "sort", "aggregate", "splitout", "filter", "compare",
              "executeworkflow", "executeworkflowtrigger", "noop", "stopanderror", "respondtowebhook", "webhook",
              "manualtrigger", "scheduletrigger", "cron", "interval", "stickynote", "httprequest", "html", "markdown",
              "xml", "moveBinaryData".lower(), "converttofile", "extractfromfile", "editimage", "removeduplicates",
              "summarize", "errortrigger", "formtrigger", "form", "n8ntrigger", "chattrigger", "debughelper",
              "readwritefile", "readbinaryfile", "writebinaryfile", "spreadsheetfile", "emailsend", "emailreadimap",
              "ssh", "executecommand", "ftp", "git", "n8n", "rssfeedread", "rssfeedreadtrigger", "workflow", "start",
              "comparedatasets", "n8ntrainingcustomerdatastore", "n8ntrainingcustomermessenger", "splitinbatches", "dateTime".lower(),
              "executiondata", "sticky", "scheduletrigger", "localfiletrigger", "emailreadimap", "sendemail", "wait"}
TRIGGER_HINTS = ("trigger", "webhook", "cron", "interval", "formtrigger", "chattrigger", "manualtrigger")
LEGACY_NODES = {"function", "functionitem", "cron", "interval", "itemlists", "spreadsheetfile", "readbinaryfile",
                "writebinaryfile", "readbinaryfiles", "movebinarydata", "start", "executeworkflow"}

# --------------------------------------------------------------------------- secrets
SECRET_PATTERNS = [
  ("openai_key", re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{20,}")),
  ("anthropic_key", re.compile(r"sk-ant-[A-Za-z0-9_-]{20,}")),
  ("github_token", re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}")),
  ("slack_token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
  ("slack_webhook", re.compile(r"hooks\.slack\.com/services/T[A-Z0-9]+/B[A-Z0-9]+/[A-Za-z0-9]+")),
  ("discord_webhook", re.compile(r"discord(?:app)?\.com/api/webhooks/\d+/[A-Za-z0-9_-]{30,}")),
  ("telegram_bot_token", re.compile(r"\b\d{8,10}:[A-Za-z0-9_-]{35}\b")),
  ("google_api_key", re.compile(r"AIza[0-9A-Za-z_-]{35}")),
  ("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
  ("stripe_key", re.compile(r"\b[sr]k_(?:live|test)_[A-Za-z0-9]{20,}\b")),
  ("bearer_token", re.compile(r"Bearer\s+[A-Za-z0-9._~+/=-]{32,}")),
  ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
  ("private_key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
  ("sendgrid_key", re.compile(r"\bSG\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\b")),
]
PLACEHOLDER_RE = re.compile(r"(?i)your[_ -]?(api|key|token|id|email|webhook)|<[^>]{3,40}>|xxx+|placeholder|change[_ -]?me|replace[_ -]?me")

# --------------------------------------------------------------------------- naming
GENERIC_NAME_RE = re.compile(
    r"(?i)^(?:\d{3,4}[_ -]+)?(?:my workflow(?: \d+)?|workflow(?: \d+)?|untitled|new workflow|test(?:ing)?|demo|copy of .*|"
    r"production workflow|[a-z0-9]+ workflow|\w+trigger workflow|[a-z]+ [a-z]+ workflow|"
    r"(?:\w+ ){1,4}(?:automate|automation|create|update|send|process|triggered|scheduled|webhook|manual)(?: \w+){0,3})$")

def is_generic_name(name: str) -> bool:
    n = (name or "").strip()
    if len(n) < 9: return True
    if GENERIC_NAME_RE.match(n): return True
    # aggregator pattern: "0382 Schedule Spotify Create Scheduled" / "Httprequest Workflow"
    if re.match(r"^\d{3,4}[_ ]", n): return True
    return False

def generate_name(integrations: list, stypes: list, is_ai: bool) -> str:
    pretty = {"googlesheets": "Google Sheets", "googledrive": "Google Drive", "googlecalendar": "Google Calendar",
              "googledocs": "Google Docs", "gmail": "Gmail", "httprequest": "HTTP API", "whatsapp": "WhatsApp",
              "linkedin": "LinkedIn", "youtube": "YouTube", "wordpress": "WordPress", "hubspot": "HubSpot",
              "mongodb": "MongoDB", "mysql": "MySQL", "postgres": "Postgres", "openai": "OpenAI", "activecampaign": "ActiveCampaign",
              "microsoftoutlook": "Outlook", "microsoftteams": "Microsoft Teams", "microsoftexcel": "Excel", "woocommerce": "WooCommerce",
              "clickup": "ClickUp", "nocodb": "NocoDB", "github": "GitHub", "gitlab": "GitLab", "rssfeedread": "RSS", "bamboohr": "BambooHR"}
    parts = [pretty.get(i, i.replace("_", " ").title()) for i in integrations[:3]]
    if any(t in ("webhook", "formtrigger", "chattrigger") or (t.endswith("trigger") and t not in ("manualtrigger", "scheduletrigger", "executeworkflowtrigger")) for t in stypes):
        mode = "Event-Triggered"
    elif any(t in ("scheduletrigger", "cron", "interval") for t in stypes):
        mode = "Scheduled"
    else:
        mode = "On-Demand"
    kind = "AI Agent" if is_ai else "Automation"
    if not parts:
        return f"{mode} {kind} Template"
    return f"{' + '.join(parts)} {mode} {kind}"

# --------------------------------------------------------------------------- helpers
def slugify(text: str, maxlen: int = 70) -> str:
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode()
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return (text[:maxlen].rstrip("-")) or "workflow"

def short_type(t: str) -> str:
    t = (t or "").lower()
    for p in ("n8n-nodes-base.", "@n8n/n8n-nodes-langchain."):
        t = t.replace(p, "")
    if "." in t:                       # community packages: n8n-nodes-netsuite.netsuite -> netsuite
        t = t.rsplit(".", 1)[-1]
    return t

def load_json(path: Path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        try:
            with open(path, "r", encoding="utf-8-sig") as f:
                return json.load(f)
        except Exception:
            return None

def is_workflow(d) -> bool:
    return isinstance(d, dict) and isinstance(d.get("nodes"), list) and len(d["nodes"]) > 0 and \
           all(isinstance(n, dict) and "type" in n for n in d["nodes"])

def content_fingerprint(d: dict) -> str:
    parts = []
    for n in d.get("nodes", []):
        if short_type(n.get("type")) == "stickynote":
            continue
        parts.append((n.get("type", ""), str(n.get("typeVersion", "")),
                      json.dumps(n.get("parameters", {}), sort_keys=True, ensure_ascii=False)))
    parts.sort()
    return hashlib.sha256(json.dumps(parts, ensure_ascii=False).encode()).hexdigest()[:16]

def structure_fingerprint(d: dict) -> str:
    types = sorted(short_type(n.get("type")) for n in d.get("nodes", []) if short_type(n.get("type")) != "stickynote")
    return hashlib.sha256(("|".join(types)).encode()).hexdigest()[:12]

SECRET_KEY_NAMES = re.compile(r"(?i)^(api[_-]?key|apikey|api_token|access_token|auth_token|secret|client_secret|password|passwd|token|bot_token)$")

def _looks_placeholder(v: str) -> bool:
    return bool(PLACEHOLDER_RE.search(v)) or v.strip().startswith(("{{", "=", "$", "<")) or len(v.strip()) < 12

def scan_and_redact(obj, hits, key=None):
    """Walk the workflow tree; redact secret-looking string values in place. Returns the new object."""
    if isinstance(obj, dict):
        return {k: scan_and_redact(v, hits, k) for k, v in obj.items()}
    if isinstance(obj, list):
        return [scan_and_redact(v, hits, key) for v in obj]
    if isinstance(obj, str):
        new = obj
        for name, rx in SECRET_PATTERNS:
            for m in rx.finditer(obj):
                frag = m.group(0)
                if PLACEHOLDER_RE.search(frag):
                    continue
                hits.append((name, frag))
                new = new.replace(frag, "<<REDACTED-REPLACE-WITH-YOUR-OWN>>")
        if key and SECRET_KEY_NAMES.match(str(key)) and new == obj and obj.strip() \
           and not obj.strip().startswith(("{{", "=", "$", "<")) and not PLACEHOLDER_RE.search(obj) \
           and re.fullmatch(r"[A-Za-z0-9_\-./+=:@!#%]{6,}", obj.strip()):
            hits.append(("literal_" + str(key).lower(), obj))
            new = "<<REDACTED-REPLACE-WITH-YOUR-OWN>>"
        return new
    return obj

def sanitize(d: dict) -> dict:
    """Remove instance-specific and potentially private data. Keeps everything needed to import."""
    d = dict(d)
    for k in ("id", "versionId", "pinData", "staticData", "shared", "updatedAt", "createdAt", "triggerCount",
              "activeVersionId", "homeProject", "sharedWithProjects", "usedCredentials", "scopes"):
        d.pop(k, None)
    d["active"] = False
    meta = d.get("meta") if isinstance(d.get("meta"), dict) else {}
    d["meta"] = {"templateCredsSetupCompleted": False}
    if meta.get("templateId"):
        d["meta"]["templateId"] = meta["templateId"]
    nodes = []
    for n in d.get("nodes", []):
        n = dict(n)
        n.pop("webhookId", None)
        creds = n.get("credentials")
        if isinstance(creds, dict):
            n["credentials"] = {ct: {"name": (cv.get("name") if isinstance(cv, dict) else str(cv)) or f"{ct} account"}
                                for ct, cv in creds.items()}
        nodes.append(n)
    d["nodes"] = nodes
    d.setdefault("settings", {})
    if isinstance(d["settings"], dict):
        d["settings"].pop("errorWorkflow", None)
        d["settings"].pop("timezone", None)
    return d

def categorize(name: str, stypes: list) -> tuple:
    lname = f" {name.lower()} "
    scores = {}
    for cid, _, kw in CATEGORIES:
        s = 0
        for k in kw["nodes"]:
            s += 3 * sum(1 for t in stypes if k in t and k not in ("cal", "box", "git", "n8n", "sms", "line", "form") or t == k)
        for k in kw["name"]:
            if k in lname:
                s += 2
        scores[cid] = s
    # utilities only wins when nothing else scored
    best = max((c for c in CAT_IDS if c != "utilities-building-blocks"), key=lambda c: scores[c])
    if scores[best] == 0:
        best = "utilities-building-blocks"
    ranked = sorted(scores.items(), key=lambda kv: -kv[1])
    secondary = [c for c, s in ranked[1:3] if s >= max(4, scores[best] // 2) and c != best]
    return best, secondary

def quality(d: dict, stypes: list, integrations: list, secret_hits, has_trigger: bool) -> tuple:
    score, notes = 0, []
    n = len([t for t in stypes if t != "stickynote"])
    name = (d.get("name") or "").strip()
    if has_trigger: score += 15
    else: notes.append("no trigger node")
    if n >= 3: score += 10
    if n >= 6: score += 5
    if n < 2: notes.append("too small (<2 functional nodes)")
    conns = d.get("connections") or {}
    if isinstance(conns, dict) and len(conns) >= max(1, n - 1 - 2): score += 10
    elif isinstance(conns, dict) and len(conns) == 0 and n > 1: notes.append("nodes are not connected")
    stickies = sum(1 for t in stypes if t == "stickynote")
    if stickies >= 1: score += 10
    if stickies >= 3: score += 5
    if not stickies: notes.append("no sticky-note documentation")
    if d.get("description"): score += 5
    if name and not is_generic_name(name): score += 10
    else: notes.append("generic name (display name auto-generated, review it)")
    if integrations: score += 10
    if len(integrations) >= 2: score += 5
    if any(t.startswith(("agent", "lmchat", "chainllm", "openai", "embeddings", "vectorstore")) for t in stypes): score += 5
    legacy = sorted({t for t in stypes if t in LEGACY_NODES})
    if legacy:
        score -= 5 * min(2, len(legacy)); notes.append("legacy nodes: " + ", ".join(legacy))
    if secret_hits:
        score -= 10; notes.append("hardcoded secret redacted: " + ", ".join(sorted({h[0] for h in secret_hits})))
    return max(0, min(100, score + 10)), notes   # +10 base for being a valid, parseable n8n export

# --------------------------------------------------------------------------- main
def fetch(sources):
    SRC_DIR.mkdir(parents=True, exist_ok=True)
    for s in sources:
        dest = SRC_DIR / s["id"]
        if dest.exists():
            print(f"[fetch] refreshing {s['repo']}")
            subprocess.run(["git", "-C", str(dest), "pull", "-q", "--depth", "1"], check=False)
        else:
            print(f"[fetch] cloning {s['repo']}")
            subprocess.run(["git", "clone", "-q", "--depth", "1", s["url"] + ".git", str(dest)], check=True)

def iter_files(source):
    base = SRC_DIR / source["id"]
    seen = set()
    for p in source.get("paths", ["."]):
        d = base / p
        if not d.exists():
            continue
        for f in d.rglob("*.json"):
            if any(part in (".git", "node_modules", "docs", "schemas", "catalog", "context", "static", "templates", "tests", "test") for part in f.relative_to(base).parts[:-1]):
                continue
            if f.name in ("package.json", "package-lock.json", "tsconfig.json", "manifest.json", "composer.json") or f.name.startswith("."):
                continue
            if f in seen: continue
            seen.add(f)
            yield f

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", action="store_true", help="clone/refresh sources first")
    ap.add_argument("--min-score", type=int, default=50, help="minimum quality score for the sellable set")
    ap.add_argument("--extra", action="append", default=[], help="extra folder of your own exported workflows (license OWN)")
    ap.add_argument("--no-copy", action="store_true", help="only build the catalog, do not write collection/ files")
    args = ap.parse_args()

    manifest = json.load(open(HERE / "sources.json", encoding="utf-8"))
    sources = manifest["sources"]
    for i, extra in enumerate(args.extra):
        sources.append({"id": f"own-{i+1}", "repo": extra, "url": "", "license": "OWN", "license_ok": True,
                        "attribution": "Original work", "paths": ["."], "_abs": extra})
    if args.fetch:
        fetch([s for s in sources if s.get("url")])

    records, by_fp, struct_seen = [], {}, defaultdict(list)
    stats = Counter()
    for s in sources:
        if s.get("_abs"):
            files = list(Path(s["_abs"]).rglob("*.json"))
        else:
            if not (SRC_DIR / s["id"]).exists():
                print(f"[warn] source {s['id']} not fetched; run with --fetch", file=sys.stderr); continue
            files = list(iter_files(s))
        print(f"[scan] {s['id']}: {len(files)} json files")
        for f in sorted(files):
            stats["files_seen"] += 1
            d = load_json(f)
            if not is_workflow(d):
                stats["not_a_workflow"] += 1; continue
            stats["valid_workflows"] += 1
            fp = content_fingerprint(d)
            rel = str(f.relative_to(SRC_DIR / s["id"])) if not s.get("_abs") else str(f)
            if fp in by_fp:
                by_fp[fp]["duplicates"].append(f"{s['id']}:{rel}")
                stats["exact_duplicates"] += 1
                # prefer a license_ok source as the canonical copy
                if s["license_ok"] and not by_fp[fp]["license_ok"]:
                    by_fp[fp].update(source=s["id"], source_path=rel, license=s["license"], license_ok=True, attribution=s["attribution"])
                continue
            hits = []
            d = scan_and_redact(d, hits)
            if hits:
                stats["with_secrets"] += 1
            stypes = [short_type(n.get("type")) for n in d["nodes"]]
            integrations = sorted({t.replace("trigger", "").replace("tool", "") for t in stypes
                                   if t not in CORE_NODES and not t.startswith(("lmchat", "memory", "outputparser", "embeddings", "chain", "agent", "tool", "vectorstore", "sticky"))})
            has_trigger = any(h in t for t in stypes for h in TRIGGER_HINTS)
            cat, secondary = categorize(d.get("name", ""), stypes)
            score, notes = quality(d, stypes, integrations, hits, has_trigger)
            original_name = (d.get("name") or "").strip()
            is_ai_flag = any(t.startswith(("agent", "lmchat", "chainllm", "openai")) for t in stypes)
            name_generated = is_generic_name(original_name)
            name = generate_name(integrations, stypes, is_ai_flag) if name_generated else original_name
            name = re.sub(r"\s+", " ", name).strip()
            sticky_text = " ".join(str(n.get("parameters", {}).get("content", "")) for n in d["nodes"] if short_type(n.get("type")) == "stickynote")
            desc = (d.get("description") or re.sub(r"\s+", " ", re.sub(r"[#*_`>\[\]()]+", " ", sticky_text))[:300]).strip()
            rec = dict(id=None, fingerprint=fp, struct=structure_fingerprint(d), name=name, original_name=original_name,
                       name_generated=name_generated, slug=slugify(name),
                       category=cat, secondary=secondary, source=s["id"], source_path=rel, license=s["license"],
                       license_ok=s["license_ok"], attribution=s["attribution"],
                       node_count=len([t for t in stypes if t != "stickynote"]), node_types=sorted(set(stypes)),
                       integrations=integrations, has_trigger=has_trigger, is_ai=is_ai_flag,
                       quality=score, notes=notes, secrets_redacted=sorted({h[0] for h in hits}), description=desc,
                       duplicates=[], _data=sanitize(d))
            by_fp[fp] = rec
            struct_seen[rec["struct"]].append(fp)
            records.append(rec)

    # near-duplicate flag
    for st, fps in struct_seen.items():
        if len(fps) > 1:
            for fp in fps:
                by_fp[fp]["near_duplicates"] = len(fps) - 1
    # variants: identical structure AND same (non-generated) name -> keep only the best-scoring copy as sellable
    groups = defaultdict(list)
    for r in records:
        if not r["name_generated"]:
            groups[(r["slug"], r["struct"])].append(r)
    for g in groups.values():
        g.sort(key=lambda r: (-int(r["license_ok"]), -r["quality"], len(json.dumps(r["_data"]))))
        for v in g[1:]:
            v["variant_of"] = g[0]["fingerprint"]; stats["variants_demoted"] += 1
    for r in records:
        r.setdefault("near_duplicates", 0); r.setdefault("variant_of", None)
        # synthetic skeletons: no real integration, no AI, and the same bare structure repeated many times
        r["skeleton"] = bool(not r["integrations"] and not r["is_ai"] and
                             (r["near_duplicates"] >= 5 or re.search(r"(?i)\(template\)\s*$", r["name"])))
        if r["skeleton"]: stats["skeletons_demoted"] += 1; r["notes"].append("synthetic skeleton (generic structure, no integration)")
        r["sellable"] = bool(r["license_ok"] and r["quality"] >= args.min_score and r["node_count"] >= 2
                             and not r["variant_of"] and not r["skeleton"])
        r["tier"] = ("premium" if r["sellable"] and r["quality"] >= 75 and r["is_ai"] else
                     "standard" if r["sellable"] else
                     "review-only" if r["license_ok"] else "rights-needed")

    # assign ids per category, write files
    records.sort(key=lambda r: (r["category"], -r["quality"], r["name"].lower()))
    counters = Counter()
    if not args.no_copy and OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    for r in records:
        counters[r["category"]] += 1
        r["id"] = f"{CAT_IDS.index(r['category'])+1:02d}-{counters[r['category']]:04d}"
        folder = ("sellable" if r["sellable"] else "variants" if r["variant_of"] else "skeletons" if r["skeleton"]
                  else "review-only" if r["license_ok"] else "rights-needed")
        r["file"] = f"collection/{folder}/{r['category']}/{r['id']}-{r['slug']}.json"
        if not args.no_copy:
            out = ROOT / r["file"]
            out.parent.mkdir(parents=True, exist_ok=True)
            data = r["_data"]
            data["name"] = r["name"]
            data.setdefault("meta", {})["collectionProvenance"] = {"source": r["attribution"], "sourcePath": r["source_path"], "id": r["id"]}
            with open(out, "w", encoding="utf-8") as fh:
                json.dump(data, fh, ensure_ascii=False, indent=1)
        r.pop("_data", None)

    # catalog outputs
    CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    pub = [r for r in records]
    with open(CATALOG_DIR / "catalog.json", "w", encoding="utf-8") as fh:
        json.dump({"generated_from": [s["repo"] for s in sources], "categories": [{"id": c, "title": CAT_TITLES[c]} for c in CAT_IDS],
                   "count": len(pub), "workflows": pub}, fh, ensure_ascii=False, indent=1)
    cols = ["id", "name", "original_name", "name_generated", "category", "tier", "quality", "sellable", "license", "source", "node_count", "has_trigger", "is_ai",
            "integrations", "secondary", "near_duplicates", "variant_of", "skeleton", "secrets_redacted", "notes", "file", "source_path", "description"]
    with open(CATALOG_DIR / "catalog.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in pub:
            row = dict(r); 
            for k in ("integrations", "secondary", "secrets_redacted", "notes"):
                row[k] = "; ".join(map(str, r[k]))
            w.writerow(row)

    sell = [r for r in records if r["sellable"]]
    # rename queue: sellable workflows whose display name was auto-generated -> feed to an LLM renaming pass
    with open(CATALOG_DIR / "rename_queue.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh); w.writerow(["id", "file", "current_name", "category", "integrations", "node_types", "description_hint"])
        for r in sell:
            if r["name_generated"]:
                w.writerow([r["id"], r["file"], r["name"], r["category"], "; ".join(r["integrations"]), "; ".join(r["node_types"]), r["description"][:200]])
    cat_counts = Counter(r["category"] for r in sell)
    tier_counts = Counter(r["tier"] for r in records)
    integ = Counter(i for r in sell for i in r["integrations"])
    summary = {
        "files_seen": stats["files_seen"], "valid_workflows": stats["valid_workflows"], "not_a_workflow": stats["not_a_workflow"],
        "exact_duplicates_removed": stats["exact_duplicates"], "unique_workflows": len(records),
        "variants_demoted": stats["variants_demoted"], "skeletons_demoted": stats["skeletons_demoted"], "names_auto_generated_sellable": sum(1 for r in records if r["sellable"] and r["name_generated"]),
        "with_hardcoded_secrets_redacted": stats["with_secrets"], "sellable": len(sell),
        "premium": tier_counts["premium"], "standard": tier_counts["standard"], "review_only": tier_counts["review-only"],
        "rights_needed": tier_counts["rights-needed"], "ai_workflows_sellable": sum(1 for r in sell if r["is_ai"]),
        "distinct_integrations_sellable": len(integ), "min_score": args.min_score,
        "per_category_sellable": {c: cat_counts.get(c, 0) for c in CAT_IDS},
        "top_integrations": integ.most_common(40),
        "per_source": {s["id"]: Counter(r["source"] for r in records)[s["id"]] for s in sources},
    }
    with open(CATALOG_DIR / "stats.json", "w", encoding="utf-8") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=2)

    # CATALOG.md (sellable set, grouped)
    lines = ["# Workflow Catalog (sellable set)", "",
             f"{len(sell)} unique, license-cleared, sanitized n8n workflows in {len(cat_counts)} categories.",
             f"Generated by `scripts/collect.py` (min quality score {args.min_score}).", ""]
    lines += ["| Category | Workflows | AI-powered |", "|---|---:|---:|"]
    for c in CAT_IDS:
        rs = [r for r in sell if r["category"] == c]
        lines.append(f"| {CAT_TITLES[c]} | {len(rs)} | {sum(1 for r in rs if r['is_ai'])} |")
    lines.append("")
    for c in CAT_IDS:
        rs = [r for r in sell if r["category"] == c]
        if not rs: continue
        lines += [f"## {CAT_TITLES[c]} ({len(rs)})", "", "| ID | Workflow | Tier | Score | Nodes | Integrations |", "|---|---|---|---:|---:|---|"]
        for r in rs:
            lines.append(f"| {r['id']} | [{r['name'][:70]}]({r['file']}) | {r['tier']} | {r['quality']} | {r['node_count']} | {', '.join(r['integrations'][:5])} |")
        lines.append("")
    (CATALOG_DIR / "CATALOG.md").write_text("\n".join(lines), encoding="utf-8")

    # review report
    rep = ["# Review report", "", "## Summary", ""]
    for k, v in summary.items():
        if k in ("per_category_sellable", "top_integrations", "per_source"): continue
        rep.append(f"- **{k}**: {v}")
    rep += ["", "## Per source", "", "| Source | Unique workflows | License | Sellable? |", "|---|---:|---|---|"]
    for s in sources:
        rep.append(f"| {s['repo']} | {summary['per_source'][s['id']]} | {s['license']} | {'yes' if s['license_ok'] else 'NO - rights needed'} |")
    rep += ["", "## Top 40 integrations in the sellable set", "", "| Integration | Workflows |", "|---|---:|"]
    rep += [f"| {i} | {n} |" for i, n in summary["top_integrations"]]
    flagged = [r for r in records if r["secrets_redacted"]]
    rep += ["", f"## Workflows that contained hardcoded secrets (redacted automatically): {len(flagged)}", "",
            "| ID | Name | Secret types | Source |", "|---|---|---|---|"]
    rep += [f"| {r['id']} | {r['name'][:60]} | {', '.join(r['secrets_redacted'])} | {r['source']}:{r['source_path']} |" for r in flagged[:200]]
    low = [r for r in records if r["license_ok"] and not r["sellable"]]
    rep += ["", f"## License-OK but below quality gate (manual review candidates): {len(low)}", "",
            "| ID | Name | Score | Notes |", "|---|---|---:|---|"]
    rep += [f"| {r['id']} | {r['name'][:60]} | {r['quality']} | {'; '.join(r['notes'])} |" for r in sorted(low, key=lambda r: -r["quality"])[:300]]
    near = [r for r in sell if r["near_duplicates"]]
    rep += ["", f"## Sellable workflows with structural near-duplicates (consider merging/renaming): {len(near)}", ""]
    rep += [f"- {r['id']} {r['name'][:70]} (+{r['near_duplicates']} similar)" for r in near[:150]]
    (CATALOG_DIR / "review_report.md").write_text("\n".join(rep), encoding="utf-8")

    print(json.dumps({k: v for k, v in summary.items() if k not in ("top_integrations",)}, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
