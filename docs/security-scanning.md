# Static Analysis, Security Testing and Dependency Scanning

## Purpose

The quality pipeline uses automated tools before merge, followed by human triage. A tool warning is not treated as automatically correct and a green tool result is not treated as automatic approval.

## Automated checks

| Check | Tool | Purpose |
|---|---|---|
| Static analysis | Ruff | Detect code-quality errors and suspicious/unused constructs. |
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

High-risk authentication/authorization/security findings must block merge until resolved or explicitly approved by an appropriate specialist. Medium-risk business-logic findings require focused tests. Low-risk non-executable/documentation issues may use normal review.

## Current evidence

The security-gate workflow was added after the V1.1 application release to align the repository's automated quality evidence with the Week 9 / assessment guidance. It does not change application behaviour.

The final scan results and any findings/dispositions are recorded after the GitHub Actions run on the quality/security-gates pull request.
