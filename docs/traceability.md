# Requirements-to-Evidence Traceability

This table links requirements and business rules to automated or reviewable evidence.

| Requirement / rule | Evidence | Why it matters |
|---|---|---|
| FR1 Staff creates a consultation slot | `test_invalid_slot_time_is_rejected` + live Streamlit demo | Verifies slot validation and supports the staff workflow. |
| FR2 Student books a slot | `test_valid_booking_is_confirmed` | Confirms the normal booking path. |
| FR3 Student views own bookings | Live Streamlit validation scenario | Confirms the user-facing view requirement. |
| FR4 Student cancels only own booking | `test_student_can_cancel_own_booking_without_waitlist`, `test_student_cannot_cancel_another_students_booking` | Covers successful and rejected cancellation paths. |
| BR1 No overlapping confirmed bookings | `test_overlapping_booking_is_rejected`, `test_touching_boundary_is_allowed` | Covers failure and exact boundary behaviour. |
| BR2 Capacity is not exceeded | `test_waitlist_does_not_exceed_confirmed_capacity` | Confirms that waitlisting does not create over-capacity confirmed bookings. |
| BR3 End time later than start time | `test_invalid_slot_time_is_rejected` | Covers invalid slot-time input. |
| FR5 Full slots create FIFO waitlist entries | `test_full_slot_places_student_on_waitlist`, `test_cancellation_promotes_first_eligible_waitlisted_student` | Verifies the assessed V1.1 change. |
| BR4 No duplicate active entry for same slot | `test_duplicate_waitlist_entry_is_rejected` | Protects against repeated-click duplicate state. |
| BR5 Promotion preserves overlap/capacity rules | `test_promotion_does_not_create_overlap`, `test_waitlist_does_not_exceed_confirmed_capacity` | Protects existing rules after the change. |
| QR1 Invalid requests fail clearly without incorrect confirmed state | invalid-name, overlap, duplicate, unauthorised-cancellation and invalid-time tests | Provides negative-path quality evidence. |
| QR2 Automated tests run in CI | `.github/workflows/quality-checks.yml` | Makes verification repeatable on push and pull request. |

## V1.0 regression treatment after V1.1
The unaffected V1.0 behaviours remain covered as regression evidence. The original V1.0 capacity test expected a full slot to be rejected; this expected result was deliberately revised because the approved V1.1 change replaces rejection with FIFO waitlisting. A replacement capacity-invariant test confirms that the number of `CONFIRMED` bookings still never exceeds slot capacity.
