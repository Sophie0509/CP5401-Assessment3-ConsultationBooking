# Review Findings and Pre-merge Decision

## Finding 1 — promotion could create overlap
- Affected code: waitlist promotion logic.
- Assessment: substantive business-rule risk.
- Evidence: regression test `test_promotion_does_not_create_overlap`.
- Disposition: corrected by checking overlap before promotion.

## Finding 2 — duplicate waitlist entries
- Affected code: booking creation.
- Assessment: valid defect risk because repeated clicks could create duplicate active entries.
- Evidence: `test_duplicate_waitlist_entry_is_rejected`.
- Disposition: corrected by rejecting an existing confirmed/waitlisted entry for the same slot.

## Regression-treatment decision
The old V1.0 test that expected a full slot to be rejected was revised because V1.1 intentionally changes this contract to waitlisting. The unchanged capacity rule is protected by `test_waitlist_does_not_exceed_confirmed_capacity`.

## Pre-merge decision
**Ready to merge only after required GitHub Actions checks pass.**

Reason: the change is scoped to waitlist behaviour, unaffected V1.0 behaviours remain protected, new failure/boundary tests cover the change risks, and no blocking review finding remains unresolved.
