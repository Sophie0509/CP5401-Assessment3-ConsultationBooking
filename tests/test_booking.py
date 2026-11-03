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


def test_full_slot_places_student_on_waitlist():
    slots = sample_slots(capacity=1)
    bookings = []
    book_slot(slots, bookings, "Alex", "S1")
    result = book_slot(slots, bookings, "Jamie", "S1")
    assert result.status == "WAITLISTED"


def test_duplicate_waitlist_entry_is_rejected():
    slots = sample_slots(capacity=1)
    bookings = []
    book_slot(slots, bookings, "Alex", "S1")
    book_slot(slots, bookings, "Jamie", "S1")
    with pytest.raises(BookingError, match="already has"):
        book_slot(slots, bookings, "Jamie", "S1")


def test_cancellation_promotes_first_eligible_waitlisted_student():
    slots = sample_slots(capacity=1)
    bookings = []
    alex = book_slot(slots, bookings, "Alex", "S1")
    jamie = book_slot(slots, bookings, "Jamie", "S1")
    cancelled, promoted = cancel_booking(slots, bookings, alex.booking_id, "Alex")
    assert cancelled.status == "CANCELLED"
    assert promoted is jamie
    assert jamie.status == "CONFIRMED"


def test_promotion_does_not_create_overlap():
    slots = sample_slots(capacity=1)
    bookings = []
    alex = book_slot(slots, bookings, "Alex", "S1")
    jamie = book_slot(slots, bookings, "Jamie", "S2")
    waitlisted = book_slot(slots, bookings, "Taylor", "S1")
    assert waitlisted.status == "WAITLISTED"
    from modules.booking import Booking
    jamie_wait = Booking("B999", "Jamie", "S1", "WAITLISTED")
    bookings.insert(1, jamie_wait)
    _, promoted = cancel_booking(slots, bookings, alex.booking_id, "Alex")
    assert jamie_wait.status == "WAITLISTED"
    assert promoted.student_name == "Taylor"


def test_student_cannot_cancel_another_students_booking():
    slots = sample_slots()
    bookings = []
    booking = book_slot(slots, bookings, "Alex", "S1")
    with pytest.raises(BookingError, match="own bookings"):
        cancel_booking(slots, bookings, booking.booking_id, "Jamie")


def test_student_can_cancel_own_booking_without_waitlist():
    slots = sample_slots()
    bookings = []
    booking = book_slot(slots, bookings, "Alex", "S1")
    cancelled, promoted = cancel_booking(slots, bookings, booking.booking_id, "Alex")
    assert cancelled.status == "CANCELLED"
    assert promoted is None


def test_waitlist_does_not_exceed_confirmed_capacity():
    slots = sample_slots(capacity=1)
    bookings = []
    book_slot(slots, bookings, "Alex", "S1")
    waitlisted = book_slot(slots, bookings, "Jamie", "S1")
    confirmed = [b for b in bookings if b.slot_id == "S1" and b.status == "CONFIRMED"]
    assert len(confirmed) == 1
    assert waitlisted.status == "WAITLISTED"


def test_invalid_slot_time_is_rejected():
    slots = {}
    with pytest.raises(BookingError, match="End time must be later"):
        create_slot(slots, Slot("BAD", "Dr Lee", "2026-11-10", "11:00", "10:00", 1))
