/**
 * Multi-tenancy model — built in from day one (§14.1 of the work plan).
 * DRFONE itself is Tenant 0; every external client is just another tenant.
 * `tenantId` travels with every request, resource, and audit record.
 */

/** Package tiers map to entitlements / feature sets per tenant (§14.2). */
export type Tier = "starter" | "business" | "enterprise";

export interface Tenant {
  tenantId: string;
  name: string;
  tier: Tier;
  /** enterprise tenants may run on a dedicated/private instance */
  dedicated: boolean;
}

/** DRFONE's own tenant — the first user of its own system. */
export const TENANT_DRFONE: Tenant = {
  tenantId: "tenant-0-drfone",
  name: "DRFONE",
  tier: "enterprise",
  dedicated: true,
};
