import { test } from "node:test";
import assert from "node:assert/strict";
import { AuditLog } from "../src/audit/audit.js";
import { OperationRoom } from "../src/core/operation-room.js";
import type { Resource } from "../src/policy/policy-engine.js";

function sample() {
  return {
    userId: "u1",
    tenantId: "tenant-0-drfone",
    role: "owner",
    channel: "telegram",
    action: "read",
    resource: "daily_brief",
    dataClassification: "internal" as const,
    decision: "allow" as const,
    decisionReason: "ok",
  };
}

test("chain verifies for an untouched log", () => {
  const log = new AuditLog();
  log.append(sample());
  log.append({ ...sample(), decision: "deny", decisionReason: "no" });
  assert.equal(log.verify(), true);
  assert.equal(log.all().length, 2);
});

test("tampering with a record breaks the chain", () => {
  const log = new AuditLog();
  log.append(sample());
  log.append(sample());
  // mutate a past record's content
  (log.all()[0] as { resource: string }).resource = "finance_report";
  assert.equal(log.verify(), false);
});

test("operation room validates, decides, and audits every request", () => {
  const resolve = (): Resource => ({
    name: "finance_report",
    tenantId: "tenant-0-drfone",
    classification: "private",
  });
  const room = new OperationRoom(resolve);

  // employee on internal channel asking private -> escalate, and it is audited
  const result = room.handle({
    requestId: "r1",
    identity: { userId: "emp", tenantId: "tenant-0-drfone", role: "employee" },
    channel: { type: "web", exposure: "internal" },
    intent: "read",
    payload: { text: "show finances" },
    timestamp: "2026-06-12T17:00:00Z",
  });

  assert.equal(result.decision.decision, "escalate");
  const records = room.auditLog().all();
  assert.equal(records.length, 1);
  assert.equal(records[0]?.decision, "escalate");
  assert.equal(room.auditLog().verify(), true);
});
