---
icon: material/briefcase-outline
tags:
  - Adversary
---

# Adversary 01 — Advisory: licensing and Enterprise

Prerequisite: [Terraform + Vault 01 — Terraform with Vault](../terraform-vault/01-terraform-vault.md).

## Why

Clients ask which Terraform and Vault option fits their situation, and
whether an Enterprise or hosted option is worth its cost over time. A useful
answer must account for licence terms, support, operations, staffing,
infrastructure, compliance, migration, and growth. This slice makes the
learner research current terms and turn them into questions, evidence, and
review material rather than making an unsupported product recommendation.

Start by copying `submissions/terraform-vault/01-terraform-vault/code/` into
`submissions/adversary/01-advisory/code/`. Keep the copied work separate from
your research and checklists. Save authored task artifacts as Markdown files
in `code/`. Use fictitious client details and redact credentials,
tokens, secret values, and private key material.

## Concepts

- Terraform licence terms
- Vault licence terms
- Community versus Enterprise
- namespaces
- replication
- Sentinel
- HSM support
- HCP and Terraform Cloud versus self-run

## Tasks

### Task 01 — Research current licence terms

Research the current Terraform and Vault licence terms, product options, and
published pricing or commercial guidance. Use official HashiCorp sources and
cite every material claim.

#### Constraints

- Work only in `submissions/adversary/01-advisory/`.
- Start from the copied code from Terraform + Vault 01. Do not modify it to create
  advisory conclusions.
- Use current official Terraform and Vault sources, including the source
  title, URL, publisher, and access date.
- Separate licence terms, product documentation, pricing, and support claims.
- Record uncertainty or missing public information instead of guessing.
- Use fictitious client details and do not include confidential commercial
  information.
- Do not research or compare products outside Terraform and Vault.

#### Done when

- The research names the current source for Terraform licence terms.
- The research names the current source for Vault licence terms.
- The research records the relevant Community and Enterprise distinctions
  without presenting an uncited conclusion.
- Pricing or cost claims identify the time period, currency, scope, and
  source, or are explicitly marked unavailable.
- Every material claim has an official citation and access date.

#### Evidence to produce

- A cited source register for the Terraform and Vault research.
- A redacted comparison of the terms and commercial facts found.
- A note listing open questions that require confirmation from HashiCorp or
  the client.

### Task 02 — Map Enterprise features to client problems

For a fictitious client, map each Enterprise feature in this slice to a real
client problem and identify the evidence needed before recommending it.

#### Constraints

- Continue from Task 01 and use only cited official Terraform or Vault
  sources for product claims.
- Include namespaces, replication, Sentinel, and HSM support in the mapping.
- Describe one concrete client problem and its affected users, systems, or
  controls for every feature.
- Distinguish a feature's capability from the client's reason to buy it.
- Record operational, migration, staffing, and ongoing cost questions where
  they affect the problem.
- Do not claim that Enterprise is required without evidence and client
  context.
- Keep all client names, systems, and values fictitious.

#### Done when

- Every named Enterprise feature has a distinct client problem mapped to it.
- Each mapping states the evidence that would confirm or reject the fit.
- The mapping records at least one operational or cost consequence for each
  feature.
- The source register supports the product statements in the mapping.
- The document identifies features that do not solve the fictitious client's
  stated problems.

#### Evidence to produce

- A redacted feature-to-problem mapping.
- Source citations attached to the relevant mappings.
- A short client-context record showing how each problem was established.

### Task 03 — Write a Terraform repository review checklist

Review a fictitious client Terraform repository and write a one-page
checklist that another adviser can use before discussing licensing, hosting,
support, or Enterprise value.

#### Constraints

- Continue from the research in Task 01.
- Keep the checklist to one page, excluding its source list.
- Write the checklist yourself. Do not copy a vendor checklist.
- Use review prompts that can be answered with repository evidence or a
  named client owner.
- Cover the repository's Terraform versions, providers, state, workflows,
  hosting model, support needs, security controls, growth, and cost drivers.
- Cite official sources for product or licence assertions.
- Do not include credentials, tokens, secret values, private keys, or real
  client data.

#### Done when

- The checklist is one page and consists of clear review prompts.
- Each prompt identifies the evidence or owner needed for a useful answer.
- The checklist exposes assumptions that could change the licensing or
  hosting recommendation.
- The checklist includes questions about recurring cost and operational
  ownership, not only initial licence price.
- A second person can use the checklist without an unwritten explanation.

#### Evidence to produce

- The one-page Terraform repository review checklist.
- A redacted record showing it was applied to the fictitious repository.
- The source list and unresolved questions produced during the review.

### Task 04 — Write a Vault setup review checklist

Review a fictitious client Vault setup and write a one-page checklist that
another adviser can use before discussing Community, Enterprise, or hosted
operation.

#### Constraints

- Continue from the research in Task 01 and the feature mapping in Task 02.
- Keep the checklist to one page, excluding its source list.
- Write the checklist yourself. Do not copy a vendor checklist.
- Use review prompts that can be answered with configuration evidence,
  operational records, or a named client owner.
- Cover tenancy boundaries, namespaces, replication, Sentinel, HSM needs,
  availability, upgrades, support, recovery, staffing, and cost drivers.
- Distinguish a client requirement from an available product capability.
- Do not include credentials, tokens, secret values, private keys, or real
  client data.

#### Done when

- The checklist is one page and consists of clear review prompts.
- Each prompt identifies the evidence or owner needed for a useful answer.
- The checklist tests the client's availability, security, compliance, and
  operational requirements.
- The checklist exposes assumptions that could change the Enterprise or
  hosting recommendation.
- A second person can use the checklist without an unwritten explanation.

#### Evidence to produce

- The one-page Vault setup review checklist.
- A redacted record showing it was applied to the fictitious setup.
- The source list and unresolved questions produced during the review.

## Explain

Answer these questions in `submissions/adversary/01-advisory/answers.md`.

### Explain 1

**Situation:** A client asks: "Should we stay on Community Terraform, or move to HCP Terraform or Terraform Enterprise?"

**Question:** Which questions do you ask before you recommend an option, and how does each answer change your recommendation?

**A solid answer covers:**

- At least four questions about the client's needs, such as team size, compliance, policy control, and operating capacity.
- How each answer moves the recommendation toward or away from an option.
- What the licence terms allow for the client's planned use.

### Explain 2

**Situation:** A client's security lead says: "We need Vault Enterprise for namespaces and replication."

**Question:** How do you test whether those features solve a real client problem, and when is the cost justified?

**A solid answer covers:**

- The client problem each feature would solve.
- Whether a Community setup or a design change could solve the same problem.
- The conditions under which the cost is justified.

### Explain 3

**Situation:** An old sales slide says a feature is included in a licence tier. You cannot find that claim in current official sources. The client meeting is tomorrow.

**Question:** What do you tell the client, and what do you record?

**A solid answer covers:**

- How you present a claim you cannot confirm.
- What you record: the source, its date, an owner, and the next check.
- How the unconfirmed claim affects the decision.
