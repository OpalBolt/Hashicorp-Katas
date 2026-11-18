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
    blank1["???"]
    blank2["???"]
    blank3["???"]

    %% ===== DO NOT TOUCH: fixed nodes =====
    auth["Auth method"]
    policy["Policy"]
    mount["Mount"]

    %% ===== DO NOT TOUCH: request flow =====
    blank1 -->|"authenticate"| auth
    auth -->|"issues"| blank2
    blank1 -->|"sends request"| policy
    policy -->|"allows path"| mount
    mount --> blank3

    %% ===== DO NOT TOUCH: styling =====
    classDef todo stroke-dasharray: 5 5,stroke-width:2px
    class blank1,blank2,blank3 todo
```
