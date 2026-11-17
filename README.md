# Terraform and Vault training

This repository contains the Terraform and Vault training guide.

## Grade your work

Keep code and authored task artifacts in each slice's `code/` folder.
Save only transient run captures in `evidence/`. No evidence template is required.
See [How grading works](docs/grading.md) for capture examples and submission rules.

The harness-independent grader lives at `.agents/skills/grader/SKILL.md`.
In an AI harness with repository access, use this prompt:

```text
Read .agents/skills/grader/SKILL.md and follow it.
Grade the terraform track in submissions/terraform/.
```

Use `vault`, `terraform-vault`, or `adversary` for another track.
You can also name one slice or the capstone.
Harnesses that discover `.agents/skills/` can load `grader` directly.

## Prerequisites

Install these tools:

- [Podman](https://podman.io/docs/installation)
- [podman-compose](https://github.com/containers/podman-compose) 1.3.0 or later
- [mise](https://mise.jdx.dev/installing-mise.html)

Podman Compose runs the local AWS emulator, its web console, and the
PostgreSQL database. The Vault
slices ask you to build the Vault server separately. Mise installs the pinned
Terraform, Vault CLI, AWS CLI, Python, and MkDocs tools.
For Docker instead, see the [Docker fallback](docs/setup.md#docker-fallback).

## Start the guide

From the repository root, install the pinned tools:

```bash
mise install
```

Install and check the supporting services:

```bash
mise run setup
```

This starts and checks Floci, Floci UI, and PostgreSQL. It seeds no data.
Before you run Terraform or the AWS CLI against the local AWS target, set the
shell variables in the guide's [local setup](docs/setup.md) page.

Stop the containers and remove this project's container data:

```bash
mise run stop
```

## Capstone customer environment

The capstone includes a fictional Mossvale Supply environment with Terraform,
Vault, and PostgreSQL.

Start it with:

```bash
mise run customer-start
```

Reset its containers and runtime data with:

```bash
mise run customer-reset
```

The first start copies the tracked baseline to the working directory and
creates its initial local Terraform state. Later starts keep that working
copy unchanged. Reset moves the old working copy to the ignored
`submissions/capstone/.mossvale-reset-backups/` directory, restores a fresh
baseline, and starts it again.
If initialization fails, reset the environment to preserve the partial copy
and try again.

The customer Compose project uses loopback-only ports and a separate project
name for each local user.

Serve the guide locally:

```bash
mise run serve
```

Open the address shown by MkDocs in your browser.

Build the guide and check for broken links:

```bash
mise run build
```
