# Capstone — Mossvale Supply written scenarios

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
