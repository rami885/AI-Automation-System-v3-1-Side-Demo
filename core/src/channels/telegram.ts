/**
 * Telegram channel adapter (Step A5) — TEST MODE ONLY.
 * It normalizes a Telegram update into a CanonicalRequest and renders replies
 * as strings. It performs NO live sending and holds NO bot token. Wiring to the
 * real Bot API happens only in Phase B, behind a gate.
 *
 * Telegram is NOT a privileged backdoor: the sender is resolved through the
 * IdentityDirectory just like any other channel.
 */

import { randomUUID } from "node:crypto";
import type { CanonicalRequest, Intent } from "../schema/canonical.js";
import type { HandleResult } from "../core/operation-room.js";
import type { ChannelAdapter } from "./adapter.js";
import type { IdentityDirectory } from "../auth/identity-directory.js";

/** Minimal slice of a Telegram update we rely on. */
export interface TelegramUpdate {
  update_id: number;
  message: {
    message_id: number;
    from: { id: number };
    chat: { id: number };
    text: string;
    date: number;
  };
}

/** Map a leading command/keyword to an intent. Defaults to "read". */
function intentFromText(text: string): Intent {
  const t = text.trim().toLowerCase();
  if (t.startsWith("/brief") || t.startsWith("/report")) return "report";
  if (t.startsWith("/review")) return "review";
  if (t.startsWith("/run") || t.startsWith("/execute")) return "execute";
  return "read";
}

export class TelegramAdapter implements ChannelAdapter<TelegramUpdate> {
  readonly type = "telegram" as const;

  constructor(private readonly directory: IdentityDirectory) {}

  toCanonical(raw: TelegramUpdate): CanonicalRequest {
    const senderId = String(raw.message.from.id);
    // Resolve (and authenticate) the sender — throws if unknown.
    const identity = this.directory.resolve("telegram", senderId);

    return {
      requestId: randomUUID(),
      identity,
      channel: { type: "telegram", exposure: "private" },
      intent: intentFromText(raw.message.text),
      payload: { text: raw.message.text },
      timestamp: new Date(raw.message.date * 1000).toISOString(),
    };
  }

  render(result: HandleResult): string {
    const { decision, output } = result;
    switch (decision.decision) {
      case "allow":
        return typeof output === "string"
          ? output
          : JSON.stringify(output, null, 2);
      case "escalate":
        return `🔐 هذا الطلب يحتاج موافقتك (تصعيد): ${decision.reason}`;
      case "deny":
        return `⛔ مرفوض: ${decision.reason}`;
    }
  }
}
