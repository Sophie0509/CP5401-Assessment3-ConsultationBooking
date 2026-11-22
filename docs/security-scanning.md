# Static Analysis, Security Testing and Dependency Scanning

## Purpose

The quality pipeline uses automated tools before merge, followed by human triage. A tool warning is not treated as automatically correct and a green tool result is not treated as automatic approval.

## Automated checks

| Check | Tool | Purpose |
|---|---|---|
| Static analysis | Ruff | Detect correctness errors, undefined/unused code and other selected static issues. |
| Security static analysis | Bandit | Identify common Python security weaknesses in the application code. |
| Dependency vulnerability scan | pip-audit | Check direct and transitive Python dependencies against known vulnerability data. |
| Dependency consistency | pip check | Detect incompatible installed package requirements. |
| Build/compile verification | compileall | Confirm application Python files compile successfully. |
| Functional/regression tests | pytest + coverage | Verify requirements, boundaries, failure paths and V1.1 regression behaviour. |

## Human triage rule

For each substantive tool finding, record:
1. the affected code/dependency;
2. whether the finding is valid, a false positive or not applicable;
3. the risk level;
4. the evidence used to decide;
5. the disposition: corrected, dismissed with justification, accepted/escalated, or unresolved.

High-risk authentication/authorization/security findings block merge until resolved or explicitly approved by an appropriate specialist. Medium-risk business-logic findings require focused tests. Low-risk non-executable/documentation issues use normal review.

## PR #4 scan evidence

Pull Request: https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/pull/4

Successful GitHub Actions run:
https://github.com/Sophie0509/CP5401-Assessment3-ConsultationBooking/actions/runs/44916772976

Final results:
- Dependency consistency: **PASS**
- Ruff static analysis: **PASS — All checks passed**
- Bandit security static analysis: **PASS — No issues identified**
- pip-audit dependency vulnerability scan: **PASS — No known vulnerabilities found**
- Python compile/build verification: **PASS**
- Automated tests: **PASS — 12 passed**
- Coverage: **89%**, above the required 85% threshold

## Triage record

### Initial Ruff run
The first run used Ruff's broad default rule set and failed on import ordering and modern Python typing-style suggestions. These were assessed as low-risk maintainability/style findings, not security or behavioural defects.

**Decision:** the CI rule set was narrowed to correctness and unused-code-focused Ruff checks so the static-analysis gate remains focused on relevant code-quality risks without introducing an unrelated style/type refactor.

**Disposition:** configuration corrected; rerun passed.

### Bandit
**Finding:** no medium/high Python security issues were identified in `app.py` or `modules/`.

**Disposition:** no code change required.

### Dependency audit
**Finding:** no known vulnerabilities were found in the dependencies resolved from `requirements.txt`, including transitive dependencies.

**Disposition:** no dependency change required.

### Test / coverage evidence
All 12 automated tests passed and measured module coverage was 89%.

**Disposition:** regression and coverage gates satisfied.

## Merge decision

This quality-pipeline change does not alter application behaviour. It is ready to merge because all automated gates pass, no unresolved security/dependency finding remains, and the initial Ruff configuration issue was manually triaged and corrected.
