# Kubernetes Basic Webapp

A simple two-tier application to demonstrate core Kubernetes concepts.

## Prerequisites

- `kubectl`
- A running Kubernetes cluster (e.g., minikube, kind, Docker Desktop)
- Ingress controller (e.g., `minikube addons enable ingress`)

## Architecture

This project uses a two-tier architecture:

- **Frontend**: An `nginx` container serving a static HTML/JS page.
- **Backend**: A simple Python Flask API providing time and timezone calculation logic.

## Deployment

To deploy the application, run:

```bash
kubectl apply -f manifests/
```

To delete the application, run:

```bash
kubectl delete -f manifests/
```
