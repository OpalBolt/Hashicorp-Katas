from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


class GitignoreTests(unittest.TestCase):
    def ignored_paths(self, paths):
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", "--stdin"],
            cwd=ROOT,
            input="\n".join(paths) + "\n",
            text=True,
            capture_output=True,
        )
        self.assertIn(result.returncode, (0, 1), result.stderr)
        return set(result.stdout.splitlines())

    def test_runtime_files_are_ignored_across_tracks(self):
        paths = {
            f"{folder}/{artifact}"
            for folder in (
                ".",
                "submissions/terraform/01-workflow/code",
                "submissions/terraform-vault/01-terraform-vault/code/terraform",
                "customers/mossvale-supply/terraform",
            )
            for artifact in (
                ".terraform/providers/provider",
                ".terraform/modules/modules.json",
                "terraform.tfstate",
                "terraform.tfstate.backup",
                "terraform.tfstate.d/development/terraform.tfstate",
                ".terraform.tfstate.lock.info",
                "review.tfplan",
                "tfplan",
                "tfplan.json",
                "plan.out",
                "crash.log",
                "crash.123.log",
            )
        }
        self.assertEqual(self.ignored_paths(paths), paths)

    def test_local_values_are_ignored_without_hiding_templates(self):
        ignored = {
            ".env",
            ".env.local",
            "submissions/terraform/01-workflow/code/training.tfvars",
            "submissions/terraform/01-workflow/code/training.auto.tfvars.json",
            "submissions/capstone/code/mossvale-supply/terraform/terraform.tfvars",
            "submissions/vault/01-vault-first-contact/code/.vault-token",
        }
        kept = {
            ".env.example",
            ".env.template",
            "submissions/terraform/01-workflow/code/training.tfvars.example",
            "submissions/terraform/01-workflow/code/training.tfvars.json.example",
            "customers/mossvale-supply/terraform/terraform.tfvars",
        }
        self.assertEqual(self.ignored_paths(ignored | kept), ignored)

    def test_configuration_lock_files_and_evidence_remain_visible(self):
        paths = {
            f"{folder}/{artifact}"
            for folder in (
                ".",
                "submissions/terraform/00-block-types/example",
                "submissions/terraform/01-workflow/code",
            )
            for artifact in ("main.tf", "versions.tf", ".terraform.lock.hcl")
        }
        paths.update(
            {
                "submissions/terraform/00-block-types/example/release-template.txt",
                "submissions/terraform/00-block-types/code/.gitkeep",
                "submissions/terraform/00-block-types/evidence/task-01.md",
                "submissions/terraform/00-block-types/evidence/plan.txt",
            }
        )
        self.assertEqual(self.ignored_paths(paths), set())
