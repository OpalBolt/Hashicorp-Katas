# 05 — Vault as a real server

## Why

Dev mode hides the work that keeps a Vault server safe and recoverable. It
uses temporary storage and convenient startup settings. Operators must own
the seal process, storage recovery, authentication choices, audit trail,
server configuration, and TLS decision.

Start this slice by copying your `submissions/04-vault-first-contact/code/`
folder to `submissions/05-vault-server/code/`. Extend the copied work in the
new folder. Use fictitious test values. Keep unseal shares, credentials,
tokens, and snapshots out of evidence and commits.

## Concepts

- seal
- unseal
- key shares
- integrated storage
- snapshots
- auth methods
- AppRole
- audit devices
- server config
- TLS

## Tasks

### Task 01 — Run Vault from a server configuration

Replace the dev-mode setup with a Vault server that reads a configuration
file. Use integrated storage with data on a persistent local volume.

#### Constraints

- Work only in `submissions/05-vault-server/`.
- Start Vault outside the repository Compose file.
- Read the server settings from a configuration file.
- Use integrated storage and a persistent volume.
- Use a test listener and fictitious values.
- Do not commit keys, tokens, certificates, or storage data.
- Record the TLS choice and its local-learning limitation.

#### Done when

- The new folder contains the server configuration and startup files.
- Vault starts without dev mode.
- The server uses integrated storage.
- The data path survives container or process replacement.
- A client reaches the server.
- Evidence does not expose credentials or private key material.

#### Evidence to produce

- The configuration and startup files.
- Redacted startup and health output.
- The storage configuration and persistence check.
- A short note about the TLS choice.

### Task 02 — Initialize, unseal, and restart the server

Initialize the server, protect the key shares, unseal it, and restart it.
Before restarting, write a fictitious test secret to the persistent server
storage. Show that the server remains recoverable without using dev mode and
that the same secret is readable after recovery.

#### Constraints

- Use a test-only initialization.
- Choose more than one key share and a threshold that requires more than one share.
- Store shares and the initial token outside the repository.
- Write a fictitious test secret before the restart.
- Never place shares, tokens, or secret values in evidence.
- Restart the server without deleting its persistent storage.
- Do not use the root token for routine checks.

#### Done when

- Vault starts sealed before unseal.
- Initialization creates the configured key shares and threshold.
- The server becomes ready after the required unseal shares are supplied.
- A non-root check works after unseal.
- The server starts sealed after restart and becomes ready after unseal again.
- The same test secret is readable after restart and unseal.

#### Evidence to produce

- Redacted initialization metadata showing the share count and threshold.
- Sealed and unsealed health results.
- Redacted restart and recovery output.
- A post-restart check that identifies the retained test path without its value.

### Task 03 — Log in as a machine with AppRole

Enable AppRole for a test machine. Give the role only the policy it needs.
Log in with the role credentials and use the resulting token for one request.

#### Constraints

- Use a dedicated test policy and role.
- Grant only the required capability and path.
- Deliver the role ID and secret ID as separate inputs.
- Set bounded uses or a bounded lifetime for the secret ID and token.
- Do not store role credentials, tokens, or secret values in the repository.
- Test both the allowed request and a denied request.

#### Done when

- AppRole is enabled and the test role has the intended policy.
- The machine receives a token through an AppRole login.
- The token can use the allowed path.
- The token cannot use a different path.
- Evidence redacts the role ID, secret ID, token, and secret values.

#### Evidence to produce

- Redacted role and policy metadata.
- A successful machine login check.
- Allowed and denied request results with sensitive fields removed.
- The configured lifetime or use limits.

### Task 04 — Enable an audit device

Enable an audit device, make a request as yourself, and find that request in
the audit log. Identify the request without exposing secret values.

#### Constraints

- Use a test audit destination that the server can write.
- Make a request after the audit device is enabled.
- Search for your own request by a safe request detail, such as its path or time.
- Redact tokens, request data, response data, and secret values.
- Record what the server does when the audit destination cannot accept a record.

#### Done when

- The audit device is enabled and its status is visible.
- A known request creates an audit record.
- The record identifies the request and its result.
- Evidence contains no token, secret, request body, or response body.
- The failure behavior is documented from an observed test or server message.

#### Evidence to produce

- Redacted audit-device status.
- The redacted client request result.
- The matching redacted audit record.
- A redacted failure test or server log, plus the observed behavior.

### Task 05 — Snapshot and restore integrated storage

Create a disposable test record, take an integrated-storage snapshot, remove
or change the record, and restore the snapshot in a safe test instance.

#### Constraints

- Use only fictitious test data.
- Keep the snapshot outside the repository.
- Record the snapshot metadata without uploading its contents.
- Use a separate test instance or disposable data path for the restore.
- Do not overwrite the working server before the restore is proven.
- Keep credentials, tokens, and secret values out of evidence.

#### Done when

- A snapshot completes and has identifiable metadata.
- The test record changes or disappears after the snapshot.
- The snapshot restores into the safe test instance.
- The restored instance contains the earlier test record.
- The original server remains available until the restore check passes.

#### Evidence to produce

- Redacted snapshot completion and metadata.
- The pre-snapshot and changed-record checks without values.
- Restore output and the post-restore record check.
- The location and handling statement for the snapshot, without its contents.

## Explain

Answer these questions in `submissions/05-vault-server/answers.md`.

### Explain 1

Why does Vault start sealed, and what risk does unseal control reduce?

### Explain 2

How can AppRole reduce the need for a long-lived application secret, and
which credentials or delivery paths still need protection?

### Explain 3

What happens when an enabled audit device cannot write a request record, and
why must an operator decide how to handle that failure?
