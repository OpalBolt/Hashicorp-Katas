---
icon: material/home-outline
---

# Terraform and Vault training

This guide helps you build hands-on Terraform and Vault skills for consulting work.
It gives you goals, reasons, constraints, and checks. It does not give you solutions.

## Who this is for

- You know Docker and have some CI/CD experience.
- You have used Terraform before, but not in depth.
- You are new to Vault.
- Your clients already use HashiCorp products. You need hands-on skill to give useful advice.

AWS is the cloud target. The ideas also apply to other clouds.

## Start here

Start with Terraform 00. It needs only Terraform and no Docker, AWS, or Floci.
Complete the [local setup](setup.md) before Terraform 01 and the later slices.
It covers Docker, the local AWS target, test credentials, and `mise run setup`.

## Work pattern

There is no deadline. Complete a slice after its prerequisites are done.
You can stop and resume at any time. Your work lives in `submissions/`.
The guide uses one folder per slice. Start a new slice by copying the previous slice's work,
then extend it. Terraform 01 and Vault 01 start fresh because they begin separate tool tracks.

## Tracks

Every slice belongs to one or more tracks. Each slice page shows its track
tags at the top, and the navigation groups the slices by track.

<div class="grid cards" markdown>

-   :simple-terraform:{ .lg .middle .track-terraform } **Terraform**

    ---

    Terraform 00–03. Block types, then workflow, state, drift, HCL, and modules.
    Later slices use local AWS.

-   :simple-vault:{ .lg .middle .track-vault } **Vault**

    ---

    Vault 00–04. Foundations, dev mode, a real server, dynamic secrets, PKI, and transit.

-   :simple-hashicorp:{ .lg .middle .track-terraform } **Terraform + Vault**

    ---

    Terraform + Vault 01–02. Both tools together, then CI/CD with no stored secrets.

-   :material-briefcase-outline:{ .lg .middle .track-advisory } **Adversary**

    ---

    Adversary 01 and the capstone. Licensing, Enterprise fit, and client advice.

</div>

## Recommended topic order

Complete the topics in this order the first time. Each row lists the required earlier work.

| # | Slice | Topic | Prerequisites |
|---|---|---|---|
| [Terraform 00 — Block types](slices/terraform/00-block-types.md) | Block types | :simple-terraform:{ .track-terraform } Terraform | [Terraform tool](setup.md#install-the-tools) |
| [Terraform 01 — Terraform workflow](slices/terraform/01-workflow.md) | Terraform workflow | :simple-terraform:{ .track-terraform } Terraform | [Terraform 00](slices/terraform/00-block-types.md), [local setup](setup.md) |
| [Terraform 02 — State and drift](slices/terraform/02-state.md) | State and drift | :simple-terraform:{ .track-terraform } Terraform | [Terraform 01](slices/terraform/01-workflow.md) |
| [Terraform 03 — HCL and modules](slices/terraform/03-modules.md) | HCL and modules | :simple-terraform:{ .track-terraform } Terraform | [Terraform 02](slices/terraform/02-state.md) |
| [Vault 00 — Foundations](slices/vault/00-foundations.md) | Foundations | :simple-vault:{ .track-vault } Vault | None |
| [Vault 01 — Vault first contact](slices/vault/01-vault-first-contact.md) | Vault first contact | :simple-vault:{ .track-vault } Vault | [Vault 00](slices/vault/00-foundations.md) |
| [Vault 02 — Vault as a real server](slices/vault/02-vault-server.md) | Vault as a real server | :simple-vault:{ .track-vault } Vault | [Vault 01](slices/vault/01-vault-first-contact.md) |
| [Vault 03 — Dynamic secrets and rotation](slices/vault/03-dynamic-secrets.md) | Dynamic secrets and rotation | :simple-vault:{ .track-vault } Vault | [Vault 02](slices/vault/02-vault-server.md) |
| [Vault 04 — PKI and transit](slices/vault/04-pki-transit.md) | PKI and transit | :simple-vault:{ .track-vault } Vault | [Vault 03](slices/vault/03-dynamic-secrets.md) |
| [Terraform + Vault 01 — Terraform with Vault](slices/terraform-vault/01-terraform-vault.md) | Terraform with Vault | :simple-hashicorp: Terraform + Vault | [Terraform 03](slices/terraform/03-modules.md), [Vault 04](slices/vault/04-pki-transit.md) |
| [Terraform + Vault 02 — CI/CD with no stored secrets](slices/terraform-vault/02-ci.md) | CI/CD with no stored secrets | :simple-githubactions:{ .track-ci } Terraform + Vault, CI | [Terraform + Vault 01](slices/terraform-vault/01-terraform-vault.md) |
| [Adversary 01 — Advisory: licensing and Enterprise](slices/adversary/01-advisory.md) | Advisory: licensing and Enterprise | :material-briefcase-outline:{ .track-advisory } Adversary | [Terraform + Vault 01](slices/terraform-vault/01-terraform-vault.md) |
| [Capstone — Client scenarios](capstone.md) | Client scenarios | :material-school-outline:{ .track-capstone } All tracks | [Vault 04](slices/vault/04-pki-transit.md), [Terraform + Vault 02](slices/terraform-vault/02-ci.md), [Adversary 01](slices/adversary/01-advisory.md) |

The capstone has a written diagnosis stage and a build stage.
The build stage uses the provided synthetic customer environment.

## Exams and reference

The slices loosely overlap with Terraform Associate and Vault Associate objectives.
The guide does not prepare you for either exam.
Read the official objectives later and record any gaps.

Read [How grading works](grading.md) before you start.
