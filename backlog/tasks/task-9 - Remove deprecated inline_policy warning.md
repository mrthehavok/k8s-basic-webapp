d: task-9
title: "Remove deprecated inline_policy warning"
status: "To Do"
created: 2025-08-01
updated: 2025-08-01

## Description

Terraform warns: `inline_policy is deprecated` on EKS IAM role. Replace with `aws_iam_role_policy` (or `aws_iam_role_policies_exclusive`) to eliminate warning.

## Acceptance Criteria

- Terraform plan/apply runs without the deprecation warning.
- CI pipelines green.

## Session History

<!-- Update as work progresses -->

## Decisions Made

<!-- Document key implementation decisions -->

## Files Modified

<!-- Track all file changes -->
