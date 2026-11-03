import streamlit as st

from modules.booking import BookingError, Slot, book_slot, booking_rows, cancel_booking, create_slot

st.set_page_config(page_title="Campus Consultation Booking", page_icon="📅", layout="wide")
st.title("Campus Consultation Booking System")
st.caption("CP5401 Assessment 3 — V1.0 baseline")

if "slots" not in st.session_state:
    st.session_state.slots = {}
if "bookings" not in st.session_state:
    st.session_state.bookings = []

role = st.sidebar.selectbox("Role", ["Student", "Staff"])

if role == "Staff":
    st.subheader("Create consultation slot")
    with st.form("slot_form"):
        slot_id = st.text_input("Slot ID", "S001")
        staff_name = st.text_input("Staff name", "Dr Lee")
        date = st.date_input("Date").isoformat()
        start_time = st.time_input("Start time").strftime("%H:%M")
        end_time = st.time_input("End time").strftime("%H:%M")
        capacity = st.number_input("Capacity", min_value=1, max_value=10, value=1)
        submitted = st.form_submit_button("Create slot")
    if submitted:
        try:
            create_slot(st.session_state.slots, Slot(slot_id, staff_name, date, start_time, end_time, int(capacity)))
            st.success("Slot created")
        except BookingError as exc:
            st.error(str(exc))

    st.subheader("Available slots")
    st.dataframe([vars(s) for s in st.session_state.slots.values()], use_container_width=True)

else:
    student = st.text_input("Student name", "Alex")
    st.subheader("Book a consultation")
    if not st.session_state.slots:
        st.info("No consultation slots have been created yet. Switch to Staff to create one.")
    else:
        slot_id = st.selectbox("Available slot", list(st.session_state.slots.keys()))
        if st.button("Book selected slot"):
            try:
                booking = book_slot(st.session_state.slots, st.session_state.bookings, student, slot_id)
                st.success(f"Booking {booking.booking_id} confirmed")
            except BookingError as exc:
                st.error(str(exc))

    st.subheader("My bookings")
    mine = [b for b in st.session_state.bookings if b.student_name == student]
    st.dataframe(booking_rows(mine), use_container_width=True)

    confirmed = [b.booking_id for b in mine if b.status == "CONFIRMED"]
    if confirmed:
        cancel_id = st.selectbox("Booking to cancel", confirmed)
        if st.button("Cancel booking"):
            try:
                cancel_booking(st.session_state.bookings, cancel_id, student)
                st.success(f"Booking {cancel_id} cancelled")
                st.rerun()
            except BookingError as exc:
                st.error(str(exc))
