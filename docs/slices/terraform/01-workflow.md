---
icon: simple/terraform
tags:
  - Terraform
---

# Terraform 01 — Terraform workflow

Prerequisites: [Terraform 00 — Block types](00-block-types.md) and [local setup](../../setup.md).

## Why

Clients need infrastructure changes that they can review before they make them.
The Terraform workflow shows the proposed change, applies only the intended change, and leaves a record of what exists.
You will use a local AWS target so that you can repeat the workflow without creating cloud resources.

Start this slice in a new folder: `submissions/terraform/01-workflow/`.

Use the local AWS target at `localhost:4566`. Set the shell variables in
[Local setup](../../setup.md) first.
Write all Terraform configuration yourself.

## Concepts

- providers
- plan
- apply
- destroy
- version pinning
- emulator limits

## Tasks

### Task 01 — Configure a local target

Create a Terraform configuration in `submissions/terraform/01-workflow/code/`.
Point its AWS provider at the local AWS target.
Choose at least two AWS resources that the local AWS target supports and manage them together.

#### Constraints

- Keep Terraform configuration in `submissions/terraform/01-workflow/code/`.
- Use the local AWS endpoint. Do not use a real AWS account.
- Do not add real cloud credentials or copy a finished configuration.
- Pin the AWS provider to a chosen version.

#### Done when

- Terraform initializes with the chosen provider version.
- A plan shows the resources that you chose for creation.
- An apply creates both resources in the local AWS target.
- The Terraform state and a local AWS check agree about the resources that exist.

#### Evidence to produce

- The configuration files and provider version constraint.
- Initialization output.
- The plan output before creation.
- Apply output and a check of the resources in the local AWS target.

### Task 02 — Change one resource through the workflow

Change one meaningful attribute of a managed resource.
Use the plan to inspect the proposed change before you apply it.

#### Constraints

- Start with the applied configuration from Task 01.
- Keep the change local and reversible.
- Do not replace the change with an unrelated refactor.
- Record the planned action before applying it.

#### Done when

- The plan shows the intended change and no unexpected resource changes.
- The apply completes against the local AWS target.
- A check of Terraform state or the local AWS target shows the new value.
- You can explain why the plan showed that action.

#### Evidence to produce

- The changed configuration.
- The plan output before the apply.
- Apply output.
- A check that shows the changed value.

### Task 03 — Remove the local resources

Destroy the resources from the same working folder and state used in the earlier tasks.

#### Constraints

- Destroy only the resources created for this slice.
- Keep the state until Terraform completes the destroy operation.
- Do not use a real AWS account.

#### Done when

- Terraform reports that the managed resources were destroyed.
- The state no longer tracks those resources.
- A local AWS check shows that the resources no longer exist.
- Your evidence identifies the working folder and state used.

#### Evidence to produce

- Destroy output.
- The resulting state inspection.
- A local AWS check that shows the resources are absent.

### Task 04 — Find an emulator limit

Find one AWS behavior that a successful local emulator run cannot prove about real AWS.
Use emulator documentation, AWS documentation, or a focused local observation to support your finding.

#### Constraints

- Do not access a real AWS account or use real credentials.
- Choose a behavior that matters to a client decision.
- Cite the source of your finding.
- Separate what the local emulator demonstrated from what remains unverified.

#### Done when

- You name one behavior that the emulator does not prove.
- You cite a source for the limitation or the real AWS behavior.
- You explain the risk of treating a local result as proof of real AWS behavior.
- You state one check that would still be needed before production use.

#### Evidence to produce

- A short written finding in `code/task-04-finding.md`.
- The source link or local observation that supports it.
- The distinction between the local result and the unverified real-world result.

## Explain

Answer these questions in `submissions/terraform/01-workflow/answers.md`.

### Explain 1

Why does Terraform have a plan phase instead of applying every configuration change immediately?

### Explain 2

Why should a team pin Terraform provider versions?

### Explain 3

What does a successful local emulator run fail to prove about real AWS?
