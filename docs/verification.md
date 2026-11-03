# Verification Evidence — V1.0 and V1.1

Verification question: **Are we building the system according to the specification?**

Primary activity: requirements-to-test review plus automated CI checks.

Evidence:
- FR2 / BR1 → `test_valid_booking_is_confirmed`, `test_overlapping_booking_is_rejected`
- BR1 boundary → `test_touching_boundary_is_allowed`
- BR2 → `test_waitlist_does_not_exceed_confirmed_capacity`
- BR3 → `test_invalid_slot_time_is_rejected`
- FR4 → own-cancellation and unauthorised-cancellation tests
- FR5 / BR4 / BR5 → waitlist creation, duplicate-entry, FIFO promotion and overlap-safe promotion tests
- QR1 → invalid student name and business-rule rejection tests
- QR2 → GitHub Actions runs dependency consistency, compile, automated test and coverage checks on push/PR

Local pre-PR evidence: **12 automated tests pass** and module coverage is **88.89%**, above the configured 85% threshold.

Required merge evidence: the GitHub Actions workflow must pass before the assessed change is merged.
