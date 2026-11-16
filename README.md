# Terraform and Vault training

This repository contains the Terraform and Vault training guide.

## Prerequisites

Install these two tools:

- [Docker](https://docs.docker.com/engine/install/)
- [mise](https://mise.jdx.dev/installing-mise.html)

Docker Compose runs the local AWS emulator and PostgreSQL database. The Vault
slices ask you to build the Vault server separately. Mise installs the pinned
Terraform, Vault CLI, AWS CLI, Python, and MkDocs tools.

## Start the guide

From the repository root, install the pinned tools:

```bash
mise install
```

Start the supporting containers:

```bash
mise run start
```

Floci is the local AWS emulator used by slices 01–03 and answers on
`localhost:4566`. PostgreSQL supports the dynamic-secrets work in slice 06.
The compose file uses test-only database values and does not include Vault.

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
