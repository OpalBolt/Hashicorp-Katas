# Terraform and Vault training

This guide takes you from "played with Terraform, new to Vault" to a consultant who can advise existing HashiCorp customers and also build what you advise.

You do the work. The guide gives you goals, the reason for each goal, and tests for success. It does not give you the answers.

## Who this is for

- You know Docker and have some CI/CD experience.
- You have used Terraform before, but not deeply.
- You are new to Vault.
- Your clients are existing HashiCorp customers, so most work is advice. Good advice needs hands-on skill, so you still build everything.

## Tools

| Tool | Use | Limit to remember |
|---|---|---|
| [Floci](https://github.com/floci-io/floci) | Local AWS emulator on `localhost:4566`. Free, MIT licence. | It is an emulator. It does not enforce IAM like real AWS. Some services are missing or approximate. |
| Vault Community Edition | Run it from the `hashicorp/vault` image. Free to run. | No Enterprise features. You must still learn what they are. |
| GitHub Actions, public repo | Free runners. Run Floci and Vault as service containers. | A Vault inside a job dies with the job. |
| MkDocs Material | Build this site: `pip install mkdocs-material`, then `mkdocs serve`. | None. |

AWS is the cloud target because it is the largest. The ideas move to Azure and GCP.

## Pace

No deadline. Each slice stands alone once its listed prerequisites are done. Stop and resume any time. Your progress lives in `submissions/`.

## Slices

Do them in order the first time. Slices 01 to 03 are Terraform. Slices 04 to 06 are Vault. Slices 07 and 08 join them. Slices 09 and 10 are the advisory layer.

| # | Slice | Needs |
|---|---|---|
| 01 | Local AWS and Terraform workflow | none |
| 02 | State and drift | 01 |
| 03 | HCL and modules | 02 |
| 04 | Vault first contact | none |
| 05 | Vault as a real server | 04 |
| 06 | Dynamic secrets, PKI, transit | 05 |
| 07 | Terraform with Vault | 03, 06 |
| 08 | CI/CD with no stored secrets | 07 |
| 09 | Advisory: licences, forks, Enterprise | 07 |
| 10 | Capstone: client scenarios | all |

## Exams

Terraform Associate and Vault Associate objectives overlap with these slices. This guide does not aim at the exams. When you finish, read the official objective lists and note any gaps.

See [How grading works](grading.md) before you start.
