---
icon: simple/vault
tags:
  - Vault
---

# Vault 01 — Vault first contact

## Why

Vault stores secrets outside application code and build configuration. This
reduces the chance that a password reaches source control, CI variables, logs,
or Terraform state. Vault also controls who can read a secret and records
when access should stop.

Prerequisite: [Vault 00 — Foundations](00-foundations.md).

Start this slice in a new folder: `submissions/vault/01-vault-first-contact/`.
Build the Vault dev-mode container yourself. Do not add a Vault server to the
repository Compose file. Use fictitious test values only, and redact tokens
from evidence.

## Concepts

- dev mode
- KV versions
- TTL
- revocation
- capabilities
- root token

## Tasks

### Task 01 — Start Vault in dev mode

Create a local Vault dev-mode setup in the new slice folder. Start the server
and confirm that a Vault client can reach it.

#### Constraints

- Work only in `submissions/vault/01-vault-first-contact/`.
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
Look for KV version 2, which supports the version history this task needs.
One fictional application's configuration path is enough. Reuse it for the later access tests.

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

Answer these questions in `submissions/vault/01-vault-first-contact/answers.md`.

### Explain 1

**Situation:** A token has one policy. That policy grants `read` on `secret/data/app` and nothing else. The token tries to write to `secret/data/app` and to read `secret/data/billing`.

**Question:** What happens to each request, and why is Vault designed this way?

**A solid answer covers:**

- The result of each request, and the reason.
- What "deny by default" means for paths the policy does not name.
- Why deny by default is safer than allow by default when someone adds new secrets.

### Explain 2

**Situation:** You find that a token has leaked. You revoke it.

**Question:** What does revocation stop, and what can it not undo?

**A solid answer covers:**

- What happens to later requests that use the revoked token.
- What happens to secrets the attacker already read.
- What else you must do after you revoke the token.

### Explain 3

**Situation:** A small team keeps the root token from their first setup in a password manager. They use it for daily work because it is easier.

**Question:** What risks does this create, and what should the team do instead?

**A solid answer covers:**

- What the root token can do and how long it lasts.
- What the audit log can and cannot tell the team about who did what.
- A safer way to do daily work, and when root access is still needed.
