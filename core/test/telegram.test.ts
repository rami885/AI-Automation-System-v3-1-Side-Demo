import { test } from "node:test";
import assert from "node:assert/strict";
import { TelegramAdapter, type TelegramUpdate } from "../src/channels/telegram.js";
import { IdentityDirectory, AuthenticationError } from "../src/auth/identity-directory.js";

const TENANT = "tenant-0-drfone";

function dir() {
  return new IdentityDirectory().register("telegram", "555001", {
    userId: "rami",
    tenantId: TENANT,
    role: "owner",
  });
}

function update(fromId: number, text: string): TelegramUpdate {
  return {
    update_id: 1,
    message: { message_id: 1, from: { id: fromId }, chat: { id: fromId }, text, date: 1_760_000_000 },
  };
}

test("maps a known sender into a canonical request", () => {
  const req = new TelegramAdapter(dir()).toCanonical(update(555001, "/brief"));
  assert.equal(req.identity.role, "owner");
  assert.equal(req.identity.tenantId, TENANT);
  assert.equal(req.channel.type, "telegram");
  assert.equal(req.channel.exposure, "private");
  assert.equal(req.intent, "report");
});

test("defaults to read intent for plain text", () => {
  const req = new TelegramAdapter(dir()).toCanonical(update(555001, "كيف الحال"));
  assert.equal(req.intent, "read");
});

test("rejects an unknown sender (no backdoor)", () => {
  assert.throws(
    () => new TelegramAdapter(dir()).toCanonical(update(999, "/brief")),
    AuthenticationError,
  );
});
