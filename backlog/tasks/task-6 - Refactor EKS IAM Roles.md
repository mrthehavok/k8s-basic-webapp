id: task-6
title: "Refactor EKS IAM Roles"
status: "To Do"
created: 2025-07-31
updated: 2025-07-31

## Description

Refactor the EKS IAM roles to use separate, externally managed resources instead of the inline policies created by the EKS module. This will resolve the `inline_policy` deprecation warning and improve the modularity of the IAM setup.

## Acceptance Criteria

- [ ] Create a new `eks_iam.tf` file to define the IAM roles for the EKS cluster and node groups.
- [ ] Update the `main.tf` file to use the externally created IAM roles and disable the default role creation in the EKS module.
- [ ] Verify that the `inline_policy` deprecation warning is no longer present when running `terraform plan`.
- [ ] Ensure that the EKS cluster and node groups are still created successfully with the new IAM roles.

## Session History

<!-- Update as work progresses -->

## Decisions Made

<!-- Document key implementation decisions -->

## Files Modified

- `terraform/eks_iam.tf` (created)
- `terraform/main.tf` (modified)

## Blockers

<!-- Document any blockers encountered -->

## Next Steps

- [ ] Apply the Terraform changes and verify the new IAM roles are working correctly.
- [ ] Merge the changes into the `main` branch after the EKS cluster upgrade is complete.
