id: task-7
title: "Upgrade to Kubernetes 1.32 & UI polish"
status: "In Progress"
created: 2025-08-01
updated: 2025-08-01

## Description

Upgrade the EKS cluster to Kubernetes 1.32 and prove deployments succeed. Add a subtle UI refresh to the calculator frontend so change is visible.

## Acceptance Criteria

- [ ] Cluster version set to 1.32 in Terraform and applied successfully via CI.
- [ ] CI deploy workflow includes a smoke-test step: after apply, fetch service LB hostname and `curl -fsS /health` (summary). Fails the job if non-200.
- [ ] Frontend UI enhanced (modern button colour & hover effect) – visible in browser.
- [ ] PR shows green pipelines (plan & apply) and smoke test passes.

## Session History

<!-- Update as work progresses -->

## Decisions Made

<!-- Document key implementation decisions -->

## Files Modified

<!-- Track all file changes -->

## Blockers

<!-- Document any blockers encountered -->

## Next Steps

<!-- Maintain continuity between sessions -->
