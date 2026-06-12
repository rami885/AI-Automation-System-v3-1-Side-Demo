/**
 * Pilot A — Daily Operations Brief (Step A6). Read-only.
 * Answers: what happened, what's late, what needs the owner's decision,
 * what's high priority. Pure function over tenant-scoped knowledge — no sending,
 * no side effects. The brief is "internal" classified.
 */

import type { KnowledgeBase, OpsItem } from "../knowledge/knowledge-base.js";

export interface DailyBrief {
  tenantId: string;
  generatedAt: string;
  counts: { total: number; done: number; inProgress: number; open: number; late: number };
  late: OpsItem[];
  needsDecision: OpsItem[];
  highPriority: OpsItem[];
}

export function generateDailyBrief(kb: KnowledgeBase, tenantId: string): DailyBrief {
  const items = kb.opsItems(tenantId);
  const by = (s: OpsItem["status"]) => items.filter((i) => i.status === s);

  return {
    tenantId,
    generatedAt: new Date().toISOString(),
    counts: {
      total: items.length,
      done: by("done").length,
      inProgress: by("in_progress").length,
      open: by("open").length,
      late: by("late").length,
    },
    late: by("late"),
    needsDecision: items.filter((i) => i.needsOwnerDecision && i.status !== "done"),
    highPriority: items.filter((i) => i.priority === "high" && i.status !== "done"),
  };
}

/** Human-readable Arabic rendering for a chat channel. */
export function renderDailyBrief(brief: DailyBrief): string {
  const { counts } = brief;
  const line = (items: OpsItem[]) =>
    items.length === 0 ? "  — لا شيء" : items.map((i) => `  • ${i.title}`).join("\n");

  return [
    "📋 التقرير اليومي للعمليات (DRFONE)",
    `الإجمالي: ${counts.total} | منجز: ${counts.done} | جارٍ: ${counts.inProgress} | مفتوح: ${counts.open} | متأخر: ${counts.late}`,
    "",
    "⏰ المتأخر:",
    line(brief.late),
    "",
    "🔑 يحتاج قرار رامي:",
    line(brief.needsDecision),
    "",
    "🔥 أولوية عالية:",
    line(brief.highPriority),
  ].join("\n");
}
