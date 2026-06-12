import { test } from "node:test";
import assert from "node:assert/strict";
import {
  validateCanonicalRequest,
  SchemaValidationError,
} from "../src/schema/canonical.js";

const valid = {
  requestId: "r1",
  identity: { userId: "u1", tenantId: "tenant-0-drfone", role: "owner" },
  channel: { type: "telegram", exposure: "private" },
  intent: "read",
  payload: { text: "daily brief" },
  timestamp: "2026-06-12T17:00:00Z",
};

test("accepts a well-formed request", () => {
  const r = validateCanonicalRequest(valid);
  assert.equal(r.identity.role, "owner");
  assert.equal(r.channel.type, "telegram");
});

test("rejects unknown role", () => {
  assert.throws(
    () => validateCanonicalRequest({ ...valid, identity: { ...valid.identity, role: "admin" } }),
    SchemaValidationError,
  );
});

test("rejects missing tenantId", () => {
  assert.throws(
    () => validateCanonicalRequest({ ...valid, identity: { userId: "u1", role: "owner" } }),
    SchemaValidationError,
  );
});

test("rejects bad channel exposure", () => {
  assert.throws(
    () => validateCanonicalRequest({ ...valid, channel: { type: "web", exposure: "open" } }),
    SchemaValidationError,
  );
});

test("rejects non-array attachments", () => {
  assert.throws(
    () => validateCanonicalRequest({ ...valid, payload: { text: "x", attachments: "nope" } }),
    SchemaValidationError,
  );
});

test("normalizes attachments to strings", () => {
  const r = validateCanonicalRequest({
    ...valid,
    payload: { text: "x", attachments: [1, "a"] },
  });
  assert.deepEqual(r.payload.attachments, ["1", "a"]);
});
