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

- 2025-08-01T12:14:20Z: Implemented `/api/evaluate` endpoint with `sympy` parser. Added unit tests and passed them locally.

## Decisions Made

- Used `sympy` for safe expression evaluation to prevent security risks associated with `eval()`.

## Files Modified

- `calculator/app.py`
- `calculator/requirements.txt`
- `calculator/test_evaluate.py`

## Blockers

<!-- Document any blockers encountered -->

## Next Steps

<!-- Maintain continuity between sessions -->
