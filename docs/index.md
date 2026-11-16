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

## Tools

| Tool | Use | Limit to remember |
|---|---|---|
| [Floci](https://github.com/floci-io/floci) | Emulate AWS on `localhost:4566`. | It does not prove real AWS behavior, including IAM behavior. |
| Vault Community Edition | Run Vault locally in a container. | It does not include Enterprise features. |
| GitHub Actions | Run the CI slice on free runners. | A Vault service container ends with its job. |
| MkDocs Material | Build and serve this guide. | None. |

AWS is the cloud target. The ideas also apply to other clouds.

## Work pattern

There is no deadline. Complete a slice after its prerequisites are done.
You can stop and resume at any time. Your work lives in `submissions/`.
The guide uses one folder per slice. Start a new slice by copying the previous slice's work,
then extend it. Slices 01 and 04 start fresh because they begin separate tool tracks.

## Tracks

Every slice belongs to one or more tracks. Each slice page shows its track
tags at the top, and the navigation groups the slices by track.

<div class="grid cards" markdown>

-   :simple-terraform:{ .lg .middle .track-terraform } **Terraform**

    ---

    Slices 01–03. Workflow, state, drift, HCL, and modules against local AWS.

-   :simple-vault:{ .lg .middle .track-vault } **Vault**

    ---

    Slices 04–07. Dev mode, a real server, dynamic secrets, PKI, and transit.

-   :simple-hashicorp:{ .lg .middle .track-terraform } **Terraform + Vault**

    ---

    Slices 08–09. Both tools together, then CI/CD with no stored secrets.

-   :material-briefcase-outline:{ .lg .middle .track-advisory } **Advisory**

    ---

    Slice 10 and the capstone. Licensing, Enterprise fit, and client advice.

</div>

## Slice order

Complete the slices in this order the first time. Each row lists the required earlier work.

| # | Slice | Track | Prerequisites |
|---|---|---|---|
| 01 | Local AWS and Terraform workflow | :simple-terraform:{ .track-terraform } Terraform | none |
| 02 | State and drift | :simple-terraform:{ .track-terraform } Terraform | 01 |
| 03 | HCL and modules | :simple-terraform:{ .track-terraform } Terraform | 02 |
| 04 | Vault first contact | :simple-vault:{ .track-vault } Vault | none |
| 05 | Vault as a real server | :simple-vault:{ .track-vault } Vault | 04 |
| 06 | Dynamic secrets and rotation | :simple-vault:{ .track-vault } Vault | 05 |
| 07 | PKI and transit | :simple-vault:{ .track-vault } Vault | 06 |
| 08 | Terraform with Vault | :simple-hashicorp: Terraform + Vault | 03, 07 |
| 09 | CI/CD with no stored secrets | :simple-githubactions:{ .track-ci } Terraform + Vault, CI | 08 |
| 10 | Advisory: licensing and Enterprise | :material-briefcase-outline:{ .track-advisory } Advisory | 08 |
| Capstone | Client scenarios | :material-school-outline:{ .track-capstone } All tracks | 07, 09, 10 |

The capstone has a written diagnosis stage and a build stage.
The build stage uses the provided synthetic customer environment.

## Exams and reference

The slices loosely overlap with Terraform Associate and Vault Associate objectives.
The guide does not prepare you for either exam.
Read the official objectives later and record any gaps.

Read [How grading works](grading.md) before you start.
