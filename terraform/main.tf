module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.5.2"

  name = "${var.cluster_name}-vpc"
  cidr = var.vpc_cidr

  azs             = ["${var.aws_region}a", "${var.aws_region}b"]
  public_subnets  = var.public_subnets
  private_subnets = var.private_subnets

  enable_nat_gateway = true
  single_nat_gateway = true
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "20.8.4"

  cluster_name    = var.cluster_name
  cluster_version = "1.31"
  subnet_ids      = module.vpc.private_subnets
  vpc_id          = module.vpc.vpc_id

  cluster_endpoint_public_access  = true
  cluster_endpoint_private_access = false

  enable_irsa = true

  eks_managed_node_groups = {
    default = {
      min_size     = 1
      max_size     = 3
      desired_size = 2

      instance_types = ["t3.micro"]
      ami_type       = "AL2023_x86_64_STANDARD"
    }
  }
}

# Data sources for EKS cluster are removed as they are not currently used
# and cause a dependency cycle during initial creation.
# They can be added back when Kubernetes resources are managed via Terraform.

data "aws_eks_cluster_auth" "this" {
  name = module.eks.cluster_name
}

provider "kubernetes" {
  host                   = module.eks.cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
  token                  = data.aws_eks_cluster_auth.this.token
}

variable "enable_aws_auth_patch" {
  description = "Temporarily skip aws-auth ConfigMap management until proper RBAC is in place."
  type        = bool
  default     = false
}

resource "kubernetes_config_map_v1_data" "aws_auth" {
  count = var.enable_aws_auth_patch ? 1 : 0

  metadata {
    name      = "aws-auth"
    namespace = "kube-system"
  }

  data = {
    mapRoles = yamlencode(
      [
        {
          rolearn  = aws_iam_role.github_actions.arn
          username = "github-actions"
          groups = [
            "system:masters",
          ]
        }
      ]
    )
  }

  depends_on = [module.eks]
}
