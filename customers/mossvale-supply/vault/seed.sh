#!/bin/sh
set -eu

secrets=$(vault secrets list -format=json)
case "$secrets" in
  *'"customer/"'*) ;;
  *)
    vault secrets enable -path=customer kv-v2
    ;;
esac
vault kv put customer/database \
  username=mossvale_app \
  password=mossvale-db-password
