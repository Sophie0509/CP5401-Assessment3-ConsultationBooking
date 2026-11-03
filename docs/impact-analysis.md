# Impact Analysis — Waitlist Change

## Affected requirements
- FR2 booking behaviour is changed when a slot is full.
- BR1 overlap prevention must remain unchanged.
- BR2 capacity enforcement must remain unchanged.
- New FR5, BR4 and BR5 define waitlist and promotion behaviour.

## Affected components
- `modules/booking.py`
- `app.py`
- `tests/test_booking.py`
- requirements and change documentation

## Risks
1. A waitlisted student may be added twice.
2. Promotion after cancellation may exceed slot capacity.
3. Promotion may create an overlapping confirmed booking.
4. Existing V1.0 booking or cancellation behaviour may regress.

## Test impact
- Retain the unaffected V1.0 tests as regression tests.
- Revise the old full-slot expectation because V1.1 intentionally changes it from rejection to waitlisting.
- Add a replacement capacity-invariant test to prove confirmed bookings still never exceed capacity.
- Add waitlist creation, duplicate-entry and promotion tests.
- Add a regression test showing promotion does not create an overlap.

## Risk classification
Medium: the change modifies user-visible business logic and booking state, but it does not change authentication, secrets, external dependencies or deployment configuration.
