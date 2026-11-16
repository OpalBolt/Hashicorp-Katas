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

The reset task does not remove files from this directory.

The Compose project uses `127.0.0.1:18200` for Vault and
`127.0.0.1:15432` for PostgreSQL.
