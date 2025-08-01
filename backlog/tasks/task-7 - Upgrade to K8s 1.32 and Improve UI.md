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

- 2025-08-01: Started work on task-7.
- 2025-08-01: Updated Terraform to use Kubernetes 1.32.
- 2025-08-01: Refreshed frontend UI with new button styles.
- 2025-08-01: Added `/health` endpoint to backend application.
- 2025-08-01: Added smoke test to CI/CD deploy workflow.
- 2025-08-01: Updated task statuses for task-6 and task-7.

## Decisions Made

- Added a `/health` endpoint to the backend for the smoke test.
- Added a smoke test to the CI/CD pipeline to verify deployment health.
- Updated the UI with CSS for a modern look and feel.

## Files Modified

- `terraform/main.tf`
- `frontend/index.html`
- `backend/calculator/app.py`
- `.github/workflows/deploy.yml`
- `backlog/tasks/task-6 - Polish Codebase and CI-CD.md`
- `backlog/tasks/task-7 - Upgrade to K8s 1.32 and Improve UI.md`

## Blockers

<!-- Document any blockers encountered -->

## Next Steps

<!-- Maintain continuity between sessions -->
