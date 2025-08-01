d: task-8
title: "Fix Smoke Test 404"
status: "To Do"
created: 2025-08-01
updated: 2025-08-01

## Description

Smoke test returns 404 against `/healthz`. Determine correct readiness endpoint or route, update k8s manifests or workflow accordingly so smoke test passes.

## Acceptance Criteria

- Correct endpoint discovered or added (returns HTTP 200).
- Deploy workflow smoke test step succeeds.
- Summary shows ✅.

## Session History

<!-- Update as work progresses -->

## Decisions Made

<!-- Document key implementation decisions -->

## Files Modified

<!-- Track all file changes -->
