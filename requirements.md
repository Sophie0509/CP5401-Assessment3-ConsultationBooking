# Requirements — V1.0 Baseline

## Problem
Students need a simple way to book staff consultation sessions without creating overlapping bookings or exceeding slot capacity.

## User roles
- Student
- Staff

## Functional requirements
- **FR1:** Staff can create consultation slots with date, start time, end time and capacity.
- **FR2:** Students can book an available consultation slot.
- **FR3:** Students can view their own bookings.
- **FR4:** Students can cancel only their own confirmed bookings.

## Business rules
- **BR1:** A student's confirmed consultation bookings must not overlap.
- **BR2:** A slot must not exceed its configured capacity.
- **BR3:** A slot end time must be later than its start time.

## Software quality requirements
- **QR1:** Invalid booking requests must be rejected with a clear message and must not create a confirmed booking.
- **QR2:** Important business rules and boundary cases must be covered by automated tests executed by GitHub Actions.

## Risk and treatment
- **Risk:** A booking change could break overlap or capacity rules.
- **Treatment:** Keep automated regression tests for overlap, boundary and capacity behaviour and run them on every push and pull request.

# V1.1 Change Requirement
- **FR5:** When a slot is full, an eligible student is placed on a FIFO waitlist.
- **BR4:** A student must not have duplicate active entries for the same slot.
- **BR5:** Cancelling a confirmed booking may promote the first eligible waitlisted student without violating overlap or capacity rules.
