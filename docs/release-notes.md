# Release Notes

## V1.0 — Baseline
- Staff can create consultation slots.
- Students can book, view and cancel their own bookings.
- Overlap, capacity and slot-time rules are enforced.
- Automated tests and GitHub Actions quality checks are included.

## V1.1 — Waitlist Change
- Full slots place eligible students on a FIFO waitlist.
- Duplicate active waitlist/booking entries for the same slot are rejected.
- Cancelling a confirmed booking promotes the first eligible waitlisted student.
- Promotion preserves overlap and capacity rules.
- Unaffected V1.0 behaviours remain covered by regression tests.
- The former "full slot must reject" test was deliberately revised because the approved change now requires waitlisting; a capacity-invariant test protects the unchanged capacity rule.
