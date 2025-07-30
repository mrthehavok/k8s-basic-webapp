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

## Accessing the Application

1.  **Create a tunnel:** Open a new terminal and run the following command. It will run continuously.

    ```bash
    minikube tunnel
    ```

2.  **Find the IP:** In your original terminal, get the IP address for the Ingress.

    ```bash
    kubectl get ingress -n learning-ns
    ```

    The IP address will be listed in the `ADDRESS` column.

3.  **Open in browser:** Open a web browser and navigate to the IP address from the previous step.
