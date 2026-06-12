import { test } from "node:test";
import assert from "node:assert/strict";
import { KnowledgeBase, type OpsItem } from "../src/knowledge/knowledge-base.js";
import { generateDailyBrief } from "../src/pilots/daily-brief.js";
import { buildApp } from "../src/app/build-app.js";

const TENANT = "tenant-0-drfone";

const items: OpsItem[] = [
  { id: "1", tenantId: TENANT, title: "late high", status: "late", priority: "high", needsOwnerDecision: false },
  { id: "2", tenantId: TENANT, title: "needs decision", status: "open", priority: "high", needsOwnerDecision: true },
  { id: "3", tenantId: TENANT, title: "done item", status: "done", priority: "low", needsOwnerDecision: false },
  { id: "4", tenantId: "other-tenant", title: "foreign", status: "late", priority: "high", needsOwnerDecision: true },
];

test("brief is tenant-scoped and counts correctly", () => {
  const brief = generateDailyBrief(new KnowledgeBase(items), TENANT);
  assert.equal(brief.counts.total, 3); // the other-tenant item is excluded
  assert.equal(brief.counts.late, 1);
  assert.equal(brief.counts.done, 1);
  assert.equal(brief.late.length, 1);
  assert.equal(brief.needsDecision.length, 1);
  assert.equal(brief.highPriority.length, 2); // late high + open high (done excluded)
});

test("end-to-end: owner report request is allowed and returns a brief", () => {
  const app = buildApp(new KnowledgeBase(items));
  const result = app.room.handle({
    requestId: "r1",
    identity: { userId: "rami", tenantId: TENANT, role: "owner" },
    channel: { type: "telegram", exposure: "private" },
    intent: "report",
    payload: { text: "/brief" },
    timestamp: new Date().toISOString(),
  });
  assert.equal(result.decision.decision, "allow");
  assert.match(String(result.output), /التقرير اليومي/);
  assert.equal(app.audit.all().length, 1);
  assert.equal(app.audit.verify(), true);
});

test("end-to-end: public client cannot pull an internal report", () => {
  const app = buildApp(new KnowledgeBase(items));
  const result = app.room.handle({
    requestId: "r2",
    identity: { userId: "c", tenantId: TENANT, role: "client" },
    channel: { type: "web", exposure: "public" },
    intent: "report",
    payload: { text: "report please" },
    timestamp: new Date().toISOString(),
  });
  assert.equal(result.decision.decision, "deny");
  assert.equal(result.output, undefined);
});
