/**
 * Knowledge layer (skeleton, read-only).
 * Holds operations items per tenant. In Phase B this is backed by Postgres /
 * the DRFONE knowledge files; for now it is in-memory and local only.
 * Every query is tenant-scoped — no cross-tenant reads.
 */

export type OpsStatus = "open" | "in_progress" | "late" | "done";
export type Priority = "low" | "medium" | "high";

export interface OpsItem {
  id: string;
  tenantId: string;
  title: string;
  status: OpsStatus;
  priority: Priority;
  needsOwnerDecision: boolean;
  due?: string;
}

export class KnowledgeBase {
  private readonly items: OpsItem[];

  constructor(items: OpsItem[] = []) {
    this.items = items;
  }

  /** Operations items for a single tenant only. */
  opsItems(tenantId: string): OpsItem[] {
    return this.items.filter((i) => i.tenantId === tenantId);
  }
}
