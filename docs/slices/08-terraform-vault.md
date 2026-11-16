---
icon: simple/hashicorp
tags:
  - Terraform
  - Vault
---

# 08 — Terraform with Vault

## Why

Terraform and Vault each protect a different part of the workflow. The join
between them is where most secrets leak: a value read from Vault can move into
Terraform state, a saved plan, provider logs, or a managed resource. This
slice makes that boundary visible before you choose a safer hand-off.

Start by copying the Terraform work from
`submissions/03-modules/code/` into
`submissions/08-terraform-vault/code/terraform/`. Copy the Vault work from
`submissions/07-pki-transit/code/` into
`submissions/08-terraform-vault/code/vault/`. Keep the two tracks in separate
paths and extend them in this new folder. Use fictitious test values. Redact
credentials, tokens, secret values, and private key material from evidence.

## Concepts

- Vault provider
- data source versus ephemeral resource
- write-only argument
- where secrets land
- bootstrap token
- short-lived provider credentials

## Tasks

### Task 01 — Make a secret land in state

Use the copied Terraform and Vault work. Read a fictitious secret from Vault
with Terraform and pass its value into a managed resource. Inspect the plan
and state to find where the value is stored.

#### Constraints

- Work only in `submissions/08-terraform-vault/`.
- Keep Terraform code under `code/terraform/` and Vault code under `code/vault/`.
- Start from the copied work; do not replace either track with an unrelated
  example.
- Use a Vault data source and a managed resource that accepts the value.
- Use a fictitious secret with no access to a real system.
- Keep provider credentials outside the repository.
- Redact the value in plans, state inspections, logs, evidence, and answers.

#### Done when

- The copied Terraform and Vault configurations remain usable in their
  separate paths.
- Terraform reads the test secret from Vault.
- A managed resource receives the read value.
- A plan or state inspection identifies the state path or attribute containing
  the value, with the value redacted.
- The inspection shows that marking the value sensitive does not remove it
  from state.
- Evidence contains no secret, token, or provider credential.

#### Evidence to produce

- The redacted data-source and resource configuration.
- Redacted initialization and plan output.
- A redacted state inspection naming the exposed path or attribute.
- A short note explaining where the leak occurred.

### Task 02 — Keep a secret out of state and saved plans

Replace the state-exposing hand-off with a supported ephemeral resource or
write-only argument. Prove what is absent from state and from a saved plan,
then record the limits of the feature you selected.

#### Constraints

- Continue from Task 01 in `submissions/08-terraform-vault/`.
- Use a feature supported by the pinned Terraform and provider versions.
- The secret must still reach its intended destination during the operation.
- Do not claim that `sensitive` alone, redaction, or deleting a local file
  keeps a value out of state.
- Inspect both state and a saved plan without printing the secret value.
- Keep fictitious values and provider credentials outside the repository.

#### Done when

- The chosen ephemeral or write-only path is accepted by Terraform and the
  provider.
- The intended operation succeeds without exposing the value in state.
- A saved plan contains no copy of the value.
- The evidence identifies the state and plan checks used to prove absence.
- The evidence records at least one limitation of the chosen feature, such as
  provider support, lifecycle, or where the destination stores the value.
- Evidence contains no secret, token, or provider credential.

#### Evidence to produce

- The redacted configuration using the selected supported feature.
- Redacted apply or plan output showing the operation succeeded.
- Redacted state and saved-plan inspections proving absence.
- A short limitation note backed by the version or provider behavior tested.

### Task 03 — Manage Vault configuration with Terraform

Use Terraform to manage one Vault policy, one authentication method, and one
secrets mount. Keep the bootstrap path separate from the provider credentials
used for normal changes.

#### Constraints

- Work in the copied tracks under `submissions/08-terraform-vault/`.
- Manage the policy, auth method, and mount through Terraform resources.
- Use a least-privilege fictitious policy and a test-only mount.
- Use short-lived provider credentials for routine Terraform operations.
- Do not put an initial token, role credential, secret value, or private key
  in configuration, state, saved plans, or evidence.
- Review the plan before applying changes.
- Do not hand-edit objects that Terraform manages.

#### Done when

- The plan contains the policy, auth method, and mount under Terraform
  management.
- Applying the plan creates or updates all three objects in the test Vault.
- A Vault inspection confirms each object and its intended relationship.
- A follow-up plan does not try to recreate unchanged objects.
- The provider credential used for the apply is short-lived or bounded, and
  its handling is documented without revealing it.
- Evidence contains no credential, token, or secret value.

#### Evidence to produce

- Redacted Terraform resources and provider configuration.
- Redacted plan and apply output for the three objects.
- Redacted Vault inspections for the policy, auth method, and mount.
- A note identifying the provider credential lifetime and storage boundary.

### Task 04 — Write a safe first-token bootstrap

Write a short runbook for creating and handing off the first Vault token that
can run the Terraform configuration. Distinguish that bootstrap event from
later short-lived provider credentials, and state what happens if the
bootstrap credential is lost or exposed.

#### Constraints

- Base the runbook on the test server and Terraform ownership from this slice.
- Do not include a real command output, token, key share, secret, or
  credential value.
- Identify who performs bootstrap, where material is held temporarily, how it
  reaches the operator, and when it is revoked or replaced.
- Require least privilege for routine Terraform work.
- Include a recovery or rotation path for loss and exposure.
- Keep Vault bootstrap ownership distinct from Terraform-managed steady-state
  configuration.

#### Done when

- The runbook names a safe first-token creation and handoff sequence.
- It keeps bootstrap material outside the repository and ordinary plan/state
  artifacts.
- It explains how the first token is exchanged for bounded provider
  credentials.
- It identifies the owner for bootstrap, Terraform configuration, and Vault
  runtime operations.
- It describes what to do after loss or suspected exposure.
- A reviewer can follow the runbook without seeing any secret value.

#### Evidence to produce

- The redacted bootstrap runbook.
- A responsibility table or equivalent ownership record.
- A redacted review or test record showing the sequence was checked.
- A note describing the loss and exposure response.

## Explain

Answer these questions in `submissions/08-terraform-vault/answers.md`.

### Explain 1

Why is marking a value `sensitive` not enough to keep a Vault secret safe in
Terraform?

### Explain 2

Which Terraform feature can keep a supported secret hand-off out of state and
saved plans, and what are the limits of that protection?

### Explain 3

Who owns the Vault configuration code after Terraform manages a policy, auth
method, or mount, and how should that ownership affect manual changes?
