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

## Slice order

Complete the slices in this order the first time. Each row lists the required earlier work.

| # | Slice | Prerequisites |
|---|---|---|
| 01 | Local AWS and Terraform workflow | none |
| 02 | State and drift | 01 |
| 03 | HCL and modules | 02 |
| 04 | Vault first contact | none |
| 05 | Vault as a real server | 04 |
| 06 | Dynamic secrets and rotation | 05 |
| 07 | PKI and transit | 06 |
| 08 | Terraform with Vault | 03, 07 |
| 09 | CI/CD with no stored secrets | 08 |
| 10 | Advisory: licensing and Enterprise | 08 |
| Capstone | Client scenarios | 07, 09, 10 |

The capstone has a written diagnosis stage and a build stage.
The build stage uses the provided synthetic customer environment.

## Exams and reference

The slices loosely overlap with Terraform Associate and Vault Associate objectives.
The guide does not prepare you for either exam.
Read the official objectives later and record any gaps.

Read [How grading works](grading.md) before you start.
