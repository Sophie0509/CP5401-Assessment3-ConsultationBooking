# Verification Evidence — V1.0

Verification question: **Are we building the system according to the specification?**

Activity: requirements-to-test review.

Evidence:
- FR2 / BR1 → `test_valid_booking_is_confirmed`, `test_overlapping_booking_is_rejected`
- BR1 boundary → `test_touching_boundary_is_allowed`
- BR2 → `test_slot_capacity_is_enforced`
- FR4 → own-cancellation and unauthorised-cancellation tests
- QR1 → invalid student name and business-rule rejection tests

Expected result: all automated tests pass before V1.0 release.
