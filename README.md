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
terraform/
┣ versions.tf       # providers & S3 backend
┣ variables.tf      # input variables
┣ main.tf           # VPC + EKS modules
┣ iam.tf            # OIDC provider & GitHub Actions role
┗ outputs.tf        # useful outputs
```

### Prerequisites

| Requirement                                                     | Why                        |
| --------------------------------------------------------------- | -------------------------- |
| **AWS account** with permissions to create VPC / EKS            | Infrastructure             |
| **S3 bucket** + **DynamoDB table** for remote state             | Terraform backend          |
| **GitHub OIDC provider** created once per account               | Keyless auth               |
| **GitHub repository secret** `AWS_REGION` (default `us-east-1`) | Workflow region override   |
| **OIDC-assumable IAM role** defined in `iam.tf`                 | Terraform / kubectl deploy |

> ℹ️ The OIDC provider and role will be created automatically by Terraform if they do not exist (first run requires elevated AWS credentials).

### Common commands (local)

```bash
# Initialise & pull remote state
terraform -chdir=terraform init

# Review changes
terraform -chdir=terraform plan -var="github_repo=<owner>/<repo>"

# Apply (creates/updates infra)
terraform -chdir=terraform apply
```

---

## CI/CD Pipeline (GitHub Actions)

[`/.github/workflows/deploy.yml`](.github/workflows/deploy.yml:1) orchestrates a two-stage pipeline:

1. **Pull Request**

   - `terraform fmt -check && tflint`
   - `terraform plan` – plan posted as comment on the PR.

2. **Merge to `main`**
   - GitHub OIDC → AWS STS → Assume role `${var.cluster_name}-github-actions`.
   - `terraform apply` – builds/updates VPC & EKS.
   - `aws eks update-kubeconfig` – obtains cluster credentials.
   - `kubectl apply -f manifests/` – deploys the application.

No AWS keys are stored; short-lived credentials are exchanged at runtime.

---

## Bootstrap Checklist

1. 🔑 Create an **S3 bucket** and **DynamoDB table**
   ```bash
   aws s3 mb s3://<YOUR_BUCKET>
   aws dynamodb create-table \
     --table-name <YOUR_TABLE> \
     --attribute-definitions AttributeName=LockID,AttributeType=S \
     --key-schema AttributeName=LockID,KeyType=HASH \
     --billing-mode PAY_PER_REQUEST
   ```
2. 🔐 (First time) Add the GitHub OIDC provider in IAM **or** let Terraform create it.
3. 📄 Update `terraform/versions.tf` backend block – replace `CHANGE_ME-terraform-state` & `CHANGE_ME-terraform-lock`.
4. 💬 Add repository secret **`AWS_REGION`** (optional if using default).
5. ✅ Open a Pull Request – ensure the **plan** appears.
6. 🚀 Merge to `main` – the **apply** job provisions EKS and deploys the app.

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
