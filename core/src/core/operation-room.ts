/**
 * AI Operation Room — Core (skeleton).
 * The single place every channel funnels into: validate -> authorize -> audit.
 * Execution/orchestration (Claude Code, tools, knowledge) plugs in behind the
 * `onAllowed` hook in later steps (A4-A6). No external calls here yet.
 */

import {
  validateCanonicalRequest,
  type CanonicalRequest,
} from "../schema/canonical.js";
import { decide, type Resource, type PolicyDecision } from "../policy/policy-engine.js";
import { AuditLog } from "../audit/audit.js";

export interface HandleResult {
  request: CanonicalRequest;
  decision: PolicyDecision;
  /** populated only when the decision is "allow" and a handler ran */
  output?: unknown;
}

/** Resolves which resource a request targets. Stubbed until step A6. */
export type ResourceResolver = (req: CanonicalRequest) => Resource;

/** Runs the actual work once a request is allowed. Stubbed until step A6. */
export type AllowedHandler = (req: CanonicalRequest, resource: Resource) => unknown;

export class OperationRoom {
  constructor(
    private readonly resolveResource: ResourceResolver,
    private readonly audit: AuditLog = new AuditLog(),
    private readonly onAllowed?: AllowedHandler,
  ) {}

  /** Entry point for every channel adapter. Accepts raw, untrusted input. */
  handle(raw: unknown): HandleResult {
    const request = validateCanonicalRequest(raw);
    const resource = this.resolveResource(request);
    const decision = decide(request, resource);

    this.audit.append({
      userId: request.identity.userId,
      tenantId: request.identity.tenantId,
      role: request.identity.role,
      channel: request.channel.type,
      action: request.intent,
      resource: resource.name,
      dataClassification: resource.classification,
      decision: decision.decision,
      decisionReason: decision.reason,
    });

    if (decision.decision === "allow" && this.onAllowed) {
      return { request, decision, output: this.onAllowed(request, resource) };
    }
    return { request, decision };
  }

  auditLog(): AuditLog {
    return this.audit;
  }
}
