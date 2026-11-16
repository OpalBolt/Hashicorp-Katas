---
icon: simple/terraform
tags:
  - Terraform
---

# 02 — State and drift

## Why

Terraform state connects configuration to real resources. A lost state file can make a team lose track of ownership and recreate resources. A locked state can stop planned work until someone resolves the operation that holds the lock. State can contain secrets, so a leaked state file can expose client credentials. Parallel applies can race, overwrite state, or produce changes that no one reviewed.

Start this slice in a new folder: `submissions/02-state/`.
Copy the previous slice's `code/` folder into it and extend that work. The previous slice destroyed its resources, so recreate your local setup before these exercises.

Use Floci at `localhost:4566`. Use fictitious test values only. Keep the configuration and state that the next slice will need.

## Concepts

- state
- remote backend
- locking
- drift
- import
- moved blocks
- state commands

## Tasks

### Task 01 — Continue the previous slice

Copy the previous slice's code into `submissions/02-state/code/` and recreate its local resources in Floci. Extend the configuration in this new folder.

#### Constraints

- Work only in `submissions/02-state/code/`.
- Use Floci. Do not use a real AWS account or real credentials.
- Start from the previous slice's code. Do not copy a finished solution.
- Use fictitious values for names, tokens, and other test data.

#### Done when

- The copied configuration initializes successfully in the new folder.
- The resources from the previous slice exist in Floci again.
- The new folder has its own working state.
- The configuration remains ready for the state exercises that follow.

#### Evidence to produce

- The copied and extended configuration files.
- Initialization and apply output.
- A Floci check of the recreated resources.
- The working folder and state location.

### Task 02 — Move state to a remote backend

Move the working state to a remote backend provided by Floci. Keep the same managed resources.

#### Constraints

- Use a remote backend in the local Floci environment.
- Do not use a real cloud account or store real credentials.
- Migrate the existing state. Do not discard it and create a new empty state.
- Keep backend access restricted to the test setup.

#### Done when

- Terraform initializes with the remote backend.
- The existing resources remain tracked after migration.
- A remote state object exists in the backend.
- A state inspection proves that the remote state contains the managed resources.

#### Evidence to produce

- The backend configuration.
- Initialization and migration output.
- The remote backend object or a safe inspection of it.
- A state inspection that does not expose secret values.

### Task 03 — Observe state locking

Use two concurrent Terraform operations against the same remote state. Make the second operation encounter the lock held by the first.

#### Constraints

- Use the same working folder and remote state as Task 02.
- Do not unlock state while another operation is still running.
- Do not delete, edit, or replace the lock record by hand.
- Use only local Floci resources and fictitious values.

#### Done when

- One operation holds the remote state lock.
- A second operation reports that the state is locked.
- The first operation completes without corrupting state.
- A later state inspection succeeds after the lock clears.

#### Evidence to produce

- Output that identifies the lock holder or lock metadata.
- Output from the blocked operation.
- Completion output from the first operation.
- A post-lock state inspection.

### Task 04 — Create and repair drift

Change a managed resource directly in Floci, outside Terraform. Use Terraform to detect and reconcile the drift.

#### Constraints

- Change one meaningful, reversible attribute.
- Make the manual change only in Floci. Do not edit the state file.
- Do not use real client data.
- Record the manual change before Terraform checks the resource.

#### Done when

- A Terraform plan identifies the manual change.
- The plan shows the intended correction.
- Applying the plan restores the declared configuration.
- A Floci check confirms the corrected value.

#### Evidence to produce

- The recorded manual change.
- The plan that detects the drift.
- Apply output.
- A Floci check of the corrected resource.

### Task 05 — Import a hand-made resource

Create one supported resource directly in Floci. Add matching Terraform configuration and bring the existing resource under management.

#### Constraints

- Create the resource outside Terraform.
- Use a resource that the configured provider and Floci support.
- Do not delete and recreate the hand-made resource to claim the import.
- Use fictitious test values.

#### Done when

- The hand-made resource exists before Terraform manages it.
- Terraform state tracks that existing resource after the import.
- A plan does not propose creating a second copy.
- The configuration matches the imported resource closely enough for a clean follow-up plan.

#### Evidence to produce

- The hand-made resource and its identifier.
- The configuration added for it.
- Import output and a state inspection.
- The follow-up plan.

### Task 06 — Rename a resource without replacement

Rename one Terraform resource address while keeping the underlying Floci resource.

#### Constraints

- Rename a resource that Terraform already manages.
- Use the repository's Terraform version.
- Do not destroy the resource before or during the rename.
- Review the plan before applying it.

#### Done when

- The configuration uses the new resource address.
- The plan records an address move without destroy and create actions.
- Applying the change keeps the same Floci resource.
- State uses the new address after the apply.

#### Evidence to produce

- The configuration before and after the rename.
- The plan showing the address move.
- Apply output.
- A state and Floci check showing the same resource remains.

### Task 07 — Find a secret in state

Put a fictitious secret-like test value into a managed configuration, then find where Terraform stores it in state. Redact the value in all evidence.

#### Constraints

- Use a made-up value that has no access to a real system.
- Do not use real credentials, tokens, or personal data.
- Do not paste the secret into evidence, answers, logs, or commits.
- Keep access to the state and backend limited to the local test setup.

#### Done when

- You identify the state path or attribute that contains the test value.
- You show that marking a value sensitive does not remove it from state.
- Evidence contains only a redacted value.
- The final configuration and state remain usable for the next slice.

#### Evidence to produce

- The test configuration with the value redacted.
- A redacted state inspection that identifies the value's location.
- A short note about the access risk.
- A final check that the working state remains available.

## Explain

Answer these questions in `submissions/02-state/answers.md`.

### Explain 1

Why is Terraform state sensitive, even when a configuration marks an input as sensitive?

### Explain 2

How can a team rename a Terraform resource safely without replacing the real resource?

### Explain 3

What should a team do after someone changes a managed resource by hand?
