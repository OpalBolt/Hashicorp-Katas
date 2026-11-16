---
icon: simple/vault
tags:
  - Vault
---

# 04 — Vault first contact

## Why

Vault stores secrets outside application code and build configuration. This
reduces the chance that a password reaches source control, CI variables, logs,
or Terraform state. Vault also controls who can read a secret and records
when access should stop.

Start this slice in a new folder: `submissions/04-vault-first-contact/`.
Build the Vault dev-mode container yourself. Do not add a Vault server to the
repository Compose file. Use fictitious test values only, and redact tokens
from evidence.

## Concepts

- dev mode
- secrets engine
- KV versions
- token
- TTL
- revocation
- policy
- capabilities
- root token

## Tasks

### Task 01 — Start Vault in dev mode

Create a local Vault dev-mode setup in the new slice folder. Start the server
and confirm that a Vault client can reach it.

#### Constraints

- Work only in `submissions/04-vault-first-contact/`.
- Build the Vault container and its startup configuration yourself.
- Do not use the repository Compose file for the Vault server.
- Use dev mode for local learning only.
- Use fictitious test values.
- Do not commit an unredacted token.

#### Done when

- The new folder contains the files needed to start the Vault dev server.
- The server starts and stays healthy.
- A Vault client reaches the server.
- Evidence identifies the dev-mode server without exposing its token.

#### Evidence to produce

- The container and startup configuration.
- Server startup and health output.
- A redacted client check.

### Task 02 — Store and version a secret

Enable or use a KV secrets engine. Store a fictitious application secret, update
it, and inspect its version history.

#### Constraints

- Keep the work in the new slice folder.
- Use a KV engine, not a different secrets engine.
- Use a test path and fictitious values.
- Create at least two versions of the same secret.
- Do not put secret values, tokens, or client data in evidence.

#### Done when

- The KV engine is available at a documented mount.
- A test secret exists at a documented path.
- The path has at least two versions.
- The current version and an earlier version can be distinguished safely.
- Evidence redacts all secret values.

#### Evidence to produce

- The mount and test path.
- Redacted output for the current and earlier versions.
- Version metadata that shows the update.

### Task 03 — Limit a token to one read path

Write a policy that grants read access to one KV path. Create a non-root token
with that policy, then test both an allowed path and a different path.

#### Constraints

- Grant only the capability needed to read the selected path.
- Do not grant access to the whole mount.
- Use a non-root token for all access tests.
- Give the token a bounded TTL.
- Keep the root token out of files and evidence.
- Use fictitious test paths and values.

#### Done when

- The policy names exactly one allowed secret path.
- The test token has the policy and a bounded TTL.
- The token reads the allowed path.
- The same token cannot read a different path.
- Evidence shows both outcomes without exposing the token or secret value.

#### Evidence to produce

- The policy file with test paths only.
- Token metadata with the token value redacted.
- A successful allowed-path check.
- A denied different-path check.

### Task 04 — Revoke a token

Create a separate test token, prove that it works before revocation, revoke it,
and prove that Vault rejects it afterward.

#### Constraints

- Use a non-root token with a bounded TTL.
- Test the token before revocation.
- Revoke the exact test token after the first check.
- Test the same token after revocation.
- Do not use or disclose a real token.

#### Done when

- The test token works before revocation.
- Vault revokes the test token.
- The revoked token fails after revocation.
- Evidence identifies the token through redacted metadata only.

#### Evidence to produce

- Pre-revocation access output.
- Revocation output or token metadata.
- Post-revocation denial output.

## Explain

Answer these questions in `submissions/04-vault-first-contact/answers.md`.

### Explain 1

Why does Vault deny access by default when a policy does not grant a
capability?

### Explain 2

What is the difference between a Vault token and a secret?

### Explain 3

Why should a team avoid using the root token for daily work?
