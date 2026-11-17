import os
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SetupTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.bin = self.root / "bin"
        self.bin.mkdir()
        self.log = self.root / "commands.log"
        engine = """#!/bin/sh
printf '%s %s\\n' "$(basename "$0")" "$*" >> "$TEST_LOG"
if [ "$(basename "$0")" = podman ] && [ "$1" = compose ]; then
  printf 'provider %s\\n' "${PODMAN_COMPOSE_PROVIDER:-unset}" >> "$TEST_LOG"
fi
case "$*" in
  "compose ps -q")
    if [ "${MISSING_POSTGRES:-0}" = 1 ]; then
      printf 'floci-id\\nfloci-ui-id\\n'
    else
      printf 'floci-id\\nfloci-ui-id\\npostgres-id\\n'
    fi
    ;;
  inspect*)
    [ "${FAIL_INSPECT:-0}" != 1 ] || exit 1
    for arg do id=$arg; done
    case "$id" in
      floci-id) printf 'true floci\\n' ;;
      floci-ui-id) printf 'true floci-ui\\n' ;;
      postgres-id) printf '%s postgres\\n' "${POSTGRES_RUNNING:-true}" ;;
    esac
    ;;
  "compose exec -T postgres pg_isready -U training -d training") exit "${FAIL_POSTGRES:-0}" ;;
esac
"""
        self.write_command("podman", engine)
        self.write_command("docker", engine)
        self.write_command("sudo", "#!/bin/sh\nprintf 'sudo %s\\n' \"$*\" >> \"$TEST_LOG\"\nexec \"$@\"\n")
        self.write_command("curl", "#!/bin/sh\nprintf 'curl %s\\n' \"$*\" >> \"$TEST_LOG\"\n")
        self.env = {
            **os.environ,
            "PATH": f"{self.bin}{os.pathsep}{os.environ['PATH']}",
            "TEST_LOG": str(self.log),
        }
        self.env.pop("CONTAINER_ENGINE", None)

    def write_command(self, name, content):
        path = self.bin / name
        path.write_text(content)
        path.chmod(0o755)

    def run_setup(self, **extra_env):
        return subprocess.run(
            ["sh", str(ROOT / "scripts/setup.sh")],
            cwd=ROOT,
            env={**self.env, **extra_env},
            text=True,
            capture_output=True,
        )

    def test_setup_starts_and_checks_all_services_without_seeding(self):
        result = self.run_setup()

        self.assertEqual(result.returncode, 0, result.stderr)
        commands = self.log.read_text()
        self.assertIn("podman compose up --detach", commands)
        self.assertIn("podman compose exec -T postgres pg_isready", commands)
        self.assertIn("provider podman-compose", commands)
        self.assertNotIn("docker ", commands)
        self.assertNotIn("seed", commands.lower())

    def test_setup_reports_a_missing_service(self):
        result = self.run_setup(MISSING_POSTGRES="1")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Service postgres is not running", result.stderr)

    def test_setup_reports_a_stopped_service(self):
        result = self.run_setup(POSTGRES_RUNNING="false")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Service postgres is not running", result.stderr)

    def test_setup_propagates_inspection_failure(self):
        result = self.run_setup(FAIL_INSPECT="1")

        self.assertNotEqual(result.returncode, 0)

    def test_docker_fallback_uses_sudo(self):
        result = self.run_setup(CONTAINER_ENGINE="docker")

        self.assertEqual(result.returncode, 0, result.stderr)
        commands = self.log.read_text()
        self.assertIn("sudo docker compose up --detach", commands)
        self.assertIn("sudo docker inspect", commands)
        self.assertNotIn("podman ", commands)

    def test_unknown_engine_fails_without_starting_services(self):
        result = self.run_setup(CONTAINER_ENGINE="other")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Unknown container engine", result.stderr)
        self.assertFalse(self.log.exists())


if __name__ == "__main__":
    unittest.main()
