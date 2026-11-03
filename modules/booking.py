from dataclasses import dataclass, asdict
from typing import Dict, List

VALID_ROLES = {"Student", "Staff"}


class BookingError(ValueError):
    """Raised when a booking request violates a business rule."""


@dataclass
class Slot:
    slot_id: str
    staff_name: str
    date: str
    start_time: str
    end_time: str
    capacity: int = 1


@dataclass
class Booking:
    booking_id: str
    student_name: str
    slot_id: str
    status: str = "CONFIRMED"


def _to_minutes(value: str) -> int:
    try:
        hour, minute = value.split(":")
        hour_i, minute_i = int(hour), int(minute)
    except Exception as exc:
        raise BookingError("Time must use HH:MM format") from exc
    if not (0 <= hour_i <= 23 and 0 <= minute_i <= 59):
        raise BookingError("Time must use a valid 24-hour value")
    return hour_i * 60 + minute_i


def validate_slot(slot: Slot) -> None:
    if not slot.slot_id.strip() or not slot.staff_name.strip() or not slot.date.strip():
        raise BookingError("Slot ID, staff name and date are required")
    if slot.capacity < 1:
        raise BookingError("Capacity must be at least 1")
    if _to_minutes(slot.start_time) >= _to_minutes(slot.end_time):
        raise BookingError("End time must be later than start time")


def slots_overlap(slot_a: Slot, slot_b: Slot) -> bool:
    if slot_a.date != slot_b.date:
        return False
    return _to_minutes(slot_a.start_time) < _to_minutes(slot_b.end_time) and _to_minutes(slot_b.start_time) < _to_minutes(slot_a.end_time)


def create_slot(slots: Dict[str, Slot], slot: Slot) -> Slot:
    validate_slot(slot)
    if slot.slot_id in slots:
        raise BookingError("Slot ID already exists")
    slots[slot.slot_id] = slot
    return slot


def _confirmed_for_slot(bookings: List[Booking], slot_id: str) -> List[Booking]:
    return [b for b in bookings if b.slot_id == slot_id and b.status == "CONFIRMED"]


def _student_confirmed_bookings(bookings: List[Booking], student_name: str) -> List[Booking]:
    return [b for b in bookings if b.student_name == student_name and b.status == "CONFIRMED"]


def book_slot(slots: Dict[str, Slot], bookings: List[Booking], student_name: str, slot_id: str) -> Booking:
    student_name = student_name.strip()
    if not student_name:
        raise BookingError("Student name is required")
    if slot_id not in slots:
        raise BookingError("Selected slot does not exist")

    requested = slots[slot_id]
    for existing in _student_confirmed_bookings(bookings, student_name):
        existing_slot = slots[existing.slot_id]
        if slots_overlap(existing_slot, requested):
            raise BookingError("Student cannot hold overlapping consultation bookings")

    if len(_confirmed_for_slot(bookings, slot_id)) >= requested.capacity:
        raise BookingError("Selected consultation slot is full")

    booking = Booking(
        booking_id=f"B{len(bookings) + 1:03d}",
        student_name=student_name,
        slot_id=slot_id,
    )
    bookings.append(booking)
    return booking


def cancel_booking(bookings: List[Booking], booking_id: str, student_name: str) -> Booking:
    for booking in bookings:
        if booking.booking_id == booking_id:
            if booking.student_name != student_name:
                raise BookingError("Students may cancel only their own bookings")
            if booking.status != "CONFIRMED":
                raise BookingError("Only confirmed bookings can be cancelled")
            booking.status = "CANCELLED"
            return booking
    raise BookingError("Booking not found")


def booking_rows(bookings: List[Booking]) -> List[dict]:
    return [asdict(item) for item in bookings]
