# CP5401 Assessment 3 — Submission Summary

**Application title:** Campus Consultation Booking System  
**Student name:** [Your name]  
**Student ID:** [Your student ID]  
**GitHub repository:** https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking  
**Streamlit deployment:** https://cp5401-consultation-booking.streamlit.app  
**V1.0 release:** https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/releases/tag/v1.0  
**V1.1 release:** https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/releases/tag/v1.1

## Change Request Summary

V1.1 adds FIFO waitlist support when a consultation slot is full. The impact analysis identified risks involving duplicate waitlist entries, capacity, overlap and regression of existing booking behaviour. The change was implemented on a separate branch, reviewed, tested, merged through Pull Request #2 and released as V1.1.

## Verification, Security and Validation Summary

Automated verification covers normal booking behaviour, invalid input, overlap boundaries, cancellation ownership, capacity protection, waitlist creation, duplicate waitlist prevention and safe promotion.

GitHub Actions now provides automated pre-merge quality gates for:
- dependency consistency;
- static analysis with Ruff;
- Python security static analysis with Bandit;
- dependency vulnerability scanning with pip-audit, including transitive dependencies;
- Python compile/build verification;
- 12 automated tests with coverage;
- an 85% coverage threshold.

Tool-generated findings are manually triaged before approval rather than being accepted blindly. The security scan evidence and dispositions are recorded in `docs/security-scanning.md`.

Deployed manual validation was completed on 2026-11-09. All five planned scenarios passed: Staff slot creation, Alex confirmed booking, Jamie waitlisting, promotion after Alex's cancellation, and rejection of an invalid repeated booking.

## Evidence Links

- Change Request: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/issues/1
- Pull Request: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/pull/2
- Quality Pipeline Hardening Issue: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/issues/3
- Impact Analysis: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/blob/main/docs/impact-analysis.md
- Review Intake: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/blob/main/docs/review-intake.md
- Review Findings / Merge Decision: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/blob/main/docs/review-findings.md
- Security Scanning / Human Triage: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/blob/main/docs/security-scanning.md
- Traceability: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/blob/main/docs/traceability.md
- Test Rationale: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/blob/main/docs/test-rationale.md
- Manual Validation Record: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/blob/main/docs/manual-validation.md
- AI-use Record: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/blob/main/docs/ai-use.md
