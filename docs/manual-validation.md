# Manual Validation Record

Purpose: demonstrate that the application meets the intended Student and Staff user needs, not only that the code passes automated tests.

## Scenario A — Staff creates a slot
1. Open the deployed Streamlit application.
2. Select **Staff**.
3. Create slot `S001` with a valid date/time and capacity 1.
4. Expected: the slot appears in the available-slots table.

## Scenario B — Student books and views a slot
1. Select **Student** and enter `Alex`.
2. Book `S001`.
3. Expected: status is `CONFIRMED` and Alex can see the booking.

## Scenario C — Full slot creates a waitlist entry
1. Enter a second student, `Jamie`.
2. Book the same capacity-1 slot.
3. Expected: Jamie receives `WAITLISTED`, while the number of confirmed bookings remains 1.

## Scenario D — Cancellation promotes the first eligible student
1. Return to Alex and cancel the confirmed booking.
2. Expected: Alex becomes `CANCELLED` and Jamie becomes `CONFIRMED`.

## Scenario E — Rejected behaviour
Attempt an invalid or unauthorised action, such as a duplicate booking or cancelling another student's booking.
Expected: a clear error is shown and no incorrect confirmed state is created.

## Result record
Complete this only after testing the deployed application.

- Date tested: ____________________
- Tester: ____________________
- Deployment URL: ____________________
- Scenario A: Pass / Fail
- Scenario B: Pass / Fail
- Scenario C: Pass / Fail
- Scenario D: Pass / Fail
- Scenario E: Pass / Fail
- Notes / defects found: ________________________________________________

This record should only be marked as passed after the deployed application has actually been tested.
