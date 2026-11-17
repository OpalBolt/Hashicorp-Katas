#!/bin/sh
set -eu

case "${CONTAINER_ENGINE:-podman}" in
  podman)
    export PODMAN_COMPOSE_PROVIDER=podman-compose
    exec podman "$@"
    ;;
  docker)
    exec sudo docker "$@"
    ;;
  *)
    printf 'Unknown container engine: %s. Use podman or docker.\n' "$CONTAINER_ENGINE" >&2
    exit 2
    ;;
esac
