/**
 * Channel adapter contract. Every channel (Telegram, Web, PWA, future) implements
 * this: it turns its own raw input into a CanonicalRequest and renders a result
 * back into its own format. The core never sees channel-specific shapes.
 */

import type { CanonicalRequest, ChannelType } from "../schema/canonical.js";
import type { HandleResult } from "../core/operation-room.js";

export interface ChannelAdapter<Raw> {
  readonly type: ChannelType;
  /** Normalize raw, untrusted channel input into the canonical shape. */
  toCanonical(raw: Raw): CanonicalRequest;
  /** Render a core result into a message for this channel (no sending here). */
  render(result: HandleResult): string;
}
