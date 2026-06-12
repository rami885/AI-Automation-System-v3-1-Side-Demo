import { test } from "node:test";
import assert from "node:assert/strict";
import { decide, type Resource } from "../src/policy/policy-engine.js";
import type { CanonicalRequest } from "../src/schema/canonical.js";
import type { Role } from "../src/policy/classification.js";
import type { ChannelExposureType, ChannelType } from "../src/schema/canonical.js";
import type { DataClassification } from "../src/policy/classification.js";

const TENANT = "tenant-0-drfone";

function req(
  role: Role,
  channelType: ChannelType,
  exposure: ChannelExposureType,
  tenantId = TENANT,
): CanonicalRequest {
  return {
    requestId: "r1",
    identity: { userId: "u1", tenantId, role },
    channel: { type: channelType, exposure },
    intent: "read",
    payload: { text: "hi" },
    timestamp: new Date().toISOString(),
  };
}

function res(classification: DataClassification, tenantId = TENANT): Resource {
  return { name: "res", tenantId, classification };
}

test("cross-tenant access is always denied", () => {
  const d = decide(req("owner", "telegram", "private"), res("public", "other-tenant"));
  assert.equal(d.decision, "deny");
  assert.match(d.reason, /cross-tenant/);
});

test("owner on private channel may access private data", () => {
  assert.equal(decide(req("owner", "telegram", "private"), res("private")).decision, "allow");
});

test("public client channel cannot see internal data", () => {
  assert.equal(decide(req("client", "web", "public"), res("internal")).decision, "deny");
});

test("public client channel can see public data", () => {
  assert.equal(decide(req("client", "web", "public"), res("public")).decision, "allow");
});

test("employee on internal channel sees internal but not confidential", () => {
  assert.equal(decide(req("employee", "web", "internal"), res("internal")).decision, "allow");
  assert.equal(decide(req("employee", "web", "internal"), res("confidential")).decision, "escalate");
});

test("employee asking finance/private data is escalated, not silently denied", () => {
  const d = decide(req("employee", "web", "internal"), res("private"));
  assert.equal(d.decision, "escalate");
  assert.match(d.reason, /owner approval/);
});

test("owner on a public channel asking confidential is escalated", () => {
  assert.equal(decide(req("owner", "web", "public"), res("confidential")).decision, "escalate");
});
