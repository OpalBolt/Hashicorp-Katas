---
icon: material/rocket-launch-outline
---

# Local setup

The guide uses Docker, mise, and a local AWS target. The target is safe to
repeat, but it does not prove real AWS behavior.

## Install the tools

Install:

- [Docker](https://docs.docker.com/engine/install/)
- [mise](https://mise.jdx.dev/installing-mise.html)

From the repository root, install the pinned Terraform, Vault, AWS CLI,
Python, and MkDocs tools:

```bash
mise install
```

## Start the local services

Run:

```bash
mise run setup
```

This starts and checks Floci on `localhost:4566`, Floci UI on
<http://localhost:4500>, and PostgreSQL on `localhost:5432`. It creates no
AWS resources and seeds no data.

Stop the services and remove their local PostgreSQL data with:

```bash
mise run stop
```

## Configure the AWS tools

With a real AWS account, you would create an access key and export it. Floci
accepts any key, so use these test values in each shell that runs Terraform
or the AWS CLI:

```bash
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
export AWS_REGION=us-east-1
export AWS_ENDPOINT_URL=http://localhost:4566
```

`AWS_ENDPOINT_URL` sends the AWS provider and AWS CLI to Floci. For example:

```bash
aws s3 ls
```

This lists buckets in Floci, not in AWS. You can browse resources in the
[Floci UI](http://localhost:4500).

!!! warning "Use these values only for Floci"
    Close the shell or unset these variables before working with a real AWS
    account. Never put a real access key in `submissions/`.

These variables cover credentials and the endpoint only. Terraform workflow
asks you to pin the provider and decide which other provider settings the
local AWS target needs. Use the
[Floci Terraform guide](https://floci.io/floci/getting-started/terraform/)
when a resource or the S3 backend does not behave as expected.
