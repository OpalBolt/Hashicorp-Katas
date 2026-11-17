---
icon: simple/terraform
tags:
  - Terraform
---

# Terraform 03 — HCL and modules

## Why

Reusable, readable Terraform is easier for a client to review, change, and
inherit. Clear interfaces make ownership visible and reduce the risk that a
small environment change affects the wrong resources.

Start this slice in a new folder: `submissions/terraform/03-modules/`.
Copy `submissions/terraform/02-state/code/` into its `code/` folder and extend that work.
Keep the local Floci resources and remote state from the previous slice
working while you add isolated environment state.

Use Floci at `localhost:4566`. Use fictitious test values only. Keep the
configuration and state ready for the Terraform and Vault slice that follows.

## Concepts

- variables
- validation
- locals
- count versus for_each
- data sources
- modules
- environments
- test

## Tasks

### Task 01 — Build from a map

Copy the previous slice's code into `submissions/terraform/03-modules/code/`. Extend it
so one resource type is created from a map of environment-specific or
component-specific values.

#### Constraints

- Work only in `submissions/terraform/03-modules/code/`.
- Start from the previous slice's code. Do not copy a finished solution.
- Keep the existing Floci resources and remote state working.
- Use a map as the source for repeated resources. Do not duplicate one block
  for each map entry.
- Use only local Floci resources and fictitious values.

#### Done when

- The copied configuration initializes successfully in the new folder.
- The map describes at least two resources.
- Terraform plans and applies the resources derived from the map.
- The state and a Floci check agree about the resources that exist.

#### Evidence to produce

- The copied and extended configuration files.
- The map and the resource declaration that consumes it.
- Initialization, plan, and apply output.
- A Floci check and state inspection for the created resources.

### Task 02 — Validate inputs and select a repetition method

Add input validation and local values to the configuration. Use either
`count` or `for_each` where it fits, and record why that choice matches the
identity of the resources.

#### Constraints

- Keep the resources from Task 01 manageable.
- Validate at least one input at the module or root configuration boundary.
- Use locals for a repeated derived value instead of repeating its expression.
- Do not hide invalid test input by changing it before validation.
- Use fictitious values and keep the work local to Floci.

#### Done when

- A valid input produces a successful plan.
- An invalid input is rejected before resource creation.
- A local value is used by a resource or module input.
- The chosen repetition method keeps resource identity stable when one item
  changes.

#### Evidence to produce

- The variable declaration, validation rule, and local values.
- A successful check with valid input.
- A failed validation check with invalid input.
- A plan or state inspection showing the chosen resource addresses.
- A short note explaining the choice of `count` or `for_each`.

### Task 03 — Read an existing resource

Use a data source to read an existing resource or service in the local Floci
environment. Use the result in the configuration without taking ownership of
the existing object.

#### Constraints

- The object must exist before the data source reads it.
- Do not create the object with the resource block under test.
- Do not import the object into state for this task.
- Use a read-only data source supported by the configured provider and Floci.
- Use fictitious test values only.

#### Done when

- The data source reads the existing object successfully.
- A plan or output shows that the read value is available to configuration.
- Terraform does not plan to create or destroy the object read by the data
  source.
- The configuration uses the read value in a managed resource or module input.

#### Evidence to produce

- The data source configuration and the object it reads.
- Initialization and plan output for the read.
- A safe output or state inspection showing the consumed value without
  exposing secrets.
- A Floci check that distinguishes the existing object from managed objects.

### Task 04 — Turn the configuration into a module

Move the reusable resource logic into a child module with a small, clear
interface. Call the module twice with different inputs.

#### Constraints

- Keep provider configuration and environment-specific values outside the
  child module unless the provider requires otherwise.
- Define the module inputs and outputs explicitly.
- Do not duplicate the module's resource logic at the call sites.
- Use two distinct module instances with different valid inputs.
- Preserve the working local resources and remote state.

#### Done when

- Terraform initializes the root configuration and the child module.
- Both module instances appear in the plan with distinct addresses.
- Applying the configuration creates both module instances in Floci.
- A module output is consumed by the root configuration or recorded in state.
- A change to one module input does not require copying the module logic.

#### Evidence to produce

- The child module files and its input and output declarations.
- The root module calls and their distinct inputs.
- Initialization, plan, and apply output.
- State and Floci checks for both module instances.
- A safe inspection showing the module output was consumed.

### Task 05 — Isolate environment state

Represent at least two environments with separate state locations. Keep the
resources from the prior tasks available while proving that an environment
change cannot silently use the other environment's state.

#### Constraints

- Use separate state locations for the environments.
- Do not use one shared state file for both environments.
- Do not treat workspaces as the only production isolation boundary.
- Keep each environment's values explicit and reviewable.
- Use only local Floci resources and fictitious values.

#### Done when

- Each environment initializes against its own state location.
- A state inspection shows distinct managed resource addresses or values for
  the environments.
- A plan in one environment does not propose changes to the other
  environment's resources.
- The existing remote state and local Floci resources remain usable.

#### Evidence to produce

- The environment layout and state configuration.
- Initialization output for each environment.
- State inspections that identify the separate state locations without
  exposing secrets.
- Plans for both environments and a Floci check of their distinct resources.

### Task 06 — Test the module

Write one Terraform test for the child module. The test must check a useful
module behavior without relying on a real cloud account.

#### Constraints

- Keep the test with the module or its test configuration in
  `submissions/terraform/03-modules/code/`.
- Test a behavior introduced by the module, not only Terraform syntax.
- Use local provider behavior or supported test doubles.
- Do not use real credentials, client data, or a real cloud account.
- Keep the test repeatable and safe to run more than once.

#### Done when

- The Terraform test file is discovered by the repository's Terraform
  version.
- The test runs successfully against the module.
- At least one assertion checks a module result or contract.
- The test does not alter the other environment's state.

#### Evidence to produce

- The Terraform test file and the module behavior it checks.
- Test discovery and successful test output.
- The assertion result, with secrets and tokens redacted.
- A note identifying which environment state the test used.

## Explain

Answer these questions in `submissions/terraform/03-modules/answers.md`.

### Explain 1

When should a repeated Terraform resource use `count`, and when should it use
`for_each`?

### Explain 2

What do sensitive values protect in Terraform, and what do they not protect?

### Explain 3

Why are workspaces a risky boundary for production and development
environments?
