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
        self.write_command(
            "docker",
            """#!/bin/sh
printf 'docker %s\\n' "$*" >> "$TEST_LOG"
case "$*" in
  "compose ps --services --status running")
    if [ "${MISSING_POSTGRES:-0}" = 1 ]; then
      printf 'floci\\nfloci-ui\\n'
    else
      printf 'floci\\nfloci-ui\\npostgres\\n'
    fi
    ;;
  "compose exec --no-TTY postgres pg_isready -U training -d training") exit "${FAIL_POSTGRES:-0}" ;;
esac
""",
        )
        self.write_command("curl", "#!/bin/sh\nprintf 'curl %s\\n' \"$*\" >> \"$TEST_LOG\"\n")
        self.env = {
            **os.environ,
            "PATH": f"{self.bin}{os.pathsep}{os.environ['PATH']}",
            "TEST_LOG": str(self.log),
        }

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
        self.assertIn("docker compose up --detach", commands)
        self.assertIn("docker compose exec --no-TTY postgres pg_isready", commands)
        self.assertNotIn("seed", commands.lower())

    def test_setup_reports_a_missing_service(self):
        result = self.run_setup(MISSING_POSTGRES="1")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Service postgres is not running", result.stderr)


if __name__ == "__main__":
    unittest.main()
