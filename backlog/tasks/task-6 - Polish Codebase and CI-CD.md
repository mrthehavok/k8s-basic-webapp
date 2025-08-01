id: task-6
title: "Polish Codebase and CI/CD"
status: "Done"
depends_on: ["task-5"]
created: 2025-08-01
updated: 2025-08-01

## Description

This task focuses on refining the existing CI/CD pipeline, improving documentation, and implementing best practices for a more robust and maintainable system. The key goals are to streamline the deployment process, enhance code quality, and provide clear guidance for future development.

## Acceptance Criteria

- **CI/CD Refactoring:**

  - [ ] The `.github/workflows/build-calculator.yml` workflow is simplified, removing redundant triggers.
  - [ ] The `.github/workflows/deploy.yml` workflow is updated to:
    - Run `terraform plan` and `kubectl diff` on pull requests to `main`.
    - Run `terraform apply` and `kubectl apply` only on merge/push to `main`.
  - [ ] The Kubernetes deployment automatically rolls out a new version when the Docker image with the `latest` tag is updated, removing the need for manual `kubectl rollout restart`.

- **Documentation:**

  - [ ] The main `README.md` is updated to reflect the new `backend/`/`frontend/` structure.
  - [ ] A brief explanation of the CI/CD pipeline is added to the `README.md`.

- **Architectural Improvements:**
  - [ ] Propose and document at least three potential architectural improvements for future consideration (e.g., vulnerability scanning, pre-commit hooks, multi-arch builds).

## Session History

- 2025-08-01: Completed all acceptance criteria for task-6.

## Decisions Made

- Refactored CI/CD workflows for clarity and correctness, separating plan/diff from apply stages.
- Updated documentation to reflect current project structure.
- Identified and documented architectural improvements for future work.

## Files Modified

- `.github/workflows/build-calculator.yml`
- `.github/workflows/deploy.yml`
- `README.md`
- `ARCHITECTURAL_IMPROVEMENTS.md`

## Blockers

<!-- Document any blockers encountered -->

## Next Steps

<!-- Maintain continuity between sessions -->
