/**
 * Composition root — wires the core for the internal pilot.
 * validate -> authorize -> audit -> (if allowed) run a pilot handler.
 * Still local only: no network, no credentials.
 */

import { OperationRoom } from "../core/operation-room.js";
import type { CanonicalRequest } from "../schema/canonical.js";
import type { Resource } from "../policy/policy-engine.js";
import { AuditLog } from "../audit/audit.js";
import { KnowledgeBase } from "../knowledge/knowledge-base.js";
import { generateDailyBrief, renderDailyBrief } from "../pilots/daily-brief.js";

/** Map a request to the resource it targets (and its classification). */
function resolveResource(req: CanonicalRequest): Resource {
  const tenantId = req.identity.tenantId;
  if (req.intent === "report") {
    return { name: "daily_brief", tenantId, classification: "internal" };
  }
  return { name: "general_query", tenantId, classification: "internal" };
}

export interface App {
  room: OperationRoom;
  audit: AuditLog;
  knowledge: KnowledgeBase;
}

export function buildApp(knowledge: KnowledgeBase, audit = new AuditLog()): App {
  const onAllowed = (req: CanonicalRequest, resource: Resource): unknown => {
    if (resource.name === "daily_brief") {
      return renderDailyBrief(generateDailyBrief(knowledge, req.identity.tenantId));
    }
    return "(سيتم توليد الرد من القلب في خطوة لاحقة)";
  };

  const room = new OperationRoom(resolveResource, audit, onAllowed);
  return { room, audit, knowledge };
}
