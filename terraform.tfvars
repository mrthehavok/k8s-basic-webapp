# Centralised variable definitions for Terraform
#
# Adjust these values to match your environment. The CI pipeline
# automatically passes this file (one directory above terraform/)
# via `-var-file=../terraform.tfvars`.

aws_region   = "eu-west-1"

# EKS cluster
cluster_name = "basic-webapp-eks"

# Networking
vpc_cidr        = "10.0.0.0/16"
public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]
private_subnets = ["10.0.101.0/24", "10.0.102.0/24"]

# GitHub repository for OIDC trust (owner/repo)
github_repo = "mrthehavok/k8s-basic-webapp"