/**
 * The two axes (besides role) that drive every authorization decision (§4.7.3):
 *  - how sensitive the resource is (DataClassification)
 *  - how exposed the channel is (ChannelExposure)
 *
 * The rule "a public channel can never see sensitive data" is attribute-based:
 * it compares resource sensitivity against channel exposure — not role alone.
 */

/** Sensitivity of a resource. Higher rank = more sensitive. */
export type DataClassification =
  | "public"
  | "internal"
  | "confidential"
  | "private"; // rami_private / finance_private both map here

/** How exposed a channel is to the outside world. */
export type ChannelExposure = "public" | "internal" | "private";

/** Who is acting. */
export type Role = "owner" | "employee" | "client";

/** Ordered ranking so we can compare sensitivity numerically. */
export const CLASSIFICATION_RANK: Record<DataClassification, number> = {
  public: 0,
  internal: 1,
  confidential: 2,
  private: 3,
};

/**
 * Maximum classification a channel may expose, by its exposure level.
 * A private (owner) channel may surface everything; a public channel only public.
 */
export const CHANNEL_MAX_CLASSIFICATION: Record<ChannelExposure, number> = {
  public: CLASSIFICATION_RANK.public, // 0
  internal: CLASSIFICATION_RANK.internal, // 1
  private: CLASSIFICATION_RANK.private, // 3
};
