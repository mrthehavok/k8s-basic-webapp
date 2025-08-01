# Architectural Improvement Proposals

This document outlines potential enhancements to the project's architecture, focusing on security, developer experience, and maintainability.

### 1. Implement Pre-Commit Hooks

- **Problem:** Inconsistent code formatting and simple bugs can make it into the codebase, creating noise in pull requests and requiring CI to catch trivial errors.
- **Proposal:** Use a tool like `pre-commit` to automatically run linters (`flake8`, `pylint`), formatters (`black`), and other checks before a commit is created.
- **Benefits:**
  - Enforces a consistent code style across all commits.
  - Catches simple errors early, reducing CI load and speeding up the development cycle.
  - Improves overall code quality.

### 2. Add Vulnerability Scanning to CI

- **Problem:** Application dependencies (both in `requirements.txt` and the base Docker image) can have known security vulnerabilities (CVEs).
- **Proposal:** Integrate a security scanner into the `build-calculator.yml` workflow.
  - Use `trivy` or `snyk` to scan the Docker image for OS and dependency vulnerabilities.
  - Use `pip-audit` or `safety` to scan `requirements.txt`.
  - Fail the build if high-severity vulnerabilities are found.
- **Benefits:**
  - Automates security checks, preventing known vulnerabilities from reaching production.
  - Provides a clear audit trail of security scans.

### 3. Split Terraform Modules

- **Problem:** The current Terraform configuration is monolithic, with all resources (VPC, EKS, IAM) in a single directory. This can become difficult to manage as the infrastructure grows.
- **Proposal:** Refactor the Terraform code into reusable modules.
  - Create a `modules/` directory.
  - Create separate modules for `vpc`, `eks`, and `iam`.
  - The root `terraform/` directory would then instantiate these modules, passing in variables.
- **Benefits:**
  - Improves code organization and reusability.
  - Allows for independent testing and versioning of infrastructure components.
  - Simplifies the root configuration, making it easier to understand the overall infrastructure at a glance.
