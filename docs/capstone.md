---
icon: material/school-outline
tags:
  - Capstone
  - Terraform
  - Vault
  - CI
  - Adversary
---

# Capstone — Mossvale Supply written scenarios

Prerequisites: [Vault 04 — PKI and transit](slices/vault/04-pki-transit.md),
[Terraform + Vault 02 — CI/CD with no stored secrets](slices/terraform-vault/02-ci.md),
and [Adversary 01 — Advisory: licensing and Enterprise](slices/adversary/01-advisory.md).

## Why

The capstone asks you to advise one fictional customer across Terraform,
Vault, CI, and product decisions. Start with written diagnoses. Do not build
anything until you have recorded what you think is happening, what you
recommend, the order of work, and why.

The later build stage uses a matching synthetic Mossvale Supply environment.
These scenarios describe its problems without giving you the fixes.

Save your answers in `submissions/capstone/answers.md`. Keep the same
per-slice layout used elsewhere in this guide:

```text
submissions/
  capstone/
    code/
    evidence/
      task-01.md
      task-02.md
      task-03.md
      task-04.md
    answers.md
```

The `code/` folder belongs to the later build stage. Do not add the synthetic
environment or build-stage solutions while completing these written scenarios.

## Concepts

- Terraform state and ownership
- Terraform structure and interfaces
- Vault operation and recovery
- secret handling and short-lived access
- CI trust and review boundaries
- licensing, hosting, and Enterprise decisions
- diagnosis, evidence, sequencing, and risk

## Tasks

### Task 01 — Diagnose Terraform ownership and structure

Mossvale Supply has a small platform team and separate development and
production accounts. Both environments were first created from one Terraform
directory. The state file is now stored beside the configuration in the
repository, and two engineers sometimes run changes from their laptops.

After a refactor, a plan proposes replacing resources that the team believes
already exist. A second engineer reports that a change made for development
also appears in the production plan. The repository has repeated resource
blocks with slightly different names, and a new team member cannot tell which
values are inputs, which are derived values, or which resources belong to
each environment. The team has not yet destroyed anything, but it cannot
explain which state owns each resource.

Write a diagnosis and recommendation for Mossvale Supply. State the order in
which the team should investigate and change the setup, and give the reason
for each step. Identify the checks that should happen before and after each
state or configuration change.

#### Done when

- The answer separates symptoms, likely causes, and facts that still need
  verification.
- The recommendation addresses both state ownership and configuration
  structure without treating a refactor as proof that resources are safe.
- The work is ordered to preserve resource ownership and avoid accidental
  replacement or cross-environment changes.
- Each major step has a reason tied to risk, reviewability, or team
  operation.
- The answer names evidence that would confirm the diagnosis and a safe
  stopping point if the evidence disagrees.

### Task 02 — Diagnose Vault operation and secret exposure

Mossvale Supply runs a test Vault server for a service that needs database
access. The server was started for convenience and loses its data when the
container is replaced. Operators use one powerful credential for setup and
routine checks. A database password is also passed through Terraform, and
the team has found secret-looking values in local state and command output.

The service still works, but nobody can show who changed a secret, how the
server would be recovered after a restart, or how access would be removed
when a job ends. The team wants a diagnosis that works for the local training
environment and clearly identifies which conclusions would require a real
client Vault.

Write a diagnosis and recommendation for Mossvale Supply. State the order of
operational, access, and secret-handling work, and explain why that order
reduces risk. Distinguish temporary test material from credentials that must
not become repository or routine-operator secrets.

#### Done when

- The answer distinguishes availability, seal or recovery, authentication,
  auditability, and secret-lifecycle symptoms.
- The recommendation separates bootstrap access from routine access and
  explains the boundary between Vault and Terraform state.
- The order includes a way to validate recovery and access removal without
  destroying the only working test setup.
- The answer identifies what evidence may be recorded safely and what must
  be redacted or kept outside the repository.
- The answer states which local observations do not prove production Vault
  behavior and what the client would still need to confirm.

### Task 03 — Diagnose CI trust and review boundaries

Mossvale Supply has a public Terraform repository. A pull request workflow
formats and plans changes, but a later step can also apply them. The same
workflow uses a long-lived Vault or cloud credential stored in repository
settings. Its permissions are broad because the original author wanted to
avoid authentication failures.

A recent log contains a Terraform diagnostic with more detail than expected.
The team cannot show that apply waits for a human review, that a job from an
unexpected branch is rejected, or that a failed authentication attempt could
not read the test secret. The workflow uses third-party actions, but the
review record does not show why their selected versions are trusted.

Write a diagnosis and recommendation for Mossvale Supply. State the order of
changes to planning, authentication, permissions, approval, and log review.
Give reasons for the order and identify tests that demonstrate both the
allowed path and the rejected path.

#### Done when

- The answer identifies separate trust boundaries for pull requests, apply,
  repository identity, Vault access, and workflow logs.
- The recommendation removes the need for a long-lived routine credential
  without assuming that masking a value is access control.
- The order keeps a reviewable plan and a recoverable test path while CI
  changes are made.
- The answer specifies least-privilege and branch or repository restriction
  checks, including what a rejected job must not receive.
- The answer names evidence for action pinning, permissions, approval, and
  redacted logs without asking the learner to expose token contents.

### Task 04 — Diagnose licensing and Enterprise fit

Mossvale Supply asks whether it should buy Terraform or Vault Enterprise
before expanding from one platform team to several. The company mentions
team separation, disaster recovery, policy guardrails, hardware-backed key
protection, support, and a hosted option, but has not stated which are
mandatory controls, how many operators it will staff, or what downtime and
recovery targets it needs.

The current local training setup uses Community-compatible components. The
customer has received conflicting informal advice about which features
require a paid product and how much operation would cost. Some advice is
based on old web pages, and no one has recorded the source date or separated
licence terms from product capability and support.

Write a diagnosis and recommendation for Mossvale Supply. State the order of
questions, evidence gathering, source checking, and decision review. Explain
why a feature request alone is not enough to recommend Enterprise or a
hosted service, and identify what the local build can and cannot demonstrate.

#### Done when

- The answer separates client requirements from product capabilities,
  licence terms, hosting choices, support, and operating cost.
- The recommendation treats namespaces, replication, policy guardrails, and
  hardware-backed protection as questions to verify rather than automatic
  reasons to buy.
- The order gathers current official sources and client evidence before
  making a commercial recommendation.
- Each major recommendation names the evidence or owner needed to confirm
  fit, cost, migration impact, and ongoing operations.
- The answer preserves a Community-compatible local build and records which
  Enterprise or hosted claims remain untested or uncertain.

### Stage 2 — Build

Answer the Explain questions at the end of this page before you start stage 2.
Now build the recommendations you wrote in stage 1. Work only in a copy of
the synthetic customer environment:

```text
customers/mossvale-supply/                 immutable baseline
submissions/capstone/code/mossvale-supply/ your working copy
```

Use the customer start and reset tasks in `customers/mossvale-supply/README.md`.
Never edit the baseline. Keep evidence in
`submissions/capstone/evidence/task-05.md` through `task-08.md`, and keep
your build-stage answers in `submissions/capstone/answers.md`.

Record before and after results. Redact passwords, tokens, and other secret
values. If a check fails, keep the failure and explain what it means. Do not
claim that a local result proves behavior in a hosted service or Enterprise
product.

### Task 05 — Build the Terraform recommendation

Implement the recommendation you wrote for Task 01 in your working copy.
Your change must make ownership and environment boundaries clear without
assuming that a refactor makes existing resources safe.

#### Constraints

- Preserve the immutable baseline and work only in the working copy.
- Keep development and production distinguishable in configuration and state.
- Do not add real credentials or secret values to the repository.
- Stop before any destructive action if your evidence does not explain the
  proposed ownership or replacement.

#### Done when

- Before and after plan output shows how your change affects each environment.
- State and configuration evidence identifies which setup owns each resource.
- The configuration makes inputs, derived values, and environment-specific
  resources easy to review.
- A check shows that a development change does not silently alter production.
- Your evidence records any remaining uncertainty and the safe stopping point.

#### Evidence to produce

Record the commands, redacted plan output, relevant state or configuration
excerpts, and the before-and-after comparison in `evidence/task-05.md`.

#### Explain

- What did you change, and which part of your written recommendation did it
  implement?
- Which evidence proves that ownership and environment boundaries improved?
- What did you leave unchanged, and why?
- What risk remains if the team applies this setup outside the local copy?

**Concept pointer:** Terraform state ownership.

### Task 06 — Build the Vault recommendation

Implement the recommendation you wrote for Task 02 in your working copy.
Keep the local service usable while you improve its operation, access
boundary, and secret handling.

#### Constraints

- Use temporary training values only. Do not add real credentials to files,
  state, output, or evidence.
- Keep a working recovery path while you test changes.
- Test access removal without destroying the only working test setup.
- Separate observations supported by the local environment from claims that
  need a client Vault.

#### Done when

- Evidence shows how the service behaves across the recovery event relevant to
  your recommendation.
- The routine access path differs from bootstrap access in the way your
  recommendation requires.
- A secret-handling check shows that the changed path does not expose secret
  values through configuration, state, or command output.
- An access-removal check shows what happens after temporary access ends.
- The evidence identifies which Vault behaviors remain untested locally.

#### Evidence to produce

Record redacted before and after status, recovery, access, and secret-handling
results in `evidence/task-06.md`. Keep raw secret values outside the
repository.

#### Explain

- What changed, and why did you choose that order?
- Which result proves that the service can recover without relying on one
  operator credential?
- What did you choose not to change, and why?
- What would a client still need to verify before using this design in
  production?

**Concept pointer:** Vault secret lifecycle.

### Task 07 — Build the CI trust recommendation

Implement the recommendation you wrote for Task 03 in the working copy's
workflow. Preserve a reviewable plan and make the allowed and rejected paths
observable without exposing credentials.

#### Constraints

- Do not add token contents or long-lived routine credentials to the
  repository.
- Keep plan and apply within the trust boundaries in your written
  recommendation.
- Test both an allowed change and a rejected branch or repository path.
- Review every third-party action version you change or retain.

#### Done when

- The workflow separates planning from the apply decision in a way that a
  reviewer can verify.
- The allowed path receives only the permissions and access it needs.
- The rejected path receives no protected secret or privileged operation.
- Authentication does not depend on the long-lived routine credential you
  diagnosed, or the evidence explains the remaining exception.
- Evidence records action versions, permission settings, review behavior, and
  redacted logs.

#### Evidence to produce

Record before and after workflow excerpts, allowed and rejected path results,
permission checks, and redacted log output in `evidence/task-07.md`.

#### Explain

- What changed at each trust boundary, and why did you change it in that
  order?
- How do the tests prove both access and rejection?
- What did you choose not to change, and why?
- What risk remains if a reviewer, action, or repository setting changes?

**Concept pointer:** CI trust boundaries.

### Task 08 — Build the Enterprise-fit recommendation

Implement the Community-compatible part of the recommendation you wrote for
Task 04 in the working copy. Use the build to record what the local setup can
prove and what requires current client or vendor evidence.

#### Constraints

- Keep the local build compatible with the Community components supplied here.
- Do not present an Enterprise or hosted feature as locally implemented when
  it is not available in this environment.
- Record source dates and owners for claims that need later verification.
- Do not make a commercial recommendation from a feature name alone.

#### Done when

- The working copy demonstrates the local controls that your recommendation
  says the Community setup can support.
- A decision record separates client requirements, product capability, license,
  hosting, support, and operating cost.
- Each untested Enterprise or hosted claim has an owner, source to check, and
  decision impact.
- The record states what evidence would change the recommendation.
- You state what you chose not to change in the local build and why.

#### Evidence to produce

Record the local before and after result, the decision record, dated official
sources, and unresolved questions in `evidence/task-08.md`. Do not copy
license text or secret values into the submission.

#### Explain

- What did you build locally, and how does it support your written
  recommendation?
- Which requirement remains unproven, and what evidence would prove it?
- What did you choose not to change, and why?
- How would staffing, recovery targets, or support requirements change your
  recommendation?

**Concept pointer:** Product fit evidence.

## Explain

Answer these questions in `submissions/capstone/answers.md` after the four
scenario responses.

### Explain 1

How should a consultant distinguish a symptom, a root-cause hypothesis, and
evidence before recommending a Terraform or Vault change?

### Explain 2

Why should the order of remediation be part of a customer recommendation,
rather than a list of independent technical improvements?

### Explain 3

How should a consultant present an Enterprise or hosted-product
recommendation when current official sources or client requirements are
incomplete?
