#!/bin/sh
set -eu

docker compose up --detach

services=$(docker compose ps --services --status running)
for service in floci floci-ui postgres; do
    printf '%s\n' "$services" | grep -Fx "$service" >/dev/null ||
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
    if docker compose exec --no-TTY postgres pg_isready -U training -d training >/dev/null 2>&1; then
        exit 0
    fi
    sleep 1
    attempt=$((attempt + 1))
done

printf 'Service postgres did not become ready\n' >&2
exit 1
