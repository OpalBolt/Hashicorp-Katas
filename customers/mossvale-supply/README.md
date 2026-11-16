# Mossvale Supply

Mossvale Supply distributes warehouse and retail supplies across the
Midwest. Its platform team runs a small service with a PostgreSQL database and
a local Vault instance for development and test work.

Start the environment from the repository root:

```bash
mise run customer-start
```

Reset the customer containers and runtime data:

```bash
mise run customer-reset
```

The first start creates the working copy and its initial local Terraform
state. Later starts keep learner edits. Reset preserves the previous working
copy under the ignored `submissions/capstone/.mossvale-reset-backups/`
directory, restores a fresh baseline, and starts it again.

The Compose project uses `127.0.0.1:18200` for Vault and
`127.0.0.1:15432` for PostgreSQL.
