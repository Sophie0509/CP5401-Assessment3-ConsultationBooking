# Change Request — Add Waitlist Support

## Requested change
When a consultation slot is full, an eligible student should be placed on a FIFO waitlist instead of receiving only a rejection.

## Intended behaviour
- A full slot places the student on the waitlist with status `WAITLISTED`.
- A student must not appear in the same slot's waitlist more than once.
- When a confirmed booking is cancelled, the first eligible waitlisted student is promoted to `CONFIRMED`.

## Behaviour that must remain unchanged
- Existing overlap prevention must still apply.
- Capacity must still never be exceeded.
- Students may still cancel only their own booking.
- Unaffected V1.0 behaviour remains protected by regression tests.
