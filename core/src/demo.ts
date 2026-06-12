/**
 * Local demo (no network). Run: `npm run demo`
 * Shows the channel-agnostic core end to end:
 *   1. Rami sends /brief on Telegram      -> allowed, brief generated
 *   2. An unknown Telegram user           -> authentication rejected
 *   3. A client on the public web channel -> denied (internal data)
 *   4. The audit chain is intact and records every decision.
 */

import { buildApp } from "./app/build-app.js";
import { KnowledgeBase, type OpsItem } from "./knowledge/knowledge-base.js";
import { IdentityDirectory } from "./auth/identity-directory.js";
import { TelegramAdapter, type TelegramUpdate } from "./channels/telegram.js";
import { AuthenticationError } from "./auth/identity-directory.js";
import { TENANT_DRFONE } from "./tenant/tenant.js";

const sampleOps: OpsItem[] = [
  { id: "1", tenantId: TENANT_DRFONE.tenantId, title: "تصليح iPhone 12 — بانتظار قطعة", status: "late", priority: "high", needsOwnerDecision: false },
  { id: "2", tenantId: TENANT_DRFONE.tenantId, title: "عرض سعر جملة لشركة — يحتاج موافقة", status: "open", priority: "high", needsOwnerDecision: true },
  { id: "3", tenantId: TENANT_DRFONE.tenantId, title: "تحديث صور 10 منتجات على الموقع", status: "in_progress", priority: "medium", needsOwnerDecision: false },
  { id: "4", tenantId: TENANT_DRFONE.tenantId, title: "رد على استفسار ضمان", status: "done", priority: "low", needsOwnerDecision: false },
];

const directory = new IdentityDirectory().register("telegram", "555001", {
  userId: "rami",
  tenantId: TENANT_DRFONE.tenantId,
  role: "owner",
});

const app = buildApp(new KnowledgeBase(sampleOps));
const telegram = new TelegramAdapter(directory);

function ramiBrief(): TelegramUpdate {
  return {
    update_id: 1,
    message: { message_id: 1, from: { id: 555001 }, chat: { id: 555001 }, text: "/brief", date: 1_760_000_000 },
  };
}

console.log("=== 1) رامي يطلب التقرير عبر Telegram ===");
const r1 = app.room.handle(telegram.toCanonical(ramiBrief()));
console.log(telegram.render(r1));

console.log("\n=== 2) مستخدم Telegram غير معروف ===");
try {
  telegram.toCanonical({ update_id: 2, message: { message_id: 2, from: { id: 999 }, chat: { id: 999 }, text: "/brief", date: 1_760_000_000 } });
} catch (e) {
  console.log(e instanceof AuthenticationError ? `⛔ ${e.message}` : String(e));
}

console.log("\n=== 3) عميل عبر الويب العام يطلب بيانات داخلية ===");
const r3 = app.room.handle({
  requestId: "web-1",
  identity: { userId: "client-x", tenantId: TENANT_DRFONE.tenantId, role: "client" },
  channel: { type: "web", exposure: "public" },
  intent: "report",
  payload: { text: "اعطني تقرير العمليات" },
  timestamp: new Date().toISOString(),
});
console.log(`القرار: ${r3.decision.decision} — ${r3.decision.reason}`);

console.log("\n=== 4) سجل التدقيق ===");
console.log(`عدد السجلات: ${app.audit.all().length} | السلسلة سليمة: ${app.audit.verify()}`);
for (const rec of app.audit.all()) {
  console.log(`  [${rec.decision}] ${rec.role}/${rec.channel} → ${rec.resource} (${rec.dataClassification})`);
}
