# Manual Validation Record

Purpose: demonstrate that the deployed application meets the intended Student and Staff user needs, not only that the code passes automated tests.

**Date tested:** 2026-11-09  
**Tester:** Student tester  
**Deployment URL:** https://cp5401-consultation-booking.streamlit.app  
**Version tested:** V1.1

## Scenario A — Staff creates a slot

1. Open the deployed Streamlit application.
2. Select **Staff**.
3. Create slot `S001` with staff name `Dr Lee`, time 10:00–11:00 and capacity 1.
4. Expected: the slot appears in the available-slots table.

**Result: PASS**

Observed evidence:
- The application displayed **Slot created**.
- `S001` appeared in the available-slots table with capacity 1.

## Scenario B — Student books and views a slot

1. Select **Student** and enter `Alex`.
2. Book `S001`.
3. Expected: status is `CONFIRMED` and Alex can see the booking.

**Result: PASS**

Observed evidence:
- The application displayed **Booking B001 confirmed**.
- Alex's booking table showed `B001 / Alex / S001 / CONFIRMED`.

## Scenario C — Full slot creates a waitlist entry

1. Enter a second student, `Jamie`.
2. Book the same capacity-1 slot.
3. Expected: Jamie receives `WAITLISTED`, while the confirmed capacity remains 1.

**Result: PASS**

Observed evidence:
- The application displayed **Slot is full. Added to waitlist as B002**.
- Jamie's booking table showed `B002 / Jamie / S001 / WAITLISTED`.

## Scenario D — Cancellation promotes the first eligible student

1. Return to Alex and cancel the confirmed booking.
2. Expected: Alex becomes `CANCELLED` and Jamie becomes `CONFIRMED`.

**Result: PASS**

Observed evidence:
- Alex's booking table showed `B001 / Alex / S001 / CANCELLED`.
- Jamie's booking table then showed `B002 / Jamie / S001 / CONFIRMED`.

## Scenario E — Invalid/repeated booking is rejected

1. Jamie attempts to book `S001` again after already holding the confirmed booking.
2. Expected: the request is rejected and no second confirmed booking is created.

**Result: PASS**

Observed evidence:
- The application displayed **Student cannot hold overlapping consultation bookings**.
- Jamie still had only the existing `B002` confirmed booking.

## Overall Validation Result

**PASS — all five planned deployed validation scenarios completed successfully.**

The deployed V1.1 application demonstrated the intended Staff and Student workflows, FIFO waitlist behaviour, promotion after cancellation, preservation of the overlap rule, and clear rejection of an invalid repeated booking.
