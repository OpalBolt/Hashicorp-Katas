---
icon: simple/vault
tags:
  - Vault
---

# Vault 00 — Diagram

This is the submission file for Task 01 in
[Vault 00 — Foundations](00-foundations.md). Run `mise run serve`, open this
page in the local site, and edit the Mermaid source below. MkDocs renders
your changes as you save the file.

The site shows this file from `submissions/vault/00-foundations/diagram.md`.

```mermaid
flowchart LR
    %% ===== YOU EDIT: replace each ??? with a label (keep the quotes) =====
    client["???"]
    token["???"]
    secret["???"]

    %% ===== DO NOT TOUCH: fixed nodes =====
    auth["Auth method"]
    policy["Policy"]
    mount["Mount"]

    %% ===== DO NOT TOUCH: request flow =====
    client -->|"authenticate"| auth
    auth -->|"issues"| token
    client -->|"sends request with token"| policy
    policy -->|"allows path"| mount
    mount --> secret

    %% ===== DO NOT TOUCH: styling (dashed = you fill in) =====
    classDef todo stroke-dasharray: 5 5,stroke-width:2px
    class client,token,secret todo
```
