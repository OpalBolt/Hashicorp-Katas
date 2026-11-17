#!/bin/sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)

container() {
    sh "$repo_root/scripts/container.sh" "$@"
}

container compose up --detach

containers=$(container compose ps -q)
services=
for id in $containers; do
    service=$(container inspect --format '{{.State.Running}} {{index .Config.Labels "com.docker.compose.service"}}' "$id")
    services="${services}
$service"
done
for service in floci floci-ui postgres; do
    printf '%s\n' "$services" | grep -Fx "true $service" >/dev/null ||
        { printf 'Service %s is not running\n' "$service" >&2; exit 1; }
done

check_http() {
    name=$1
    url=$2
    attempt=1
    while [ "$attempt" -le 30 ]; do
        if curl --silent --show-error --output /dev/null --connect-timeout 2 "$url"; then
            return 0
        fi
        sleep 1
        attempt=$((attempt + 1))
    done
    printf 'Service %s did not become ready at %s\n' "$name" "$url" >&2
    exit 1
}

check_http floci http://127.0.0.1:4566/
check_http floci-ui http://127.0.0.1:4500/

attempt=1
while [ "$attempt" -le 30 ]; do
    if container compose exec -T postgres pg_isready -U training -d training >/dev/null 2>&1; then
        exit 0
    fi
    sleep 1
    attempt=$((attempt + 1))
done

printf 'Service postgres did not become ready\n' >&2
exit 1
