#!/bin/sh
set -eu

action=${1:-}
repo_root=$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)
baseline="$repo_root/customers/mossvale-supply"
dir="$repo_root/submissions/capstone/code/mossvale-supply"
backup_root="$repo_root/submissions/capstone/.mossvale-reset-backups"
initializing="$repo_root/submissions/capstone/.mossvale-initializing"
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
  sh "$repo_root/scripts/container.sh" compose \
    --project-name "$project" \
    -f "$dir/compose.yml" "$@"
}

copy_baseline() {
  mkdir -p "$(dirname "$dir")"
  : > "$initializing"
  cp -R "$baseline" "$dir"
}

initialize_state() {
  terraform -chdir="$dir/terraform" init -input=false
  terraform -chdir="$dir/terraform" apply -input=false -auto-approve
  rm "$initializing"
}

start() {
  if [ -e "$initializing" ] || [ -e "$dir/.mossvale-initializing" ]; then
    printf '%s\n' "Initialization did not finish. Run mise run customer-reset to preserve this copy and retry." >&2
    exit 1
  fi

  if [ ! -e "$dir" ]; then
    copy_baseline
    initialize_state
  fi

  compose up --detach
}

reset() {
  if [ -e "$dir" ] || [ -L "$dir" ]; then
    if [ ! -e "$initializing" ] && [ ! -e "$dir/.mossvale-initializing" ]; then
      compose down --volumes
    fi
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
