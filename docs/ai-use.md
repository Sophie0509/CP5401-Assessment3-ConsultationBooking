# Appendix A — Generative AI Use Record

## Tool used
ChatGPT (OpenAI)

## Significant use
AI assistance was used to help draft the initial project structure, Python/Streamlit code, automated tests, GitHub Actions workflow, change-control records and documentation templates.

## Significant prompt examples
1. "Create a small Streamlit consultation booking application with Student and Staff roles, testable business rules, pytest tests and GitHub Actions evidence suitable for CP5401 Assessment 3."
2. "Add a controlled V1.1 FIFO waitlist change after a V1.0 baseline, including impact analysis, regression tests, review findings and CI evidence."
3. "Review the final quality pipeline against the assessment guidance and add static analysis, security scanning and dependency vulnerability scanning with human triage."

## Human verification performed
The student:
- read and checked the generated code against the documented requirements and business rules;
- ran the complete automated test suite and coverage gate;
- checked normal, invalid, boundary and regression behaviour;
- manually validated the deployed Streamlit application;
- reviewed AI/tool-generated findings instead of treating them as automatic approval;
- recorded review findings, risk classification and merge decisions;
- added final static/security/dependency quality gates through Issue #3 and PR #4.

## Assumptions checked for the assessed change
- Python list order is sufficient to represent FIFO order in this small in-memory assessment application.
- A waitlisted student is promoted only if the promotion does not violate overlap or capacity rules.
- The V1.1 requirement intentionally changes full-slot behaviour from rejection to waitlisting, so the obsolete expected result was revised while unchanged capacity behaviour remained protected.
- Session-state/in-memory storage is acceptable for the demonstration scope; persistence is outside the assessed application scope.

## Final security / dependency verification
The final repository quality pipeline runs:
- Ruff static analysis;
- Bandit Python security static analysis;
- pip-audit dependency vulnerability scanning;
- dependency consistency checks;
- Python compile/build verification;
- pytest regression tests with coverage;
- an 85% minimum coverage threshold.

Final main-branch evidence:
- Ruff: PASS
- Bandit: PASS — no issues identified
- pip-audit: PASS — no known vulnerabilities found
- pytest: PASS — 12 tests
- measured module coverage: 89%

The first broad Ruff run reported import-ordering and typing-modernisation findings. These were manually assessed as low-risk maintainability/style findings rather than behavioural/security defects. The static-analysis gate was narrowed to correctness/unused-code-focused rules, documented, rerun and passed.

## Human ownership
AI assistance does not transfer responsibility. The student remains responsible for understanding and defending the requirements, code paths, tests, assumptions, tool findings, limitations and merge decisions during the oral defence.

## Evidence
- Assessed change Issue #1: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/issues/1
- Assessed change PR #2: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/pull/2
- Quality pipeline Issue #3: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/issues/3
- Quality pipeline PR #4: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/pull/4
- Security scanning / human triage: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/blob/main/docs/security-scanning.md
