---
icon: material/rocket-launch-outline
---

# Local setup

The guide uses Podman, mise, and a local AWS target. The target is safe to
repeat, but it does not prove real AWS behavior.

## Install the tools

Install:

- [Podman](https://podman.io/docs/installation)
- [podman-compose](https://github.com/containers/podman-compose) 1.3.0 or later
- [mise](https://mise.jdx.dev/installing-mise.html)

The container tasks use rootless Podman and the `podman-compose` provider.
They do not require Docker or membership in the Docker group.

From the repository root, install the pinned Terraform, Vault, AWS CLI,
Python, and MkDocs tools:

```bash
mise install
```

## Start the local services

Run:

```bash
mise run setup
```

This starts and checks Floci on `localhost:4566`, Floci UI on
<http://localhost:4500>, and PostgreSQL on `localhost:5432`. It creates no
AWS resources and seeds no data.

The setup does not mount a container engine socket. Floci services that start
other containers, such as Lambda and RDS, need extra configuration. For rootless
Podman, see [Floci's Podman guide](https://floci.io/floci/configuration/docker/#running-on-podman-rootless).
Socket access lets Floci control your containers. Grant it only to an image you
trust.

Stop the services and remove their local PostgreSQL data with:

```bash
mise run stop
```

## Docker fallback

If you cannot use Podman, install [Docker](https://docs.docker.com/engine/install/)
and the [Docker Compose plugin](https://docs.docker.com/compose/install/linux/).
Select Docker in every shell that runs container tasks:

```bash
export CONTAINER_ENGINE=docker
```

The tasks run Docker commands through `sudo`, not through Docker group
membership. Do not run `mise` or Terraform with `sudo`. For manual commands,
use `sudo docker`, for example. Docker commands run with root privileges.

```bash
sudo docker compose ps
```

Podman and Docker have separate containers and volumes. Keep the same engine
for setup, start, stop, and customer tasks. Before switching an existing Docker
training environment to Podman, stop its containers without deleting volumes:

```bash
sudo docker compose down
```

Run this from the repository root. If you also started the customer environment
with Docker, stop it without deleting its volumes:

```bash
sudo docker compose --project-name "mossvale-supply-$(id -u)" \
  -f submissions/capstone/code/mossvale-supply/compose.yml down
```

Keep its volumes and working copy if you need the data later.

## Configure the AWS tools

With a real AWS account, you would create an access key and export it. Floci
accepts any key, so use these test values in each shell that runs Terraform
or the AWS CLI:

```bash
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
export AWS_REGION=us-east-1
export AWS_ENDPOINT_URL=http://localhost:4566
```

`AWS_ENDPOINT_URL` points AWS requests at Floci. For example, with the AWS CLI:

```bash
aws s3 ls
```

This lists buckets in Floci, not in AWS. You can browse resources in the
[Floci UI](http://localhost:4500).

!!! warning "Use these values only for Floci"
    Close the shell or unset these variables before working with a real AWS
    account. Never put a real access key in `submissions/`.

### Configure the Terraform AWS provider

Floci uses the standard `hashicorp/aws` provider, not a separate provider.
It needs provider settings beyond the shell variables above.
Configure these before the first Terraform plan, not only when troubleshooting.

Use the [Floci Terraform guide](https://floci.io/floci/getting-started/terraform/)
as the configuration reference:

- Skip credential validation, EC2 metadata checks, and account ID lookup with
  `skip_credentials_validation`, `skip_metadata_api_check`, and
  `skip_requesting_account_id`.
- Enable path-style S3 requests with `s3_use_path_style`.
- Set an endpoint override to `http://localhost:4566` for every AWS service
  your configuration uses.

Write the provider configuration yourself and pin its version in Terraform 01.
If you later use an S3 backend, configure it separately.
AWS provider settings do not configure Terraform's backend.
