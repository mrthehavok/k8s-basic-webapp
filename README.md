# k8s-basic-webapp

A simple calculator web application with a vanilla HTML/JS frontend and a **Flask** backend.
It supports **local development** and **automated deployment** to an **AWS EKS** cluster driven by Terraform and GitHub Actions.

---

## Table of Contents

1.  [Architecture](#architecture)
2.  [Local Development](#local-development)
3.  [AWS Infrastructure as Code (Terraform)](#aws-infrastructure-as-code-terraform)
4.  [CI/CD Pipeline](#cicd-pipeline)
5.  [Bootstrap Checklist](#bootstrap-checklist)
6.  [Troubleshooting & FAQ](#troubleshooting--faq)
7.  [Contributing](#contributing)
8.  [License](#license)

---

## Architecture

The repository is structured as follows:

- `frontend/`: Contains the static HTML and JavaScript for the calculator UI.
- `backend/`: Holds the Python Flask application that provides the calculation API.
- `k8s/`: Kubernetes manifests for deploying the application (Deployment, Service, Ingress).
- `terraform/`: Terraform code for provisioning the AWS EKS cluster and related infrastructure.
- `.github/workflows/`: GitHub Actions workflows for CI/CD.

---

## Local Development

To run the application locally, you can use the provided Dockerfile:

```bash
# Build the image
docker build -t calculator-app .

# Run the container
docker run -p 8000:8000 calculator-app
```

The application will be available at `http://localhost:8000`.

---

## AWS Infrastructure as Code (Terraform)

```
.
├── .github/workflows/deploy.yml  # CI/CD Pipeline
├── k8s/                          # Kubernetes manifests
├── scripts/
│   └── create_backend_bucket.sh  # Idempotent S3 bootstrap
├── terraform/
│   ├── versions.tf               # Providers & S3 backend
│   ├── variables.tf              # Variable definitions
│   ├── main.tf                   # VPC + EKS modules
│   ├── iam.tf                    # OIDC provider & GitHub Actions role
│   └── outputs.tf                # Useful outputs
└── terraform.tfvars              # Root variable values
```

### Prerequisites

| Requirement                                            | Purpose / Usage                                            |
| ------------------------------------------------------ | ---------------------------------------------------------- |
| **AWS account** with permissions to create VPC / EKS   | Provisioning infrastructure                                |
| **AWS CLI** configured for the target account / region | Required for the local bootstrap script & manual Terraform |
| **Terraform CLI ≥ 1.5**                                | Local `terraform init / plan / apply` (optional)           |
| **S3 bucket** for remote state                         | Backend for Terraform state & locking                      |
| **GitHub OIDC provider** created once per account      | Key-less authentication from GitHub Actions                |
| **GitHub repository secret** `AWS_IAM_ROLE_TO_ASSUME`  | ARN of the IAM role to assume from the workflow            |
| **Root `terraform.tfvars` file**                       | Centralised variable management                            |

> _¹ The bucket and table are created automatically by the bootstrap script **or** by the CI pipeline if they don’t exist._

> ℹ️ The OIDC provider and role will be created automatically by Terraform if they do not exist (first run requires elevated AWS credentials).

### Common commands (local)

```bash
# Initialise & pull remote state
terraform -chdir=terraform init

# Review changes
terraform -chdir=terraform plan -var-file=../terraform.tfvars

# Apply (creates/updates infra)
terraform -chdir=terraform apply -var-file=../terraform.tfvars
```

---

## CI/CD Pipeline

The CI/CD process is automated using GitHub Actions and is split into two main workflows:

1.  **Build (`build-calculator.yml`):**

    - **Trigger:** Runs on pull requests or pushes to `main` that modify the application code (`frontend/`, `backend/`) or the `Dockerfile`.
    - **Action:** Builds the Docker image. On a push to `main`, it pushes the image to GHCR, tagging it with `latest` and the commit SHA.

2.  **Deploy (`deploy.yml`):**
    - **Trigger:** Runs on pull requests or pushes to `main` that modify the infrastructure (`terraform/`) or Kubernetes (`k8s/`) code.
    - **Plan (on PR):**
      - Runs `terraform plan` to preview infrastructure changes.
      - Runs `kubectl diff` to preview Kubernetes manifest changes.
    - **Apply (on push to `main`):**
      - Applies the Terraform plan.
      - Uses `kustomize` to update the image tag in the Kubernetes deployment to the specific commit SHA and applies the manifests, triggering a zero-downtime rolling update.

---

## Bootstrap Checklist

1.  🔑 **Bootstrap S3 Backend**
    The **deploy** GitHub Actions workflow automatically runs the helper script on every PR and merge.
    Local execution is only required if you want to run `terraform init/plan/apply` from your workstation:
    ```bash
    ./scripts/create_backend_bucket.sh
    ```
2.  📄 **Configure Variables**: Copy `terraform.tfvars.example` to `terraform.tfvars` and update the `github_repo` and other variables as needed.
3.  🔐 **Configure Secrets**: Add the `AWS_IAM_ROLE_TO_ASSUME` secret to your GitHub repository settings, containing the ARN of the role created by `iam.tf`.
4.  ✅ **Open a Pull Request**: Ensure the **plan** appears, loading variables from `terraform.tfvars`.
5.  🚀 Merge to `main` – the **apply** job provisions EKS and deploys the app.

---

## Troubleshooting & FAQ

| Symptom                          | Resolution                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------- |
| `Error acquiring the state lock` | Verify DynamoDB table exists & ensure no pending lock rows.                     |
| GitHub Action `AccessDenied`     | Confirm OIDC role trust policy includes `repo:<owner>/<repo>` & correct branch. |
| Load balancer not created        | Check AWS ALB Ingress Controller logs and VPC subnets are tagged for ELB.       |

---

## Contributing

PRs welcome!
Please follow the [commit style conventions](AGENTS.md:1) and open issues for feature requests.

---

## License

MIT
