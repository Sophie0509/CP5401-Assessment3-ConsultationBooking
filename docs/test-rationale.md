# Automated Test Rationale

The automated suite is intentionally small and requirement-focused. It covers normal behaviour, invalid input, boundaries, ownership rules, the assessed V1.1 change and regression risks.

- `test_valid_booking_is_confirmed` — normal path for FR2.
- `test_empty_student_name_is_rejected` — invalid required input for QR1.
- `test_overlapping_booking_is_rejected` — failure path for BR1.
- `test_touching_boundary_is_allowed` — exact overlap boundary; prevents an inclusive-boundary defect.
- `test_full_slot_places_student_on_waitlist` — main V1.1 behaviour for FR5.
- `test_duplicate_waitlist_entry_is_rejected` — invalid repeated action for BR4.
- `test_cancellation_promotes_first_eligible_waitlisted_student` — FIFO promotion path for BR5.
- `test_promotion_does_not_create_overlap` — regression test for the main change risk.
- `test_student_cannot_cancel_another_students_booking` — rejected ownership path for FR4.
- `test_student_can_cancel_own_booking_without_waitlist` — preserved V1.0 cancellation behaviour.
- `test_waitlist_does_not_exceed_confirmed_capacity` — preserved BR2 invariant after V1.1.
- `test_invalid_slot_time_is_rejected` — invalid/boundary-oriented evidence for BR3.

A passing suite is not treated as proof of complete quality. The live validation and review evidence remain necessary because automated tests only demonstrate the behaviours that are explicitly asserted.
