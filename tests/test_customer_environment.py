import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CustomerEnvironmentTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "scripts").mkdir()
        shutil.copy(ROOT / "scripts/mossvale-customer.sh", self.root / "scripts")
        shutil.copy(ROOT / "scripts/container.sh", self.root / "scripts")
        shutil.copytree(
            ROOT / "customers/mossvale-supply",
            self.root / "customers/mossvale-supply",
        )
        self.working = self.root / "submissions/capstone/code/mossvale-supply"
        self.backups = self.root / "submissions/capstone/.mossvale-reset-backups"
        self.initializing = self.root / "submissions/capstone/.mossvale-initializing"
        self.log = self.root / "commands.log"
        bin_dir = self.root / "bin"
        bin_dir.mkdir()
        engine = """#!/bin/sh
printf '%s %s\\n' "$(basename "$0")" "$*" >> "$TEST_LOG"
case " $* " in
  *" down "*) [ "${FAIL_DOWN:-0}" != 1 ] ;;
esac
"""
        self.write_command(bin_dir / "podman", engine)
        self.write_command(bin_dir / "docker", engine)
        self.write_command(
            bin_dir / "sudo",
            '#!/bin/sh\nprintf \'sudo %s\\n\' "$*" >> "$TEST_LOG"\nexec "$@"\n',
        )
        self.write_command(
            bin_dir / "terraform",
            """#!/bin/sh
set -eu
printf 'terraform %s\\n' "$*" >> "$TEST_LOG"
for arg in "$@"; do
  case "$arg" in -chdir=*) dir=${arg#-chdir=} ;; esac
done
case " $* " in
  *" init "*) [ "${FAIL_INIT:-0}" != 1 ] ;;
  *" apply "*) : > "$dir/terraform.tfstate" ;;
esac
""",
        )
        self.env = os.environ.copy()
        self.env["PATH"] = f"{bin_dir}{os.pathsep}{self.env['PATH']}"
        self.env["TEST_LOG"] = str(self.log)
        self.env.pop("CONTAINER_ENGINE", None)

    def write_command(self, path, content):
        path.write_text(content)
        path.chmod(0o755)

    def run_customer(self, action, **extra_env):
        return subprocess.run(
            ["sh", str(self.root / "scripts/mossvale-customer.sh"), action],
            cwd=self.root,
            env={**self.env, **extra_env},
            text=True,
            capture_output=True,
        )

    def test_start_initializes_only_a_new_copy(self):
        self.assertEqual(self.run_customer("start").returncode, 0)
        state = self.working / "terraform/terraform.tfstate"
        self.assertTrue(state.exists())
        state.unlink()
        note = self.working / "learner-note.txt"
        note.write_text("learner work")

        self.assertEqual(self.run_customer("start").returncode, 0)
        self.assertEqual(note.read_text(), "learner work")
        self.assertFalse(state.exists())
        self.assertEqual(
            sum(line.startswith("terraform ") for line in self.log.read_text().splitlines()),
            2,
        )
        self.assertIn("podman compose ", self.log.read_text())

    def test_docker_fallback_keeps_terraform_unprivileged(self):
        result = self.run_customer("start", CONTAINER_ENGINE="docker")

        self.assertEqual(result.returncode, 0, result.stderr)
        commands = self.log.read_text()
        self.assertIn("sudo docker compose ", commands)
        self.assertNotIn("sudo terraform ", commands)

    def test_reset_preserves_edits_and_restores_the_baseline(self):
        self.assertEqual(self.run_customer("start").returncode, 0)
        (self.working / "learner-note.txt").write_text("learner work")

        result = self.run_customer("reset")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.working / "learner-note.txt").exists())
        saved = list(self.backups.glob("*/working-copy/learner-note.txt"))
        self.assertEqual(len(saved), 1)
        self.assertEqual(saved[0].read_text(), "learner work")
        self.assertTrue((self.working / "terraform/terraform.tfstate").exists())

    def test_reset_failure_keeps_the_working_copy(self):
        self.assertEqual(self.run_customer("start").returncode, 0)
        note = self.working / "learner-note.txt"
        note.write_text("learner work")

        self.assertNotEqual(self.run_customer("reset", FAIL_DOWN="1").returncode, 0)
        self.assertEqual(note.read_text(), "learner work")
        self.assertFalse(self.backups.exists())

    def test_failed_initialization_does_not_start_on_retry(self):
        self.assertNotEqual(self.run_customer("start", FAIL_INIT="1").returncode, 0)
        self.assertTrue(self.initializing.exists())

        result = self.run_customer("start")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Initialization did not finish", result.stderr)
        self.assertNotIn("podman ", self.log.read_text())

    def test_failed_copy_can_be_reset_without_losing_the_partial_copy(self):
        copy_command = self.root / "bin/cp"
        self.write_command(
            copy_command,
            """#!/bin/sh
mkdir -p "$3"
: > "$3/partial-copy"
exit 1
""",
        )

        self.assertNotEqual(self.run_customer("start").returncode, 0)
        self.assertTrue(self.initializing.exists())
        retry = self.run_customer("start")
        self.assertNotEqual(retry.returncode, 0)
        self.assertIn("Initialization did not finish", retry.stderr)
        self.assertFalse(self.log.exists())
        copy_command.unlink()

        result = self.run_customer("reset")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.initializing.exists())
        self.assertEqual(len(list(self.backups.glob("*/working-copy/partial-copy"))), 1)
        self.assertNotIn(" down ", self.log.read_text())


if __name__ == "__main__":
    unittest.main()
