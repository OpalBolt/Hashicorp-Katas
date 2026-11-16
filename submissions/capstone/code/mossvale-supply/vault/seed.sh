#!/bin/sh
set -eu

vault secrets enable -path=customer kv-v2 >/dev/null 2>&1 || true
vault kv put customer/database \
  username=mossvale_app \
  password=mossvale-db-password
