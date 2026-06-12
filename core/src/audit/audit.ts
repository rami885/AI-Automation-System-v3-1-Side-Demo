/**
 * Audit log (§4.7.6) — append-only and tamper-evident via a hash chain.
 * Records EVERY decision, including denials and escalations (a denial is the
 * security signal). This in-memory implementation defines the contract; the
 * production sink is Postgres (Supabase) with the same append-only shape.
 */

import { createHash } from "node:crypto";
import type { Decision } from "../policy/policy-engine.js";
import type { DataClassification } from "../policy/classification.js";

export interface AuditRecord {
  auditId: string;
  userId: string;
  tenantId: string;
  role: string;
  channel: string;
  action: string;
  resource: string;
  dataClassification: DataClassification;
  decision: Decision;
  decisionReason: string;
  timestamp: string;
  prevHash: string;
  hash: string;
}

export type AuditInput = Omit<AuditRecord, "auditId" | "timestamp" | "prevHash" | "hash">;

const GENESIS = "0".repeat(64);

function computeHash(record: Omit<AuditRecord, "hash">): string {
  const h = createHash("sha256");
  h.update(
    [
      record.auditId,
      record.userId,
      record.tenantId,
      record.role,
      record.channel,
      record.action,
      record.resource,
      record.dataClassification,
      record.decision,
      record.decisionReason,
      record.timestamp,
      record.prevHash,
    ].join("|"),
  );
  return h.digest("hex");
}

export class AuditLog {
  private readonly records: AuditRecord[] = [];
  private seq = 0;

  /** Append a record; its hash chains to the previous one. */
  append(input: AuditInput): AuditRecord {
    const prevHash = this.records.at(-1)?.hash ?? GENESIS;
    const base: Omit<AuditRecord, "hash"> = {
      ...input,
      auditId: `audit-${++this.seq}`,
      timestamp: new Date().toISOString(),
      prevHash,
    };
    const record: AuditRecord = { ...base, hash: computeHash(base) };
    this.records.push(record);
    return record;
  }

  /** Verify the chain is intact (no record was altered or removed). */
  verify(): boolean {
    let prevHash = GENESIS;
    for (const record of this.records) {
      const { hash, ...rest } = record;
      if (record.prevHash !== prevHash) return false;
      if (computeHash(rest) !== hash) return false;
      prevHash = hash;
    }
    return true;
  }

  all(): readonly AuditRecord[] {
    return this.records;
  }
}
