# Review report

## Summary

- **files_seen**: 6283
- **valid_workflows**: 5843
- **not_a_workflow**: 440
- **exact_duplicates_removed**: 1176
- **unique_workflows**: 4667
- **variants_demoted**: 356
- **skeletons_demoted**: 459
- **names_auto_generated_sellable**: 1793
- **with_hardcoded_secrets_redacted**: 27
- **sellable**: 3304
- **premium**: 591
- **standard**: 2713
- **review_only**: 1133
- **rights_needed**: 230
- **ai_workflows_sellable**: 711
- **distinct_integrations_sellable**: 296
- **min_score**: 50

## Per source

| Source | Unique workflows | License | Sellable? |
|---|---:|---|---|
| Zie619/n8n-workflows | 1961 | MIT | yes |
| oxbshw/ultimate-n8n-ai-workflows | 2369 | MIT | yes |
| enescingoz/awesome-n8n-templates | 107 | CC-BY-4.0 | yes |
| wassupjay/n8n-free-templates | 202 | NONE | NO - rights needed |
| lucaswalter/n8n-ai-workflows | 28 | NONE | NO - rights needed |

## Top 40 integrations in the sellable set

| Integration | Workflows |
|---|---:|
| googlesheets | 522 |
| gmail | 388 |
| telegram | 319 |
| googledrive | 300 |
| slack | 247 |
| openai | 214 |
| airtable | 198 |
| notion | 114 |
| googlecalendar | 101 |
| documentdefaultdataloader | 87 |
| textsplitterrecursivecharactertextsplitter | 71 |
| informationextractor | 66 |
| hubspot | 66 |
| postgres | 64 |
| github | 57 |
| microsoftoutlook | 55 |
| wordpress | 50 |
| twitter | 50 |
| mattermost | 49 |
| discord | 47 |
| twilio | 41 |
| youtube | 40 |
| googledocs | 39 |
| mysql | 39 |
| pipedrive | 39 |
| supabase | 38 |
| redis | 37 |
| textclassifier | 36 |
| jira | 36 |
| typeform | 36 |
| whatsapp | 34 |
| openweathermap | 32 |
| shopify | 27 |
| compression | 26 |
| zendesk | 26 |
| woocommerce | 25 |
| mcpclient | 25 |
| graphql | 25 |
| dropbox | 24 |
| clearbit | 24 |

## Workflows that contained hardcoded secrets (redacted automatically): 27

| ID | Name | Secret types | Source |
|---|---|---|---|
| 01-0448 | Extract spend details (template) | literal_password | oxbshw:automation/1443_Splitout_Extractfromfile_Automation_Triggered.json |
| 01-0449 | Extract spend details (template) | literal_password | oxbshw:automation/1935_Splitout_Extractfromfile_Automation_Triggered.json |
| 01-0741 | Evolutionapi + Googletasks + Mcpclient Event-Triggered AI Ag | literal_apikey | oxbshw:workflows/1103_Googletaskstool_Telegram_Automation_Webhook.json |
| 01-0803 | Chatbot AI | bearer_token | zie619:workflows/Http/1868_HTTP_Stickynote_Automate_Webhook.json |
| 01-0804 | Chatbot AI | bearer_token | oxbshw:automation/1868_HTTP_Stickynote_Automate_Webhook.json |
| 01-0907 | Calculate the Centroid of a Set of Vectors | jwt | zie619:workflows/Code/1862_Code_Respondtowebhook_Automation_Webhook.json |
| 13-0335 | Discord Scheduled Automation | discord_webhook | oxbshw:workflows/ai-agents/0360_Discord_Cron_Automation_Scheduled.json |
| 13-0336 | Gmail + Google Calendar + Google Sheets Event-Triggered Auto | literal_password | zie619:workflows/Googlecalendar/1116_GoogleCalendar_GoogleSheets_Create_Triggered.json |
| 02-0140 | Auto Knowledge Base Article Generator | bearer_token | zie619:workflows/Code/1756_Code_HTTP_Automation_Webhook.json |
| 06-0106 | Evolutionapi + Googletasks + Telegram Event-Triggered Automa | literal_apikey | zie619:workflows/Googletaskstool/1103_Googletaskstool_Telegram_Automation_Webhook.json |
| 06-0208 | Helpdesk Integration Health Probe (Template) | openai_key | oxbshw:workflows/generated/open-workflow-library-v0/customer-support/customer-support-helpdesk-integration-health-probe/workflow.json |
| 07-0267 | Extract spend details (template) | literal_password | zie619:workflows/Splitout/1443_Splitout_Extractfromfile_Automation_Triggered.json |
| 07-0268 | Extract spend details (template) | literal_password | zie619:workflows/Splitout/1935_Splitout_Extractfromfile_Automation_Triggered.json |
| 07-0351 | Streamline Your Zoom Meetings with Secure, Automated Stripe  | literal_password | zie619:workflows/Http/0739_HTTP_Form_Automate_Webhook.json |
| 07-0362 | YT AI News Playlist Creator/AI News Form Updater | google_api_key | zie619:workflows/Telegram/0742_Telegram_Splitout_Create_Webhook.json |
| 07-0409 | Google Maps FULL | bearer_token | zie619:workflows/Http/1964_HTTP_Aggregate_Automation_Webhook.json |
| 09-0213 | At-Risk Student Monitor (Template) | openai_key | oxbshw:workflows/generated/open-workflow-library-v0/education/education-at-risk-student-monitor/workflow.json |
| 11-0011 | Quickbooks + Stripe Event-Triggered Automation | literal_client_secret | oxbshw:workflows/ai-agents/0707_HTTP_Stripe_Create_Webhook.json |
| 11-0013 | Filemaker Event-Triggered Automation | literal_secret | zie619:workflows/Webhook/0615_Webhook_Filemaker_Create_Webhook.json |
| 11-0015 | Quickbooks + Stripe Event-Triggered Automation | literal_client_secret | zie619:workflows/Http/0707_HTTP_Stripe_Create_Webhook.json |
| 03-0053 | Shopify + Mautic | literal_secret | zie619:workflows/Mautic/1526_Mautic_Webhook_Automation_Webhook.json |
| 03-0081 | Shopify + Mautic | literal_secret | oxbshw:automation/1526_Mautic_Webhook_Automation_Webhook.json |
| 03-0109 | AccountCraft WhatsApp Automation - Infridet | literal_password | oxbshw:workflows/ai-agents/0901_HTTP_GoogleSheets_Automate_Webhook.json |
| 12-0321 | Task Intake Router (Template) | openai_key | oxbshw:workflows/generated/open-workflow-library-v0/project-management/project-management-task-intake-router/workflow.json |
| 16-0350 | Create, update, and get a user using the G Suite Admin node | literal_password | oxbshw:workflows/ai-agents/0455_Manual_Gsuiteadmin_Create_Triggered.json |
| 16-0422 | Create, update, and get a user using the G Suite Admin node | literal_password | zie619:workflows/Manual/0455_Manual_Gsuiteadmin_Create_Triggered.json |
| 14-0082 | Event-Triggered Automation Template | private_key | zie619:workflows/Code/0924_Code_Respondtowebhook_Process_Webhook.json |

## License-OK but below quality gate (manual review candidates): 1133

| ID | Name | Score | Notes |
|---|---|---:|---|
| 01-0006 | AI-Generated Summary Block for WordPress Posts - with OpenAI | 95 |  |
| 01-0008 | AI-Powered Information Monitoring with OpenAI, Google Sheets | 95 |  |
| 01-0012 | Automate Pinterest Analysis & AI-Powered Content Suggestions | 95 |  |
| 01-0019 | Effortless Email Management with AI | 95 |  |
| 01-0026 | Hacker News to Video Template - AlexK1919 | 95 |  |
| 01-0028 | HR-focused automation pipeline with AI | 95 |  |
| 01-0033 | mails2notion V2 | 95 |  |
| 01-0035 | Microsoft Outlook AI Email Assistant | 95 |  |
| 01-0039 | OpenAI Assistant for Hubspot Chat | 95 |  |
| 01-0041 | OpenAI Personal Shopper with RAG and WooCommerce | 95 |  |
| 01-0048 | RAG Workflow For Stock Earnings Report Analysis | 95 |  |
| 01-0054 | Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment w | 95 |  |
| 01-0057 | Spot Workplace Discrimination Patterns with AI | 95 |  |
| 01-0060 | Telegram-bot AI Da Nang | 95 |  |
| 01-0064 | Translate Telegram audio messages with AI (55 supported lang | 95 |  |
| 01-0067 | UTM Link Creator & QR Code Generator with Scheduled Google A | 95 |  |
| 01-0069 | Voice RAG Chatbot with ElevenLabs and OpenAI | 95 |  |
| 01-0080 | 🤖🧠 AI Agent Chatbot + LONG TERM Memory + Note Storage + Tele | 95 |  |
| 02-0004 | Generate Instagram Content from Top Trends with AI Image Gen | 95 |  |
| 07-0008 | HR Job Posting and Evaluation with AI | 95 |  |
| 07-0013 | Printify Automation - Update Title and Description - AlexK19 | 95 |  |
| 07-0017 | Social Media AI Agent - Telegram | 95 |  |
| 08-0011 | Whisper Transkription copy | 95 |  |
| 01-0120 | Building RAG Chatbot for Movie Recommendations with Qdrant a | 90 |  |
| 01-0129 | Chat with Postgresql Database | 90 |  |
| 01-0179 | Fine-tuning with OpenAI models | 90 |  |
| 01-0203 | HN Who is Hiring Scrape | 90 |  |
| 01-0227 | Load Prompts from Github Repo and auto populate n8n expressi | 90 |  |
| 01-0236 | Make OpenAI Citation for File Retrieval RAG | 90 |  |
| 01-0239 | modelo do chatbot | 90 |  |
| 01-0251 | News Extraction | 90 | legacy nodes: itemlists |
| 01-0322 | Telegram RAG pdf | 90 |  |
| 01-0324 | Testing Mulitple Local LLM with LM Studio | 90 |  |
| 01-0351 | Vision-Based AI Agent Scraper - with Google Sheets, Scraping | 90 |  |
| 01-0359 | Whisper Transkription copy | 90 |  |
| 13-0010 | Email Summary Agent | 90 |  |
| 06-0004 | Play with Spotify from Telegram | 90 |  |
| 07-0023 | AI Logo Sheet Extractor to Airtable | 90 |  |
| 07-0025 | Automated Work Attendance with Location Triggers | 90 |  |
| 07-0031 | LINE BOT - Google Sheets Record Receipt | 90 |  |
| 07-0032 | n8n Community Topic Tracker by Keyword | 90 |  |
| 07-0037 | SSL Expiry Alert | 90 |  |
| 08-0022 | Extract text from PDF and image using Vertex AI (Gemini) int | 90 |  |
| 08-0024 | Extract text from PDF and image using Vertex AI (Gemini) int | 90 |  |
| 03-0002 | 2. Add Beehiiv newsletter subscribers from Gumroad sales | 90 |  |
| 03-0005 | piepdrive-test | 90 |  |
| 15-0003 | Google analytics template | 90 |  |
| 01-0382 | AI Social Media Caption Creator | 85 |  |
| 01-0402 | BambooHR AI-Powered Company Policies and Benefits Chatbot | 85 |  |
| 01-0412 | Complete Youtube | 85 |  |
| 01-0441 | Email AI Auto-responder. Summerize and send email | 85 |  |
| 01-0449 | Extract spend details (template) | 85 | hardcoded secret redacted: literal_password |
| 01-0452 | Fine-tuning with OpenAI models | 85 |  |
| 01-0509 | MongoDB Agent | 85 |  |
| 01-0510 | News Extraction | 85 | legacy nodes: itemlists |
| 01-0511 | News Extraction | 85 | legacy nodes: itemlists |
| 01-0525 | OpenAI-model-examples | 85 | legacy nodes: readbinaryfiles |
| 01-0529 | RAG & GenAI App With WordPress Content | 85 |  |
| 01-0534 | Selenium Ultimate Scraper Workflow | 85 |  |
| 01-0542 | 🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠 | 85 |  |
| 13-0030 | mails2notion V2 | 85 |  |
| 13-0045 | 🤖🧑‍💻 AI Agent for Top n8n Creators Leaderboard Reporting | 85 |  |
| 02-0008 | AI-Generated Summary Block for WordPress Posts - with OpenAI | 85 |  |
| 02-0014 | Generate Instagram Content from Top Trends with AI Image Gen | 85 |  |
| 02-0016 | Post New YouTube Videos to X | 85 |  |
| 06-0021 | Telegram Tron Wallet Blacklist Checker | 85 |  |
| 06-0024 | Telegram-bot AI Da Nang | 85 |  |
| 06-0026 | 🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠 | 85 |  |
| 07-0051 | AI-Powered Information Monitoring with OpenAI, Google Sheets | 85 |  |
| 07-0056 | Automate Pinterest Analysis & AI-Powered Content Suggestions | 85 |  |
| 07-0058 | AutoQoutesV2_template | 85 |  |
| 07-0064 | Dynamically create tables in Airtable for your Webflow form  | 85 |  |
| 07-0081 | HR Job Posting and Evaluation with AI | 85 |  |
| 07-0082 | Image-to-3D | 85 |  |
| 07-0090 | Microsoft Outlook AI Email Assistant | 85 |  |
| 07-0098 | RAG & GenAI App With WordPress Content | 85 |  |
| 07-0099 | Scrape Books from URL with Dumpling AI, Clean HTML, Save to  | 85 |  |
| 07-0106 | Social Media AI Agent - Telegram | 85 |  |
| 07-0116 | Umami analytics template | 85 |  |
| 07-0117 | Web Server Monitor. | 85 |  |
| 09-0004 | [1/3 - anomaly detection] [1/2 - KNN classification] Batch u | 85 |  |
| 09-0009 | Clockify Backup Template | 85 |  |
| 08-0038 | AutoClip – Automatically Generate Video Clips and Upload to  | 85 |  |
| 08-0044 | Flux Dev Image Generation Fal.ai | 85 |  |
| 08-0046 | Hacker News to Video Template - AlexK1919 | 85 |  |
| 08-0049 | HR-focused automation pipeline with AI | 85 |  |
| 08-0050 | Line Save File to Google Drive and Log File's URL | 85 |  |
| 08-0053 | OCR receipts from Google Drive | 85 |  |
| 08-0057 | RAG Workflow For Stock Earnings Report Analysis | 85 |  |
| 08-0063 | Tiktok Downloader | 85 |  |
| 08-0068 | 🤖🧠 AI Agent Chatbot + LONG TERM Memory + Note Storage + Tele | 85 |  |
| 08-0070 | 🦙👁️👁️ Find the Best Local Ollama Vision Models by Comparison | 85 |  |
| 05-0003 | OpenAI Personal Shopper with RAG and WooCommerce | 85 |  |
| 03-0008 | Effortless Email Management with AI | 85 |  |
| 03-0009 | Gumroad sale trigger | 85 |  |
| 12-0016 | Notion to Linkedin | 85 |  |
| 12-0020 | Phishing_analysis__URLScan_io_and_Virustotal_ | 85 |  |
| 04-0002 | Lead Qualification with BatchData | 85 |  |
| 15-0006 | Google analytics template | 85 |  |
| 15-0007 | Google analytics template | 85 |  |
| 15-0009 | SERPBear analytics template | 85 |  |
| 15-0010 | UTM Link Creator & QR Code Generator with Scheduled Google A | 85 |  |
| 01-0551 | AI Agent to chat with you Search Console Data, using OpenAI  | 80 |  |
| 01-0553 | AI CV Screening Workflow | 80 | no sticky-note documentation |
| 01-0592 | Dynamically generate HTML page from user request using OpenA | 80 |  |
| 01-0597 | Extract personal data with a self-hosted LLM Mistral NeMo | 80 |  |
| 01-0644 | Intelligent Web Query and Semantic Re-Ranking Flow | 80 |  |
| 01-0648 | LINE Assistant with Google Calendar and Gmail Integration | 80 | no sticky-note documentation |
| 01-0662 | Open Deep Research - AI-Powered Autonomous Research Workflow | 80 |  |
| 01-0667 | OpenAI Assistant for Hubspot Chat | 80 |  |
| 01-0671 | OpenAI-model-examples | 80 | legacy nodes: readbinaryfiles |
| 01-0691 | Spot Workplace Discrimination Patterns with AI | 80 |  |
| 01-0700 | Voice RAG Chatbot with ElevenLabs and OpenAI | 80 |  |
| 01-0706 | 🐋DeepSeek V3 Chat & R1 Reasoning Quick Start | 80 |  |
| 01-0712 | 🔥📈🤖 AI Agent for n8n Creators Leaderboard - Find Popular Wor | 80 |  |
| 13-0059 | Email Summary Agent | 80 |  |
| 13-0068 | Notify_user_in_Slack_of_quarantined_email_and_create_Jira_ti | 80 |  |
| 13-0071 | Real Estate Market Scanning | 80 |  |
| 13-0079 | Template - SSL Expiry Alert System | 80 |  |
| 06-0033 | GROQ LLAVA V1.5 7B | 80 |  |
| 06-0036 | MAIA - Health Check | 80 |  |
| 06-0037 | NeurochainAI Basic API Integration | 80 |  |
| 06-0043 | Play with Spotify from Telegram | 80 |  |
| 06-0051 | Translate Telegram audio messages with AI (55 supported lang | 80 |  |
| 06-0055 | 🤖 Telegram Messaging Agent for Text/Audio/Images | 80 |  |
| 07-0127 | AI Logo Sheet Extractor to Airtable | 80 |  |
| 07-0134 | Amazon keywords | 80 |  |
| 07-0139 | Automating Betting Data Retrieval with TheOddsAPI and Airtab | 80 |  |
| 07-0143 | Chat with Postgresql Database | 80 |  |
| 07-0145 | Connect Airtable Contacts to telli for Automated AI Voice Ca | 80 |  |
| 07-0147 | Convert image from jpg/png to webp | 80 |  |
| 07-0148 | Convert Squarespace Profiles to Shopify Customers in Google  | 80 |  |
| 07-0155 | Find Top Keywords | 80 |  |
| 07-0157 | Generate Leads with Google Maps - AlexK1919 | 80 |  |
| 07-0158 | Generate New Keywords with Search Volumes⚒️⚒️🟢🟢 | 80 |  |
| 07-0182 | HN Who is Hiring Scrape | 80 |  |
| 07-0184 | Import multiple Manufacturers from Google Sheets to Shopware | 80 |  |
| 07-0189 | Linkedin to Airtable | 80 |  |
| 07-0190 | Live link checker | 80 |  |
| 07-0194 | Matomo Analytics Report | 80 |  |
| 07-0202 | Printify Automation - Update Title and Description - AlexK19 | 80 |  |
| 07-0204 | ProspectLens company research | 80 |  |
| 07-0207 | Scrape Trustpilot Reviews to Google Sheets | 80 |  |
| 07-0209 | Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment w | 80 |  |
| 07-0210 | Search LinkedIn companies and add them to Airtable CRM | 80 |  |
| 07-0214 | Suspicious_login_detection | 80 |  |
| 07-0215 | Sync Youtube Video Urls with Google Sheets | 80 |  |
| 07-0217 | Testing Mulitple Local LLM with LM Studio | 80 |  |
| 07-0222 | Umami analytics template | 80 |  |
| 07-0223 | Umami analytics template | 80 |  |
| 07-0225 | Vision-Based AI Agent Scraper - with Google Sheets, Scraping | 80 |  |
| 09-0018 | [1/3 - anomaly detection] [1/2 - KNN classification] Batch u | 80 |  |
| 09-0019 | [1/3 - anomaly detection] [1/2 - KNN classification] Batch u | 80 |  |
| 09-0020 | [n8n] Advanced URL Parsing and Shortening Workflow - Switchy | 80 |  |
| 09-0022 | Backup Squarespace code Injections to Github | 80 |  |
| 09-0027 | Load Prompts from Github Repo and auto populate n8n expressi | 80 |  |
| 09-0028 | n8n Subworkflow Dependency Graph & Auto-Tagging | 80 |  |
| 09-0029 | Remote IOT Sensor monitoring via MQTT and InfluxDB | 80 |  |
| 09-0030 | Restore your credentials from GitHub | 80 |  |
| 08-0078 | Flux Dev Image Generation Fal.ai | 80 |  |
| 08-0079 | Flux Dev Image Generation Fal.ai | 80 |  |
| 08-0088 | n8n workflow deployer | 80 |  |
| 08-0089 | Optimise images uploaded to GDrive | 80 |  |
| 08-0092 | Remove Advanced Background from Google Drive Images | 80 |  |
| 10-0003 | BambooHR AI-Powered Company Policies and Benefits Chatbot | 80 |  |
| 03-0015 | AI Email processing autoresponder with approval (Yes/No) | 80 |  |
| 03-0018 | Email AI Auto-responder. Summerize and send email | 80 |  |
| 03-0024 | INSEE Enrichment for Agile CRM | 80 |  |
| 03-0025 | Meeting booked - to newsletter and CRM | 80 |  |
| 03-0027 | piepdrive-test | 80 |  |
| 12-0030 | Analyze_Crowdstrike_Detections__search_for_IOCs_in_VirusTota | 80 | legacy nodes: itemlists |
| 12-0037 | Create_Unique_Jira_tickets_from_Splunk_alerts | 80 |  |
| 12-0041 | Hugging Face to Notion | 80 | no sticky-note documentation |
| 12-0046 | Linear Project Status and End Date to Productboard feature S | 80 |  |
| 12-0049 | Notion to Clockify Sync Template | 80 |  |
| 12-0055 | Track Working Time and Pauses | 80 |  |
| 15-0013 | SERPBear analytics template | 80 |  |
| 15-0014 | SERPBear analytics template | 80 |  |
| 14-0013 | 💡🌐 Essential Multipage Website Scraper with Jina.ai | 80 |  |
| 01-0714 | AI Email processing autoresponder with approval (Yes/No) | 75 | no trigger node |
| 01-0725 | Building RAG Chatbot for Movie Recommendations with Qdrant a | 75 |  |
| 01-0757 | Image-Based Data Extraction API using Gemini AI | 75 |  |
| 01-0776 | Text to Speech (OpenAI) | 75 | synthetic skeleton (generic structure, no integration) |
| 01-0777 | Text to Speech (OpenAI) | 75 | synthetic skeleton (generic structure, no integration) |
| 13-0082 | Daylight Saving Time Notification | 75 |  |
| 13-0087 | Get PDF with JSReport | 75 |  |
| 13-0113 | Receive_and_analyze_emails_with_rules_in_Sublime_Security | 75 | legacy nodes: movebinarydata |
| 02-0038 | Complete Youtube | 75 |  |
| 02-0047 | Post New YouTube Videos to X | 75 |  |
| 06-0065 | NeurochainAI Basic API Integration | 75 |  |
| 06-0066 | NeurochainAI Basic API Integration | 75 |  |
| 06-0076 | Telegram RAG pdf | 75 |  |
| 07-0231 | 2. Refresh Pipedrive tokens | 75 |  |
| 07-0234 | AI Social Media Caption Creator | 75 |  |
| 07-0251 | Airtable markdown to html | 75 |  |
| 07-0252 | Amazon Product Price Tracker | 75 |  |
| 07-0253 | Automate Drive-To-Store Lead Generation System (with coupon) | 75 |  |
| 07-0254 | Automated Daily Weather Data Fetcher and Storage | 75 |  |
| 07-0263 | Entra Contacts to Zammad User Sync | 75 |  |
| 07-0264 | Entra User to Zammad User Sync | 75 |  |
| 07-0266 | Extract Business Leads from Google Maps with Dumpling AI to  | 75 |  |
| 07-0268 | Extract spend details (template) | 75 | hardcoded secret redacted: literal_password |
| 07-0269 | Fetch Squarespace Blog & Event Collections to Google Sheets | 75 |  |
| 07-0271 | Get all orders in Squarespace to Google Sheets | 75 |  |
| 07-0293 | Google Maps Email Scraper Template | 75 | legacy nodes: executeworkflow |
| 07-0326 | Import CSV from URL to GoogleSheet | 75 | legacy nodes: spreadsheetfile |
| 07-0328 | Linkedin Chrome Extensions | 75 |  |
| 07-0330 | Log errors and avoid sending too many emails | 75 | legacy nodes: executeworkflow |
| 07-0331 | Luma AI - Webhook Response v1 - AK | 75 |  |
| 07-0332 | Luma AI Dream Machine - Simple v1 - AK | 75 |  |
| 07-0334 | modelo do chatbot | 75 |  |
| 07-0337 | MongoDB Agent | 75 |  |
| 07-0354 | TEMPLATE - Multi Methods API Endpoint | 75 |  |
| 07-0356 | Unique QRcode coupon assignment and validation for Lead Gene | 75 |  |
| 07-0359 | Weekly_Shodan_Query___Report_Accidents__no_function_node_ | 75 | legacy nodes: itemlists |
| 07-0361 | Youtube Searcher | 75 |  |
| 07-0362 | YT AI News Playlist Creator/AI News Form Updater | 75 | hardcoded secret redacted: google_api_key |
| 09-0041 | Perform a domain search (single) with Icypeas | 75 | synthetic skeleton (generic structure, no integration) |
| 09-0042 | Restore your workflows from GitHub | 75 |  |
| 08-0104 | Automated PDF to HTML Conversion | 75 |  |
| 08-0142 | Scans von PDF zu Nextcloud | 75 |  |
| 05-0009 | [n8n] - Shopify Orders to D365 Business Central Sales Orders | 75 |  |
| 03-0035 | Email verification with Icypeas (single) | 75 | synthetic skeleton (generic structure, no integration) |
| 03-0049 | Perform an email search with Icypeas (single) | 75 | synthetic skeleton (generic structure, no integration) |
| 03-0050 | Property Lead Contact Enrichment from CRM | 75 | legacy nodes: spreadsheetfile |
| 03-0054 | Summarize emails with A.I. then send to messenger | 75 |  |
| 12-0097 | Realtime Notion Todoist 2-way Sync Template | 75 | legacy nodes: executeworkflow |
| 16-0004 | [2/2] KNN classifier (lands dataset) | 75 |  |
| 16-0006 | [2/3] Set up medoids (2 types) for anomaly detection (crops  | 75 |  |
| 16-0007 | [3/3] Anomaly detection tool (crops dataset) | 75 |  |
| 16-0011 | FLUX-fill standalone | 75 |  |
| 01-0791 | AI Agent to chat with you Search Console Data, using OpenAI  | 70 |  |
| 01-0809 | Docsify example | 70 |  |
| 01-0817 | Dynamically generate HTML page from user request using OpenA | 70 |  |
| 01-0838 | Extract personal data with a self-hosted LLM Mistral NeMo | 70 | nodes are not connected |
| 01-0841 | Generate Graphic Wallpaper with Midjourney, GPT-4o-mini and  | 70 |  |
| 01-0857 | Line Chatbot Handling AI Responses with Groq and Llama3 | 70 |  |
| 01-0861 | Make OpenAI Citation for File Retrieval RAG | 70 |  |
| 01-0892 | Text to Speech (OpenAI) | 70 | synthetic skeleton (generic structure, no integration) |
| 01-0893 | Text to Speech (OpenAI) | 70 | synthetic skeleton (generic structure, no integration) |
| 01-0895 | Transform Image to Lego Style Using Line and Dall-E | 70 | no sticky-note documentation |
| 01-0901 | 🎥 Gemini AI Video Analysis | 70 |  |
| 01-0903 | 🔥📈🤖 AI Agent for n8n Creators Leaderboard - Find Popular Wor | 70 |  |
| 13-0129 | AI CV Screening Workflow | 70 | no sticky-note documentation |
| 13-0138 | Discord AI bot | 70 | no sticky-note documentation |
| 13-0163 | line message api demo | 70 |  |
| 13-0167 | Monitor USDT ERC-20 Wallet Balance with Etherscan and Telegr | 70 | legacy nodes: cron |
| 13-0189 | Telegram channel to Readeck & Hoarder | 70 |  |
| 02-0058 | Fully automated Video Captions generation with json2video | 70 |  |
| 02-0059 | Generate 360° Virtual Try-on Videos for Clothing with Kling  | 70 |  |
| 02-0064 | Publish Image Post to Bluesky | 70 |  |
| 02-0067 | Turn YouTube Videos into Summaries, Transcripts, and Visual  | 70 |  |
| 02-0071 | Use XMLRPC via HttpRequest-node to post on Wordpress.com | 70 |  |
| 07-0452 | Lead Generation System (Template) | 70 |  |
| 07-0461 | New Ticket Alerts to Teams | 70 | no sticky-note documentation |
| 07-0474 | Selenium Ultimate Scraper Workflow | 70 |  |
| 07-0484 | 💥workflow n8n d'Auto-Post sur les réseaux sociaux - vide | 70 |  |
| 09-0048 | Backup workflows to git repository on Gitea | 70 |  |
| 09-0049 | Clone n8n Workflows between Instances using n8n API | 70 |  |
| 09-0051 | Docsify example | 70 |  |
| 09-0068 | Perform a domain search (single) with Icypeas | 70 | synthetic skeleton (generic structure, no integration) |
| 09-0073 | Retry Execution Hourly | 70 |  |
| 08-0153 | Basic PDF Digital Sign Service | 70 |  |
| 08-0158 | Credentials Transfer | 70 |  |
| 08-0197 | On-Demand Automation Template | 70 | generic name (display name auto-generated, review it); synthetic skeleton (generic structure, no integration) |
| 08-0198 | On-Demand Automation Template | 70 | generic name (display name auto-generated, review it); synthetic skeleton (generic structure, no integration) |
| 08-0199 | On-Demand Automation Template | 70 | generic name (display name auto-generated, review it); synthetic skeleton (generic structure, no integration) |
| 08-0214 | Workflow Importer | 70 |  |
| 10-0005 | Create Threads on Bluesky | 70 |  |
| 03-0064 | Email verification with Icypeas (single) | 70 | synthetic skeleton (generic structure, no integration) |
| 03-0078 | Perform an email search with Icypeas (single) | 70 | synthetic skeleton (generic structure, no integration) |
| 03-0081 | Shopify + Mautic | 70 | hardcoded secret redacted: literal_secret |
| 03-0083 | Very simple Human in the loop system email with AI e IMAP | 70 |  |
| 03-0084 | xSend and check TTS (Text-to-speech) voice calls end email v | 70 |  |
| 12-0116 | LINE Assistant with Google Calendar and Gmail Integration | 70 | no sticky-note documentation |
| 16-0023 | [2/2] KNN classifier (lands dataset) | 70 |  |
| 16-0024 | [2/2] KNN classifier (lands dataset) | 70 |  |
| 16-0025 | [2/3] Set up medoids (2 types) for anomaly detection (crops  | 70 |  |
| 16-0026 | [2/3] Set up medoids (2 types) for anomaly detection (crops  | 70 |  |
| 16-0027 | [3/3] Anomaly detection tool (crops dataset) | 70 |  |
| 16-0028 | [3/3] Anomaly detection tool (crops dataset) | 70 |  |
| 16-0036 | dub.co URL Shortener | 70 |  |
| 16-0037 | FLUX-fill standalone | 70 |  |
| 16-0038 | FLUX-fill standalone | 70 |  |
| 16-0042 | Google Site Index - sitemap.xml example | 70 |  |
| 16-0051 | Read sitemap and filter URLs | 70 |  |
| 16-0054 | 🐋DeepSeek V3 Chat & R1 Reasoning Quick Start | 70 |  |
| 14-0025 | Extract And Decode Google News RSS URLs to Clean Article Lin | 70 |  |
| 14-0026 | get_a_web_page | 70 | synthetic skeleton (generic structure, no integration) |
| 14-0027 | get_a_web_page | 70 | synthetic skeleton (generic structure, no integration) |
| 14-0035 | Intelligent Web Query and Semantic Re-Ranking Flow | 70 |  |
| 14-0037 | Open Deep Research - AI-Powered Autonomous Research Workflow | 70 |  |
| 01-0906 | Bilig WorkPaper MCP formula engine for n8n agents | 65 | synthetic skeleton (generic structure, no integration) |
| 01-0925 | New OpenAI Image Generation | 65 |  |
| 01-0940 | Simple OpenAI Image Generator | 65 |  |
| 01-0943 | Very simple Human in the loop system email with AI e IMAP | 65 | no trigger node |
| 13-0193 | [hiroshidigital.com] Send Message In Larksuite | 65 |  |
| 13-0233 | Weather via Slack | 65 | no sticky-note documentation |
| 02-0090 | upload-post images | 65 |  |
| 07-0493 | Automated Content SEO Audit Report | 65 |  |

## Sellable workflows with structural near-duplicates (consider merging/renaming): 1235

- 01-0005 AI-Generated Summary Block for WordPress Posts - with OpenAI, WordPres (+1 similar)
- 01-0007 AI-Powered Information Monitoring with OpenAI, Google Sheets, Jina AI  (+1 similar)
- 01-0011 Automate Pinterest Analysis & AI-Powered Content Suggestions With Pint (+1 similar)
- 01-0013 Automated Resume Review System Using OpenAI + Google Sheets (+2 similar)
- 01-0018 Effortless Email Management with AI (+1 similar)
- 01-0025 Hacker News to Video Template - AlexK1919 (+1 similar)
- 01-0029 HR-focused automation pipeline with AI (+2 similar)
- 01-0032 mails2notion V2 (+1 similar)
- 01-0034 Microsoft Outlook AI Email Assistant (+1 similar)
- 01-0038 OpenAI Assistant for Hubspot Chat (+1 similar)
- 01-0040 OpenAI Personal Shopper with RAG and WooCommerce (+1 similar)
- 01-0049 RAG Workflow For Stock Earnings Report Analysis (+1 similar)
- 01-0053 Scrape Trustpilot Reviews with DeepSeek, Analyze Sentiment with OpenAI (+1 similar)
- 01-0056 Spot Workplace Discrimination Patterns with AI (+1 similar)
- 01-0061 Telegram-bot AI Da Nang (+1 similar)
- 01-0065 Translate Telegram audio messages with AI (55 supported languages) v1 (+1 similar)
- 01-0068 UTM Link Creator & QR Code Generator with Scheduled Google Analytics R (+1 similar)
- 01-0070 Voice RAG Chatbot with ElevenLabs and OpenAI (+1 similar)
- 01-0081 🤖🧠 AI Agent Chatbot + LONG TERM Memory + Note Storage + Telegram (+1 similar)
- 01-0102 Ask a human (+1 similar)
- 01-0121 Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI (+1 similar)
- 01-0124 Calendar_scheduling (+1 similar)
- 01-0130 Chat with Postgresql Database (+1 similar)
- 01-0180 Fine-tuning with OpenAI models (+1 similar)
- 01-0202 HN Who is Hiring Scrape (+1 similar)
- 01-0222 LeadPilot Lite — Manual Lead Email Writer (+1 similar)
- 01-0226 Load Prompts from Github Repo and auto populate n8n expressions (+1 similar)
- 01-0235 Make OpenAI Citation for File Retrieval RAG (+1 similar)
- 01-0240 modelo do chatbot (+1 similar)
- 01-0250 News Extraction (+3 similar)
- 01-0257 OpenAI Assistant workflow: uploa file, create an Assistant, chat with  (+1 similar)
- 01-0268 Podcast Digest (+1 similar)
- 01-0319 SupportFlow Lite — Simple AI Support Bot (No RAG) (+1 similar)
- 01-0321 Telegram RAG pdf (+1 similar)
- 01-0325 Testing Mulitple Local LLM with LM Studio (+1 similar)
- 01-0352 Vision-Based AI Agent Scraper - with Google Sheets, ScrapingBee, and G (+1 similar)
- 01-0360 Whisper Transkription copy (+1 similar)
- 01-0383 AI Social Media Caption Creator (+1 similar)
- 01-0385 Airtable + Gmail + Google Calendar Event-Triggered AI Agent (+1 similar)
- 01-0386 Airtable + Gmail + Google Calendar Event-Triggered AI Agent (+1 similar)
- 01-0387 Airtable + Gmail + Informationextractor Scheduled AI Agent (+1 similar)
- 01-0388 Airtable + Gmail + Informationextractor Scheduled AI Agent (+1 similar)
- 01-0389 Airtable + Graphql + Informationextractor Event-Triggered AI Agent (+1 similar)
- 01-0390 Airtable + Graphql + Informationextractor Event-Triggered AI Agent (+1 similar)
- 01-0392 Airtable + Textclassifier Event-Triggered AI Agent (+1 similar)
- 01-0393 Airtable + Textclassifier Event-Triggered AI Agent (+1 similar)
- 01-0394 Airtable + Twilio Event-Triggered AI Agent (+1 similar)
- 01-0395 Airtable + Twilio Event-Triggered AI Agent (+1 similar)
- 01-0403 BambooHR AI-Powered Company Policies and Benefits Chatbot (+1 similar)
- 01-0404 Bannerbear + Discord + OpenAI Event-Triggered AI Agent (+1 similar)
- 01-0405 Bannerbear + Discord + OpenAI Event-Triggered AI Agent (+1 similar)
- 01-0411 Clearbit + Gmail + Google Calendar Scheduled AI Agent (+1 similar)
- 01-0413 Complete Youtube (+1 similar)
- 01-0414 Compression + Documentdefaultdataloader + Textsplitterrecursivecharact (+1 similar)
- 01-0415 Compression + Documentdefaultdataloader + Textsplitterrecursivecharact (+1 similar)
- 01-0416 Compression + Google Drive + Informationextractor On-Demand AI Agent (+1 similar)
- 01-0417 Compression + Google Drive + Informationextractor On-Demand AI Agent (+1 similar)
- 01-0423 Documentdefaultdataloader + Google Drive + OpenAI On-Demand AI Agent (+1 similar)
- 01-0424 Documentdefaultdataloader + Google Drive + OpenAI On-Demand AI Agent (+1 similar)
- 01-0430 Documentdefaultdataloader + Google Drive + Textsplittertokensplitter E (+1 similar)
- 01-0431 Documentdefaultdataloader + Google Drive + Textsplittertokensplitter E (+1 similar)
- 01-0433 Documentdefaultdataloader + Retrievervectorstore + Textsplitterrecursi (+1 similar)
- 01-0434 Documentdefaultdataloader + Retrievervectorstore + Textsplitterrecursi (+1 similar)
- 01-0435 Documentdefaultdataloader + Retrievervectorstore + Textsplitterrecursi (+1 similar)
- 01-0436 Documentdefaultdataloader + Retrievervectorstore + Textsplitterrecursi (+1 similar)
- 01-0438 Documentdefaultdataloader + Supabase + Textsplitterrecursivecharactert (+1 similar)
- 01-0439 Documentdefaultdataloader + Supabase + Textsplitterrecursivecharactert (+1 similar)
- 01-0442 Email AI Auto-responder. Summerize and send email (+1 similar)
- 01-0448 Extract spend details (template) (+1 similar)
- 01-0451 Fine-tuning with OpenAI models (+1 similar)
- 01-0458 Gmail + Google Docs + OpenAI Event-Triggered AI Agent (+1 similar)
- 01-0459 Gmail + Google Docs + OpenAI Event-Triggered AI Agent (+1 similar)
- 01-0460 Gmail + Google Sheets + Lmopenai Event-Triggered AI Agent (+1 similar)
- 01-0461 Gmail + Google Sheets + Lmopenai Event-Triggered AI Agent (+1 similar)
- 01-0472 Gmail + OpenAI Scheduled AI Agent (+3 similar)
- 01-0473 Gmail + OpenAI Scheduled AI Agent (+3 similar)
- 01-0474 Gmail + Strava + WhatsApp Event-Triggered AI Agent (+1 similar)
- 01-0475 Gmail + Strava + WhatsApp Event-Triggered AI Agent (+1 similar)
- 01-0478 Google Calendar + Google Drive On-Demand AI Agent (+1 similar)
- 01-0479 Google Calendar + Google Drive On-Demand AI Agent (+1 similar)
- 01-0482 Google Drive + Google Sheets + Linear Scheduled AI Agent (+1 similar)
- 01-0483 Google Drive + Google Sheets + Linear Scheduled AI Agent (+1 similar)
- 01-0486 Google Drive + OpenAI On-Demand AI Agent (+1 similar)
- 01-0487 Google Drive + OpenAI On-Demand AI Agent (+1 similar)
- 01-0492 Google Sheets + OpenAI Event-Triggered AI Agent (+1 similar)
- 01-0493 Google Sheets + OpenAI Event-Triggered AI Agent (+1 similar)
- 01-0498 Image Generation API (+2 similar)
- 01-0500 Informationextractor + WordPress On-Demand AI Agent (+1 similar)
- 01-0501 Informationextractor + WordPress On-Demand AI Agent (+1 similar)
- 01-0503 Lemlist + Slack Event-Triggered AI Agent (+1 similar)
- 01-0504 Lemlist + Slack Event-Triggered AI Agent (+1 similar)
- 01-0505 Linear + Slack Scheduled AI Agent (+1 similar)
- 01-0506 Linear + Slack Scheduled AI Agent (+1 similar)
- 01-0508 MongoDB Agent (+1 similar)
- 01-0512 Notion + Textclassifier Event-Triggered AI Agent (+1 similar)
- 01-0513 Notion + Textclassifier Event-Triggered AI Agent (+1 similar)
- 01-0515 OpenAI + Reddit On-Demand AI Agent (+1 similar)
- 01-0516 OpenAI + Reddit On-Demand AI Agent (+1 similar)
- 01-0521 OpenAI + Twitter Scheduled AI Agent (+1 similar)
- 01-0522 OpenAI + Twitter Scheduled AI Agent (+1 similar)
- 01-0526 OpenAI-model-examples (+3 similar)
- 01-0528 RAG & GenAI App With WordPress Content (+1 similar)
- 01-0530 Redis + Twilio Event-Triggered AI Agent (+1 similar)
- 01-0531 Redis + Twilio Event-Triggered AI Agent (+1 similar)
- 01-0533 Selenium Ultimate Scraper Workflow (+1 similar)
- 01-0543 🐋🤖 DeepSeek AI Agent + Telegram + LONG TERM Memory 🧠 (+1 similar)
- 01-0545 🤖🧑‍💻 AI Agent for Top n8n Creators Leaderboard Reporting (+1 similar)
- 01-0547 [AI/LangChain] Output Parser 4 (+2 similar)
- 01-0552 AI Agent to chat with you Search Console Data, using OpenAI and Postgr (+1 similar)
- 01-0554 AI CV Screening Workflow (+1 similar)
- 01-0558 Airtable Event-Triggered AI Agent (+1 similar)
- 01-0559 Airtable Event-Triggered AI Agent (+1 similar)
- 01-0560 Airtable Event-Triggered AI Agent (+1 similar)
- 01-0561 Airtable Event-Triggered AI Agent (+1 similar)
- 01-0562 Baserow + Gmail + Google Calendar Event-Triggered AI Agent (+1 similar)
- 01-0563 Baserow + Gmail + Google Calendar Event-Triggered AI Agent (+1 similar)
- 01-0566 chrome extension backend with AI (+2 similar)
- 01-0567 Clearbit + Gmail + Google Calendar Scheduled AI Agent (+1 similar)
- 01-0572 CoinMarketCap_Exchange_and_Community_Agent_Tool (+1 similar)
- 01-0573 CoinMarketCap_Exchange_and_Community_Agent_Tool (+1 similar)
- 01-0577 Discord + Informationextractor + OpenAI Scheduled AI Agent (+1 similar)
- 01-0578 Discord + Informationextractor + OpenAI Scheduled AI Agent (+1 similar)
- 01-0580 Documentdefaultdataloader + Google Sheets + Informationextractor On-De (+1 similar)
- 01-0581 Documentdefaultdataloader + Google Sheets + Informationextractor On-De (+1 similar)
- 01-0582 Documentdefaultdataloader + Google Sheets + Informationextractor On-De (+1 similar)
- 01-0583 Documentdefaultdataloader + Google Sheets + Informationextractor On-De (+1 similar)
- 01-0587 Documentjsoninputloader + Gmail + Textsplitterrecursivecharactertextsp (+1 similar)
- 01-0591 Dynamically generate HTML page from user request using OpenAI Structur (+1 similar)
- 01-0596 Extract personal data with a self-hosted LLM Mistral NeMo (+1 similar)
- 01-0598 Generate audio from text using OpenAI - text-to-speech Workflow (+2 similar)
- 01-0601 Gmail + Google Calendar Event-Triggered AI Agent (+1 similar)
- 01-0604 Gmail + OpenAI Scheduled AI Agent (+3 similar)
- 01-0605 Gmail + OpenAI Scheduled AI Agent (+3 similar)
- 01-0607 Gmail Event-Triggered AI Agent (+1 similar)
- 01-0608 Gmail Event-Triggered AI Agent (+1 similar)
- 01-0612 Google Drive On-Demand AI Agent (+1 similar)
- 01-0613 Google Drive On-Demand AI Agent (+1 similar)
- 01-0615 Google Sheets + Informationextractor On-Demand AI Agent (+1 similar)
- 01-0616 Google Sheets + Informationextractor On-Demand AI Agent (+1 similar)
- 01-0617 Google Sheets + OpenAI Event-Triggered AI Agent (+1 similar)
- 01-0618 Google Sheets + OpenAI Event-Triggered AI Agent (+1 similar)
- 01-0623 Google Sheets Event-Triggered AI Agent (+1 similar)
- 01-0625 Google Sheets Event-Triggered AI Agent (+1 similar)
- 01-0627 Google Sheets Event-Triggered AI Agent (+1 similar)
- 01-0628 Google Sheets Event-Triggered AI Agent (+1 similar)
- 01-0629 Google Sheets Scheduled AI Agent (+1 similar)
- 01-0630 Google Sheets Scheduled AI Agent (+1 similar)
- 01-0636 Image-Based Data Extraction API using Gemini AI (+1 similar)
- 01-0637 Informationextractor + Textclassifier Event-Triggered AI Agent (+1 similar)
- 01-0638 Informationextractor + Textclassifier Event-Triggered AI Agent (+1 similar)