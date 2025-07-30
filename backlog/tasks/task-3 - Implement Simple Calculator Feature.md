id: task-3
title: "Implement Simple Calculator Feature"
status: "To Do"
depends_on: ["task-2"]
created: 2025-07-30
updated: 2025-07-30

## Description

This task involves adding a new feature to the web application: a **simple calculator**. This will require modifications to both the frontend (to create the user interface) and the backend (to create the calculation logic).

The calculator should support basic arithmetic operations: addition, subtraction, multiplication, and division.

## Acceptance Criteria

- [ ] **Frontend:**

  - [ ] A new "Calculator" section is added to `index.html`.
  - [ ] The UI includes two input fields for numbers and buttons for the four operations (+, -, \*, /).
  - [ ] A result area is present to display the output.
  - [ ] Clicking an operation button triggers a `fetch` call to the backend API.

- [ ] **Backend:**

  - [ ] A new API endpoint, `/api/calculate`, is added to the Flask application.
  - [ ] The endpoint accepts two numbers and an operation type as query parameters.
  - [ ] The endpoint returns a JSON object with the calculated result.
  - [ ] The endpoint includes error handling for invalid inputs (e.g., division by zero).

- [ ] **Deployment:**
  - [ ] The updated application is successfully deployed to the EKS cluster via the automated GitHub Actions pipeline.

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
