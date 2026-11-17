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

Complete the [local setup](setup.md) before the Terraform slices. It covers
Docker, the local AWS target, test credentials, and `mise run setup`.

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

    Terraform 01–03. Workflow, state, drift, HCL, and modules against local AWS.

-   :simple-vault:{ .lg .middle .track-vault } **Vault**

    ---

    Vault 01–04. Dev mode, a real server, dynamic secrets, PKI, and transit.

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
| Terraform 01 | Terraform workflow | :simple-terraform:{ .track-terraform } Terraform | Local setup |
| Terraform 02 | State and drift | :simple-terraform:{ .track-terraform } Terraform | Terraform 01 |
| Terraform 03 | HCL and modules | :simple-terraform:{ .track-terraform } Terraform | Terraform 02 |
| Vault 01 | Vault first contact | :simple-vault:{ .track-vault } Vault | none |
| Vault 02 | Vault as a real server | :simple-vault:{ .track-vault } Vault | Vault 01 |
| Vault 03 | Dynamic secrets and rotation | :simple-vault:{ .track-vault } Vault | Vault 02 |
| Vault 04 | PKI and transit | :simple-vault:{ .track-vault } Vault | Vault 03 |
| Terraform + Vault 01 | Terraform with Vault | :simple-hashicorp: Terraform + Vault | Terraform 03, Vault 04 |
| Terraform + Vault 02 | CI/CD with no stored secrets | :simple-githubactions:{ .track-ci } Terraform + Vault, CI | Terraform + Vault 01 |
| Adversary 01 | Advisory: licensing and Enterprise | :material-briefcase-outline:{ .track-advisory } Adversary | Terraform + Vault 01 |
| Capstone | Client scenarios | :material-school-outline:{ .track-capstone } All tracks | Vault 04, Terraform + Vault 02, Adversary 01 |

The capstone has a written diagnosis stage and a build stage.
The build stage uses the provided synthetic customer environment.

## Exams and reference

The slices loosely overlap with Terraform Associate and Vault Associate objectives.
The guide does not prepare you for either exam.
Read the official objectives later and record any gaps.

Read [How grading works](grading.md) before you start.
