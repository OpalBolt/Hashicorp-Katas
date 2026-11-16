---
icon: simple/vault
tags:
  - Vault
---

# 07 — PKI and transit

## Why

Long-lived certificates increase the time available to an attacker after a
private key leaks. Certificate replacement also becomes costly when many
services share a long lifetime.

Applications that hold encryption keys can expose those keys through logs,
backups, memory, or a compromised host. Vault can perform encryption without
giving the application the key.

Start this slice by copying your `submissions/06-dynamic-secrets/code/` folder
to `submissions/07-pki-transit/code/`. Extend the copied work in the new
folder. Keep the Vault server work usable for the later integration slice. Use
fictitious test values. Redact keys, tokens, certificates, plaintext, and
secret values from evidence.

## Concepts

- root CA
- intermediate CA
- role
- certificate TTL
- revocation
- transit
- key rotation
- key versions
- response wrapping

## Tasks

### Task 01 — Build a root and intermediate CA

Create a root CA and an intermediate CA in the local Vault server. Use the
intermediate CA for service certificates.

#### Constraints

- Work only in `submissions/07-pki-transit/`.
- Extend the copied Vault server work from slice 06.
- Use a test-only root CA and intermediate CA.
- Keep the root CA separate from the issuing CA.
- Use fictitious names and values.
- Keep private keys, tokens, and certificates outside the repository.
- Redact keys, tokens, certificates, and secret values from evidence.

#### Done when

- The root CA exists and has identifiable test metadata.
- The intermediate CA exists and chains to the root CA.
- The intermediate CA can issue service certificates.
- The issuing configuration uses a bounded certificate lifetime.
- The root CA is not used as the issuing CA for service certificates.
- Evidence contains no private key or certificate value.

#### Evidence to produce

- Redacted root and intermediate CA metadata.
- Redacted chain relationship output.
- Redacted issuing configuration and lifetime metadata.
- A note that identifies where each private key is stored outside the repository.

### Task 02 — Issue a short-lived service certificate

Use the intermediate CA to issue a certificate for a fictitious service. Give
the certificate a short TTL and include the service identity it needs.

#### Constraints

- Use the intermediate CA from Task 01.
- Use a dedicated test role with a bounded TTL.
- Use a fictitious service name and test domain.
- Keep the private key outside the repository.
- Do not use a long-lived certificate to satisfy the task.
- Redact certificates, keys, tokens, and secret values from evidence.

#### Done when

- The role accepts the intended service identity.
- Vault issues a certificate from the intermediate CA.
- The certificate contains the intended subject or SAN.
- The certificate expiry shows a short lifetime.
- The certificate lifetime is shorter than the CA lifetime.
- Evidence contains no certificate or private key value.

#### Evidence to produce

- Redacted role metadata and TTL settings.
- Redacted issuance metadata.
- Certificate subject, issuer, SAN, and expiry with values minimized or masked.
- A redacted record of private-key handling.

### Task 03 — Verify the certificate chain

Verify that the service certificate chains through the intermediate CA to the
root CA. Check the service identity during verification.

#### Constraints

- Verify the certificate issued in Task 02.
- Use the complete test chain from the root and intermediate CAs.
- Check the intended service identity.
- Record a failed check when the chain or identity is wrong.
- Keep private keys, tokens, certificates, and secret values out of evidence.

#### Done when

- The complete chain verifies from the service certificate to the root CA.
- The identity check succeeds for the intended service.
- The verification identifies the intermediate issuer.
- A missing or incorrect chain or identity fails verification.
- Evidence proves the certificate chain check without exposing certificate data.

#### Evidence to produce

- Redacted successful chain-verification output.
- Redacted identity-verification output.
- A redacted failed verification result for an invalid chain or identity.
- Certificate and issuer metadata without certificate contents.

### Task 04 — Encrypt, rotate, and decrypt with transit

Use the transit engine to encrypt and decrypt a test value. Rotate the transit
key, then decrypt data created before the rotation.

#### Constraints

- Use a dedicated transit key and least-privilege test policy.
- Keep the transit key inside Vault.
- Do not give the application the transit key.
- Use a fictitious test value.
- Rotate the key through Vault.
- Test old ciphertext after rotation.
- Keep keys, tokens, plaintext, ciphertext contents, and secret values out of
  evidence.

#### Done when

- The application can encrypt the test value through transit.
- The application can decrypt the encrypted value through transit.
- Vault reports a new key version after rotation.
- New encryption uses the rotated key version.
- Ciphertext created before rotation still decrypts successfully.
- Evidence identifies both key versions without exposing key or value contents.

#### Evidence to produce

- Redacted transit policy and key metadata.
- Redacted pre-rotation encryption and decryption checks.
- Redacted rotation output showing key versions.
- A redacted check that old ciphertext still decrypts after rotation.
- A redacted check that new encryption uses the rotated version.

### Task 05 — Hand over a secret with response wrapping

Use response wrapping to hand a test secret to a separate recipient. Prove
that the recipient can unwrap it once and that the wrapping token has a
bounded lifetime.

#### Constraints

- Use a fictitious test secret.
- Set a short wrapping TTL.
- Deliver only the wrapped response to the recipient.
- Keep the wrapping token outside the repository and evidence.
- Do not expose the secret value in evidence.
- Test reuse or expiry behavior without resetting the result.

#### Done when

- Vault returns a wrapped response for the test secret.
- The recipient unwraps the response successfully.
- The wrapping token has a documented bounded TTL.
- The same wrapping token cannot unwrap the response a second time.
- Evidence contains no wrapping token or secret value.

#### Evidence to produce

- Redacted wrapped-response metadata and TTL.
- A redacted recipient unwrap result.
- A redacted second-use or expiry failure.
- A note describing how the wrapped response reached the recipient without
  exposing the token.

## Explain

Answer these questions in `submissions/07-pki-transit/answers.md`.

### Explain 1

Why should the root CA stay separate from the CA that issues service
certificates?

### Explain 2

What does transit let an application avoid storing?

### Explain 3

What does key rotation change for new and old ciphertext?
