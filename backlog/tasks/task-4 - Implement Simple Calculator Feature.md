id: task-4
title: "Implement Simple Calculator Feature"
status: "Done"
depends_on: ["task-2"]
created: 2025-07-30
updated: 2025-07-31

## Description

This task involves adding a new feature to the web application: a **simple calculator**. This will require modifications to both the frontend (to create the user interface) and the backend (to create the calculation logic).

The calculator should support basic arithmetic operations: addition, subtraction, multiplication, and division.

## Acceptance Criteria

- [x] **Frontend:**

  - [x] A new "Calculator" section is added to `index.html`.
  - [x] The UI includes two input fields for numbers and buttons for the four operations (+, -, \*, /).
  - [x] A result area is present to display the output.
  - [x] Clicking an operation button triggers a `fetch` call to the backend API.

- [x] **Backend:**

  - [x] A new API endpoint, `/api/calculate`, is added to the Flask application.
  - [x] The endpoint accepts two numbers and an operation type as query parameters.
  - [x] The endpoint returns a JSON object with the calculated result.
  - [x] The endpoint includes error handling for invalid inputs (e.g., division by zero).

- [x] **Deployment:**
  - [x] The updated application is successfully deployed to the EKS cluster via the automated GitHub Actions pipeline.

## Session History

- **2025-07-31**: Implemented HTML UI and `/api/calculate` endpoint.

## Decisions Made

- Served `index.html` directly from Flask to avoid additional Nginx config.

## Files Modified

- `index.html`
- `calculator/app.py`
- `Dockerfile`
- `README.md`

## Blockers

<!-- Document any blockers encountered -->

## Next Steps

<!-- Maintain continuity between sessions -->
