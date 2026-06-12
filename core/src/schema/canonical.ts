/**
 * Canonical Message Schema (§4.7.2).
 * Every channel adapter (Telegram, Web, PWA, future) normalizes its raw input
 * into this single shape BEFORE it reaches the core. This is what makes the
 * core channel-agnostic: channel specifics never leak past the adapter.
 */

import type { Role } from "../policy/classification.js";

export type ChannelType = "telegram" | "web" | "pwa";
export type ChannelExposureType = "private" | "internal" | "public";
export type Intent = "read" | "review" | "write" | "code" | "report" | "execute";

export interface Identity {
  /** stable user id from the auth provider (Supabase), not the channel id */
  userId: string;
  /** the tenant this user belongs to — enforced on every request */
  tenantId: string;
  role: Role;
}

export interface ChannelInfo {
  type: ChannelType;
  exposure: ChannelExposureType;
}

export interface CanonicalRequest {
  requestId: string;
  identity: Identity;
  channel: ChannelInfo;
  intent: Intent;
  payload: {
    text: string;
    attachments?: string[];
  };
  timestamp: string; // ISO-8601
}

const CHANNEL_TYPES: readonly ChannelType[] = ["telegram", "web", "pwa"];
const EXPOSURES: readonly ChannelExposureType[] = ["private", "internal", "public"];
const INTENTS: readonly Intent[] = ["read", "review", "write", "code", "report", "execute"];
const ROLES: readonly Role[] = ["owner", "employee", "client"];

export class SchemaValidationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "SchemaValidationError";
  }
}

function requireString(value: unknown, field: string): string {
  if (typeof value !== "string" || value.trim() === "") {
    throw new SchemaValidationError(`Field "${field}" must be a non-empty string`);
  }
  return value;
}

function requireOneOf<T extends string>(
  value: unknown,
  allowed: readonly T[],
  field: string,
): T {
  if (typeof value !== "string" || !allowed.includes(value as T)) {
    throw new SchemaValidationError(
      `Field "${field}" must be one of: ${allowed.join(", ")}`,
    );
  }
  return value as T;
}

/**
 * Validate raw (untrusted) channel input and return a typed CanonicalRequest.
 * Throws SchemaValidationError on any malformed field — the core only ever
 * sees validated requests.
 */
export function validateCanonicalRequest(raw: unknown): CanonicalRequest {
  if (typeof raw !== "object" || raw === null) {
    throw new SchemaValidationError("Request must be an object");
  }
  const r = raw as Record<string, unknown>;
  const identity = (r.identity ?? {}) as Record<string, unknown>;
  const channel = (r.channel ?? {}) as Record<string, unknown>;
  const payload = (r.payload ?? {}) as Record<string, unknown>;

  const attachments = payload.attachments;
  if (attachments !== undefined && !Array.isArray(attachments)) {
    throw new SchemaValidationError(`Field "payload.attachments" must be an array`);
  }

  const result: CanonicalRequest = {
    requestId: requireString(r.requestId, "requestId"),
    identity: {
      userId: requireString(identity.userId, "identity.userId"),
      tenantId: requireString(identity.tenantId, "identity.tenantId"),
      role: requireOneOf<Role>(identity.role, ROLES, "identity.role"),
    },
    channel: {
      type: requireOneOf<ChannelType>(channel.type, CHANNEL_TYPES, "channel.type"),
      exposure: requireOneOf<ChannelExposureType>(
        channel.exposure,
        EXPOSURES,
        "channel.exposure",
      ),
    },
    intent: requireOneOf<Intent>(r.intent, INTENTS, "intent"),
    payload: {
      text: requireString(payload.text, "payload.text"),
      ...(attachments !== undefined
        ? { attachments: (attachments as unknown[]).map((a) => String(a)) }
        : {}),
    },
    timestamp: requireString(r.timestamp, "timestamp"),
  };

  return result;
}
