/**
 * Identity directory (seam for Supabase Auth — §13).
 * Maps an external channel identifier (e.g. a Telegram user id) to a trusted
 * internal Identity. This is what stops a channel from being a backdoor:
 * even Telegram must resolve to a known identity with an explicit role/tenant.
 * Unknown principals are rejected — no anonymous access.
 */

import type { Identity, ChannelType } from "../schema/canonical.js";

export class AuthenticationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "AuthenticationError";
  }
}

function key(channel: ChannelType, externalId: string): string {
  return `${channel}:${externalId}`;
}

export class IdentityDirectory {
  private readonly map = new Map<string, Identity>();

  register(channel: ChannelType, externalId: string, identity: Identity): this {
    this.map.set(key(channel, externalId), identity);
    return this;
  }

  /** Resolve a channel principal to a trusted identity, or throw. */
  resolve(channel: ChannelType, externalId: string): Identity {
    const identity = this.map.get(key(channel, externalId));
    if (!identity) {
      throw new AuthenticationError(
        `unknown ${channel} principal "${externalId}" — access denied`,
      );
    }
    return identity;
  }
}
