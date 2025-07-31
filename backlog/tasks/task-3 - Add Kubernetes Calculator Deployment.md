id: task-3
title: "Add Kubernetes Calculator Deployment"
status: "In Progress"
depends_on: ["task-2"]
created: 2025-07-31
updated: 2025-07-31

## Description

Write Kubernetes-ready code and manifests for the web-calculator service.  
Use the existing **manual** branch as an implementation reference.

## Acceptance Criteria

- [-] Calculator container image builds via GitHub Actions.
- [-] Raw manifests included under `charts/` or `k8s/`.
- [ ] Deployment runs in EKS cluster when applied.
- [-] README is updated with deployment instructions.

## Session History

- 2025-07-31 09:44: Agent started work. Created Flask application, Dockerfile, GitHub Actions workflow, Kubernetes manifests, and updated README.

## Decisions Made

<!-- Document key choices -->

## Files Modified

- `calculator/app.py` (created)
- `calculator/requirements.txt` (created)
- `Dockerfile` (created)
- `.dockerignore` (created)
- `.github/workflows/build-calculator.yml` (created)
- `k8s/deployment.yaml` (created)
- `k8s/service.yaml` (created)
- `k8s/ingress.yaml` (created)
- `README.md` (modified)

## Blockers

<!-- Fill during implementation -->

## Next Steps

<!-- Fill during implementation -->
