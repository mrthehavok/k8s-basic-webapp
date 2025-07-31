terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.30"
    }
  }

  backend "s3" {
    # TODO: replace with real bucket/key before first apply
    bucket       = "k8s-tfstate-347913851454-eu-west-1"
    key          = "eks/terraform.tfstate"
    region       = "eu-west-1"
    encrypt      = true
    use_lockfile = true
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      created_by   = "terraform"
      project_name = "k8s-basic-webapp"
    }
  }
}
