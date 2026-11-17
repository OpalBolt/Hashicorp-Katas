---
icon: simple/vault
tags:
  - Vault
---

# Vault 03 — Dynamic secrets and rotation

Prerequisite: [Vault 02 — Vault as a real server](02-vault-server.md).

## Why

Static database passwords remain useful to anyone who finds them. A short-lived
credential limits the time and access an attacker gets. Vault can create a
database user for each request, track its lease, and revoke it when the work
ends.

Start this slice by copying your `submissions/vault/02-vault-server/code/` folder to
`submissions/vault/03-dynamic-secrets/code/`. Extend the copied work in the new
folder. Keep the Vault server work from the previous slice. Use fictitious test
values. Redact credentials, tokens, passwords, and secret values from evidence.

## Concepts

- lease
- renewal
- revocation
- max TTL
- database secrets engine
- dynamic role
- static role
- rotation

## Tasks

### Task 01 — Request database credentials on demand

Connect the Vault container to the PostgreSQL `postgres` service. Configure a
database secrets engine and a dynamic role for a test database. Request
credentials on demand twice.

#### Constraints

- Work only in `submissions/vault/03-dynamic-secrets/`.
- Extend the copied Vault server work.
- Use the repository PostgreSQL service as the test database.
- Make Vault and PostgreSQL reachable on one Docker network.
- Use a database secrets engine and a dynamic role.
- Set a bounded lease duration and max TTL.
- Use fictitious database names, roles, and values.
- Keep credentials and tokens outside the repository.
- Redact usernames, passwords, tokens, and secret values from evidence.

#### Done when

- Vault can reach the PostgreSQL service.
- The database secrets engine has a documented test mount.
- The dynamic role has a bounded lease and max TTL.
- The first request returns usable temporary credentials.
- The second request returns usable temporary credentials.
- The two requests have different database usernames or identities.
- Both credentials work only within their lease limits.
- Evidence contains no credential or secret value.

#### Evidence to produce

- Redacted database connection and role configuration.
- Redacted output for both credential requests.
- Lease metadata that shows separate requests and bounded lifetimes.
- A redacted check that each credential can access the test database.

### Task 02 — Revoke one lease and inspect the database

Use the two credentials from Task 01. Prove that each request created a
separate database user. Revoke one lease and prove that its database user no
longer works while the other user remains separate.

#### Constraints

- Use only the temporary credentials from Task 01.
- Identify users through safe metadata, not passwords or tokens.
- Test both users before revocation.
- Revoke exactly one lease.
- Test the revoked user after revocation.
- Check the other user separately after revocation.
- Do not delete the database or reset its data to hide a failure.
- Redact credentials, tokens, connection strings, and secret values.

#### Done when

- The database shows two separate users created by the two requests.
- Both temporary users work before revocation.
- Vault reports the selected lease as revoked.
- The revoked user's database access fails afterward.
- The other temporary user remains distinct and its result is recorded.
- Evidence shows the lease-to-user relationship without secret values.

#### Evidence to produce

- A redacted database user listing before revocation.
- Redacted pre-revocation checks for both users.
- Redacted lease revocation output.
- Redacted post-revocation checks for both users.
- A short statement that explains which user the revoked lease created.

### Task 03 — Rotate a static database credential

Create a static role for a test database account. Request its credential, rotate
the static credential through Vault, and prove that the old credential stops
working.

#### Constraints

- Use a static role that maps to one test database account.
- Use a separate test account from the dynamic users.
- Set a bounded rotation period for the static role.
- Record the old credential only outside the repository.
- Rotate the credential through Vault.
- Test the old credential after rotation.
- Test the new credential after rotation.
- Redact both credentials, tokens, and secret values.

#### Done when

- Vault returns the static role credential before rotation.
- The old credential works before rotation.
- Vault reports a completed rotation.
- The old credential fails after rotation.
- The new credential works after rotation.
- Evidence identifies the static role without exposing its credentials.

#### Evidence to produce

- Redacted static-role configuration and metadata.
- A redacted pre-rotation access check.
- Redacted rotation output.
- Redacted checks that show old access fails and new access succeeds.

## Explain

Answer these questions in `submissions/vault/03-dynamic-secrets/answers.md`.

### Explain 1

Why can a short lease reduce risk more than a strong long-lived password?

### Explain 2

What happens to a dynamic database credential when its lease reaches its end,
and how does renewal change that result?

### Explain 3

What risk does credential rotation leave unchanged?
