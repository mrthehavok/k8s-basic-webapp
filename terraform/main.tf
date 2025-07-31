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

  # Enable the EKS module to manage the aws-auth ConfigMap
  authentication_mode = "API_AND_CONFIG_MAP"

  # Grant access to specific IAM principals
  access_entries = {
    # Grant your user admin access
    idmitriev = {
      principal_arn = "arn:aws:iam::347913851454:user/idmitriev"
      policy_associations = {
        admin = {
          policy_arn = "arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy"
          access_scope = {
            type = "cluster"
          }
        }
      }
    }
    # Grant GitHub Actions role admin access
    github_actions = {
      principal_arn = aws_iam_role.github_actions.arn
      policy_associations = {
        admin = {
          policy_arn = "arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy"
          access_scope = {
            type = "cluster"
          }
        }
      }
    }
  }
}

# Output to confirm who has access
output "eks_access_entries" {
  description = "IAM principals with EKS cluster access"
  value = {
    user           = "arn:aws:iam::347913851454:user/idmitriev"
    github_actions = aws_iam_role.github_actions.arn
  }
}
