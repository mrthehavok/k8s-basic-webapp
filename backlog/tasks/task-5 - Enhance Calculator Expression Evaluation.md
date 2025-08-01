id: task-5
title: "Enhance Calculator Expression Evaluation"
status: "In Progress"
depends_on: ["task-4"]
created: 2025-08-01
updated: 2025-08-01

## Description

The project currently features a simple calculator that accepts two numbers and basic operations. This task aims to extend the functionality so that the **UI accepts an arbitrary arithmetic expression** and the **backend safely parses and evaluates** it.

Supported elements:  
– Operators: `+`, `-`, `*`, `/`, `^`  
– Parentheses for grouping `(` `)`  
– Functions: `sqrt`, `log`

## Acceptance Criteria

- **Frontend:**

  - A single text input allows users to enter an expression.
  - A **Calculate** button triggers evaluation.
  - The result (or error message) is displayed below the input.

- **Backend:**

  - A new endpoint `/api/evaluate?expr=...` (GET) is implemented in Flask.
  - Endpoint returns JSON `{ "result": <number> }` on success or `{ "error": "<message>" }` on failure.
  - Expression parsing and evaluation must be safe (e.g. using Python `ast` parsing or `sympy`).
  - Handles invalid syntax, math domain errors, and division by zero gracefully.

- **Deployment & CI/CD:**

  - Docker image, Kubernetes manifests, and GitHub Actions pipeline updated accordingly.
  - The updated calculator page is served at the root path.

- **Testing:**
  - Unit tests cover valid expressions, invalid syntax, and runtime errors.

## Session History


- 2025-08-01T12:01:42Z: Created branch `feat/task-5-enhance-calculator-exp-eval` and began development.
- 2025-08-01T12:14:20Z: Implemented `/api/evaluate` endpoint with `sympy` parser. Added unit tests and passed them locally.
- 2025-08-01T12:27:53Z: Restructured project into `backend/` and `frontend/` directories. Updated Dockerfile and CI workflows with path filtering.


## Decisions Made

- Used `sympy` for safe expression evaluation to prevent security risks associated with `eval()`.

- Restructured project to separate frontend and backend concerns for better CI/CD.
- Kept workflows in `.github/workflows` but added path filters to trigger builds only when relevant code changes.

## Files Modified

- `backend/calculator/app.py`
- `backend/calculator/requirements.txt`
- `backend/calculator/test_evaluate.py`
- `frontend/index.html`
- `Dockerfile`
- `.github/workflows/build-calculator.yml`
- `.github/workflows/deploy.yml`

## Blockers

<!-- Document any blockers encountered -->

## Next Steps

<!-- Maintain continuity between sessions -->
