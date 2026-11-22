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

## Automated quality gates
GitHub Actions runs the following checks on pushes and pull requests:
- dependency consistency with `pip check`;
- static analysis with `ruff`;
- Python security static analysis with `bandit`;
- dependency vulnerability scanning with `pip-audit`;
- Python compile/build verification;
- automated `pytest` tests with coverage;
- an 85% minimum coverage threshold.

Tool findings are reviewed by a human before the merge decision. A scanner result is evidence, not automatic approval.

## Quality engineering evidence
- `requirements.md` — functional and quality requirements
- `tests/` — automated verification and regression tests
- `.github/workflows/quality-checks.yml` — continuous integration
- `docs/verification.md` — verification evidence
- `docs/validation.md` — validation plan/evidence
- `docs/security-scanning.md` — static/security/dependency scan evidence and triage
- `docs/traceability.md` — requirements-to-test traceability
- `docs/test-rationale.md` — why each automated test is used
- `docs/review-intake.md` — AI-assisted change review intake
- `docs/review-findings.md` — findings and pre-merge decision
- `docs/manual-validation.md` — deployed validation record

## Releases
- `v1.0` — baseline booking system
- `v1.1` — FIFO waitlist feature
