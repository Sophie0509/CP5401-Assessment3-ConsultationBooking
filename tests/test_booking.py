import pytest

from modules.booking import BookingError, Slot, book_slot, cancel_booking, create_slot


def sample_slots(capacity=1):
    slots = {}
    create_slot(slots, Slot("S1", "Dr Lee", "2026-11-10", "10:00", "11:00", capacity))
    create_slot(slots, Slot("S2", "Dr Lee", "2026-11-10", "10:30", "11:30", 1))
    create_slot(slots, Slot("S3", "Dr Lee", "2026-11-10", "11:00", "12:00", 1))
    return slots


def test_valid_booking_is_confirmed():
    slots = sample_slots()
    bookings = []
    result = book_slot(slots, bookings, "Alex", "S1")
    assert result.status == "CONFIRMED"
    assert result.student_name == "Alex"


def test_empty_student_name_is_rejected():
    slots = sample_slots()
    with pytest.raises(BookingError, match="Student name is required"):
        book_slot(slots, [], "   ", "S1")


def test_overlapping_booking_is_rejected():
    slots = sample_slots()
    bookings = []
    book_slot(slots, bookings, "Alex", "S1")
    with pytest.raises(BookingError, match="overlapping"):
        book_slot(slots, bookings, "Alex", "S2")


def test_touching_boundary_is_allowed():
    slots = sample_slots()
    bookings = []
    book_slot(slots, bookings, "Alex", "S1")
    result = book_slot(slots, bookings, "Alex", "S3")
    assert result.status == "CONFIRMED"


def test_slot_capacity_is_enforced():
    slots = sample_slots(capacity=1)
    bookings = []
    book_slot(slots, bookings, "Alex", "S1")
    with pytest.raises(BookingError, match="full"):
        book_slot(slots, bookings, "Jamie", "S1")


def test_student_cannot_cancel_another_students_booking():
    slots = sample_slots()
    bookings = []
    booking = book_slot(slots, bookings, "Alex", "S1")
    with pytest.raises(BookingError, match="own bookings"):
        cancel_booking(bookings, booking.booking_id, "Jamie")


def test_student_can_cancel_own_booking():
    slots = sample_slots()
    bookings = []
    booking = book_slot(slots, bookings, "Alex", "S1")
    cancelled = cancel_booking(bookings, booking.booking_id, "Alex")
    assert cancelled.status == "CANCELLED"
