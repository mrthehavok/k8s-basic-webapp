# k8s-basic-webapp

A two-tier demo application that runs **Nginx** (frontend) and **Flask** (backend).  
It supports **local development** with Minikube and **automated deployment** to an **AWS EKS** cluster driven by Terraform and GitHub Actions (OIDC federation – no long-lived AWS keys).

---

## Table of Contents

1. [Architecture](#architecture)
2. [Local Development (Minikube)](#local-development-minikube)
3. [AWS Infrastructure as Code (Terraform)](#aws-infrastructure-as-code-terraform)
4. [CI/CD Pipeline (GitHub Actions)](#cicd-pipeline-github-actions)
5. [Bootstrap Checklist](#bootstrap-checklist)
6. [Troubleshooting & FAQ](#troubleshooting--faq)
7. [Contributing](#contributing)
8. [License](#license)

---

## Architecture

```
┌──────────────┐     ┌──────────────┐
│  Nginx FE    │     │  Flask BE    │
│   Service    │ ─► │   Service     │
└──────────────┘     └──────────────┘
        ▲                     │
        │ Ingress             │
        └─────────── LB ──────┘
```

| Layer    | Development     | Production (AWS)                                      |
| -------- | --------------- | ----------------------------------------------------- |
| Compute  | Minikube VM     | Amazon EKS (managed K8s)                              |
| Network  | Minikube bridge | VPC + public/private subnets                          |
| TLS / LB | Nginx Ingress   | AWS ALB (via `alb.ingress.kubernetes.io` annotations) |
| State    | —               | S3 backend + DynamoDB lock table (Terraform)          |

---

## Local Development (Minikube)

```bash
# 1. Start Minikube
minikube start

# 2. Deploy manifests
kubectl apply -f manifests/

# 3. Access the app
minikube service nginx-service
```

### Tear down

```bash
kubectl delete -f manifests/
minikube delete
```

---

## AWS Infrastructure as Code (Terraform)

```
.
├── .github/workflows/deploy.yml  # CI/CD Pipeline
├── manifests/                    # Kubernetes manifests
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

## CI/CD Pipeline (GitHub Actions)

[`/.github/workflows/deploy.yml`](.github/workflows/deploy.yml:1) orchestrates a two-stage pipeline:

1. **Pull Request**

   - `terraform fmt -check && tflint`
   - `terraform plan` – plan posted as comment on the PR.

2. **Merge to `main`**
   - GitHub OIDC → AWS STS → Assume role via `secrets.AWS_IAM_ROLE_TO_ASSUME`.
   - `terraform apply` – builds/updates VPC & EKS.
   - `aws eks update-kubeconfig` – obtains cluster credentials.
   - `kubectl apply -f manifests/` – deploys the application.

No AWS keys are stored; short-lived credentials are exchanged at runtime.

---

## Bootstrap Checklist

1. 🔑 **Bootstrap S3 Backend**
   The **deploy** GitHub Actions workflow automatically runs the helper script on every PR and merge.
   Local execution is only required if you want to run `terraform init/plan/apply` from your workstation:
   ```bash
   ./scripts/create_backend_bucket.sh
   ```
2. 📄 **Configure Variables**: Copy `terraform.tfvars.example` to `terraform.tfvars` and update the `github_repo` and other variables as needed.
3. 🔐 **Configure Secrets**: Add the `AWS_IAM_ROLE_TO_ASSUME` secret to your GitHub repository settings, containing the ARN of the role created by `iam.tf`.
4. ✅ **Open a Pull Request**: Ensure the **plan** appears, loading variables from `terraform.tfvars`.
5. 🚀 Merge to `main` – the **apply** job provisions EKS and deploys the app.

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

## Calculator Application

### Build

To build the Docker image for the calculator application, run the following command from the root of the repository:

```bash
docker build -t ghcr.io/&lt;owner&gt;/calculator:latest .
```

The image will also be built automatically by a GitHub Actions workflow when changes are pushed to the `feat/task-3-k8s-calculator` branch.

### Deploy

To deploy the application to a Kubernetes cluster, apply the manifests in the `k8s/` directory:

```bash
kubectl apply -f k8s/
```

### Usage

Open `index.html` in a browser after the service is running. The page includes a
simple calculator UI that calls the `/api/calculate` endpoint. The API accepts
`a`, `b`, and `op` query parameters where `op` is one of `add`, `subtract`,
`multiply`, or `divide`.
