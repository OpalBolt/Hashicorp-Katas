#!/bin/sh
set -eu

action=${1:-}
repo_root=$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)
baseline="$repo_root/customers/mossvale-supply"
dir="$repo_root/submissions/capstone/code/mossvale-supply"
backup_root="$repo_root/submissions/capstone/.mossvale-reset-backups"
project="mossvale-supply-$(id -u)"

if [ ! -d "$baseline" ]; then
  printf 'Customer baseline does not exist: %s\n' "$baseline" >&2
  exit 1
fi

if [ -e "$dir" ] && [ ! -d "$dir" ]; then
  printf 'Customer working copy is not a directory: %s\n' "$dir" >&2
  exit 1
fi

compose() {
  docker compose \
    --project-name "$project" \
    --project-directory "$dir" \
    -f "$dir/compose.yml" "$@"
}

copy_baseline() {
  mkdir -p "$(dirname "$dir")"
  cp -R "$baseline" "$dir"
  : > "$dir/.mossvale-initializing"
}

initialize_state() {
  terraform -chdir="$dir/terraform" init -input=false
  terraform -chdir="$dir/terraform" apply -input=false -auto-approve
  rm "$dir/.mossvale-initializing"
}

start() {
  if [ ! -e "$dir" ]; then
    copy_baseline
    initialize_state
  fi

  if [ -e "$dir/.mossvale-initializing" ]; then
    printf '%s\n' "Initialization did not finish. Run mise run customer-reset to preserve this copy and retry." >&2
    exit 1
  fi

  compose up --detach
}

reset() {
  if [ -e "$dir" ] || [ -L "$dir" ]; then
    compose down --volumes
    mkdir -p "$backup_root"
    backup=$(mktemp -d "$backup_root/reset-XXXXXXXX")
    mv "$dir" "$backup/working-copy"
    printf 'Previous working copy saved to %s\n' "$backup/working-copy"
  fi

  copy_baseline
  initialize_state
  compose up --detach
}

case "$action" in
  start)
    start
    ;;
  reset)
    reset
    ;;
  *)
    printf 'Usage: %s {start|reset}\n' "$0" >&2
    exit 2
    ;;
esac
