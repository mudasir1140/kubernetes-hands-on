# Exercise 1: Kubernetes Getting Started

## Objective
Deploy an Nginx web server in Kubernetes using Minikube, expose it through a NodePort service, and verify browser access.

## Tools Used
- Ubuntu on WSL
- Docker Desktop
- Minikube
- kubectl
- Nginx

## Procedure

### 1. Start Minikube
```bash
minikube start -p devops-multinode
```

### 2. Create an Nginx Pod
```bash
kubectl run hello-k8s --image=nginx:stable --port=80
```

### 3. Verify the Pod
```bash
kubectl get pods
```

Confirm that the `hello-k8s` Pod is running and ready.

### 4. Expose the Pod
```bash
kubectl expose pod hello-k8s --type=NodePort --port=80
```

### 5. Access the Service
```bash
minikube service hello-k8s -p devops-multinode --url
```

Open the generated URL in a browser. Keep the terminal running while the Minikube service tunnel is active.

## Result
Successfully deployed an Nginx Pod in Minikube, exposed it through a NodePort service, and verified that the Nginx welcome page opened in the browser.

## Notes
- The `nginx:stable` image was used for the successful deployment.
- The Minikube profile is `devops-multinode`.
