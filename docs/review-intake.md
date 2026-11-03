# AI-assisted Change Review Intake

## Intended behaviour
Add FIFO waitlist behaviour when a consultation slot is full.

## Must remain unchanged
Overlap prevention, capacity enforcement, own-booking cancellation and unaffected V1.0 regression behaviour.

## AI tool and task
ChatGPT was used to help implement the waitlist change, revise tests and update documentation.

## Affected files
- `modules/booking.py`
- `app.py`
- `tests/test_booking.py`
- requirements and change documentation

## AI assumptions to verify
1. List order can represent FIFO order for this small assessment application.
2. A waitlisted student is promoted only if promotion does not create an overlap.
3. Local in-memory/session-state storage is acceptable for the assessment demonstration.

## Human verification
- Read and explain the changed logic.
- Run all original and new tests.
- Manually demonstrate booking, waitlisting, cancellation and promotion.

## Risk classification
Medium: user-visible booking-state logic changes, but no authentication, secrets or external dependency changes.
