#!/usr/bin/env bash
# Idempotent bootstrap script for Terraform remote-state S3 bucket.
# Creates the bucket if it does not yet exist and enables versioning.
#
# Usage (local or CI):
#   ./scripts/create_backend_bucket.sh
#
# Environment:
#   AWS_REGION – AWS region to create / check the bucket in
#                (defaults to eu-west-1 for this project).

set -euo pipefail

BUCKET="k8s-tfstate-347913851454-eu-west-1"
REGION="${AWS_REGION:-eu-west-1}"

echo "🔍  Checking existence of S3 bucket: ${BUCKET} in ${REGION} …"

if aws s3api head-bucket --bucket "${BUCKET}" 2>/dev/null; then
  echo "✅  Bucket ${BUCKET} already exists – nothing to do."
  exit 0
fi

echo "🚀  Creating bucket ${BUCKET} …"
aws s3api create-bucket \
  --bucket "${BUCKET}" \
  --region "${REGION}" \
  --create-bucket-configuration LocationConstraint="${REGION}"

echo "🔒  Enabling versioning on bucket ${BUCKET} …"
aws s3api put-bucket-versioning \
  --bucket "${BUCKET}" \
  --versioning-configuration Status=Enabled

echo "✅  Bucket ${BUCKET} created and versioning enabled."