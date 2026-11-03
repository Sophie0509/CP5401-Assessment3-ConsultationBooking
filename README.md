# Campus Consultation Booking System

Small Streamlit application for CP5401 Assessment 3.

## Purpose
The application allows staff to create consultation slots and students to book, view and cancel consultation bookings while enforcing overlap and capacity rules.

## Run locally
```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Run tests
```bash
pytest -q
```

## Quality engineering evidence
- `requirements.md` — functional and quality requirements
- `tests/` — automated verification and regression tests
- `.github/workflows/quality-checks.yml` — continuous integration
- `docs/verification.md` — verification evidence
- `docs/validation.md` — validation plan/evidence

## Releases
- `v1.0` — baseline booking system
- `v1.1` — assessed change (waitlist feature)
