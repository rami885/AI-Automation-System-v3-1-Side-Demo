/**
 * Policy Decision Point (PDP) — the single, central authorization authority
 * (§4.7.3). Every channel routes through this; nothing is allowed by default.
 *
 * Decision = f(tenant isolation, role, data classification, channel exposure).
 *
 * Order of evaluation:
 *   1. Tenant isolation   — cross-tenant access is always denied.
 *   2. Client ceiling     — clients never exceed "public".
 *   3. Classification fit  — within the channel's exposure ceiling -> allow.
 *   4. Trusted escalation  — owner/employee asking above the ceiling -> escalate
 *                            (routed to owner approval via the Escalation Gate).
 *   5. Otherwise          — deny.
 */

import type { CanonicalRequest } from "../schema/canonical.js";
import {
  CHANNEL_MAX_CLASSIFICATION,
  CLASSIFICATION_RANK,
  type DataClassification,
} from "./classification.js";

export type Decision = "allow" | "deny" | "escalate";

/** A thing the request wants to touch. Always carries its owning tenant. */
export interface Resource {
  /** logical name, e.g. "daily_brief", "finance_report" */
  name: string;
  tenantId: string;
  classification: DataClassification;
}

export interface PolicyDecision {
  decision: Decision;
  reason: string;
}

export function decide(req: CanonicalRequest, resource: Resource): PolicyDecision {
  const { identity, channel } = req;

  // 1. Tenant isolation — the multi-tenant guarantee.
  if (identity.tenantId !== resource.tenantId) {
    return {
      decision: "deny",
      reason: `cross-tenant access denied (identity=${identity.tenantId}, resource=${resource.tenantId})`,
    };
  }

  const resourceRank = CLASSIFICATION_RANK[resource.classification];
  const channelMax = CHANNEL_MAX_CLASSIFICATION[channel.exposure];

  // 2. Clients can never see anything above public, on any channel.
  if (identity.role === "client") {
    if (resourceRank <= CLASSIFICATION_RANK.public) {
      return { decision: "allow", reason: "client access to public resource" };
    }
    return {
      decision: "deny",
      reason: `client may not access ${resource.classification} data`,
    };
  }

  // 3. Within the channel's exposure ceiling -> allow.
  if (resourceRank <= channelMax) {
    return {
      decision: "allow",
      reason: `${resource.classification} within ${channel.exposure} channel ceiling`,
    };
  }

  // 4. Trusted internal user (owner/employee) reaching above the ceiling
  //    is not a hard denial — it is escalated for explicit owner approval.
  return {
    decision: "escalate",
    reason: `${identity.role} requested ${resource.classification} via ${channel.exposure} channel — requires owner approval`,
  };
}
