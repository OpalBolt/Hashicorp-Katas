# Terraform and Vault training

This repository contains the Terraform and Vault training guide.

## Prerequisites

Install these two tools:

- [Docker](https://docs.docker.com/engine/install/)
- [mise](https://mise.jdx.dev/installing-mise.html)

Docker runs the local AWS emulator and Vault server. Mise installs the pinned
Terraform, Vault CLI, AWS CLI, Python, and MkDocs tools.

## Start the guide

From the repository root, install the pinned tools:

```bash
mise install
```

Serve the guide locally:

```bash
mise run serve
```

Open the address shown by MkDocs in your browser.

Build the guide and check for broken links:

```bash
mise run build
```
