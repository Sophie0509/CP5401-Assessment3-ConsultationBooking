# Appendix A — Generative AI Use Record

## Tool used
ChatGPT (OpenAI)

## Significant use
AI assistance was used to help draft the initial project structure, Python/Streamlit code, automated tests, GitHub Actions workflow, change-control records and documentation templates.

## Significant prompt examples
1. "Create a small Streamlit consultation booking application with Student and Staff roles, testable business rules, pytest tests and GitHub Actions evidence suitable for CP5401 Assessment 3."
2. "Add a controlled V1.1 FIFO waitlist change after a V1.0 baseline, including impact analysis, regression tests, review findings and CI evidence."

## Human verification required
The student must:
- read and understand all generated code;
- run the application locally and on the deployed Streamlit site;
- run the complete automated test suite;
- confirm each test against the documented requirements and business rules;
- review AI-generated tests for expected results, boundaries and failure paths;
- review and modify AI-generated output where needed;
- explain assumptions, review findings, risk classification and merge decision;
- be able to explain the code, tests, workflow and quality decisions during the oral defence.

## Assumptions checked for the assessed change
- Python list order is sufficient to represent FIFO order in this small in-memory assessment application.
- A waitlisted student is promoted only if the promotion does not violate overlap or capacity rules.
- Session-state/in-memory storage is acceptable for the demonstration scope; persistence is outside the assessed application scope.
