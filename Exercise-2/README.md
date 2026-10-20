# Exercise 2: Deploy a Flask App on Minikube Using kubectl and YAML

## Objective

Deploy a Python Flask application to Kubernetes using Docker, Minikube, kubectl, and YAML.

## Prerequisites

- Docker Desktop with WSL integration
- Minikube
- kubectl
- Ubuntu on WSL

## Technologies Used

- Python and Flask
- Docker
- Kubernetes
- Minikube
- YAML

## Project Structure

```text
Exercise-2/
├── app.py
├── Dockerfile
├── flask-deployment.yaml
└── README.md
```

## Step 1: Check the Cluster

```bash
minikube status -p devops-multinode
kubectl get nodes
```

## Step 2: Create the Flask Application

The `app.py` file runs a Flask server on port 15000 and returns a greeting.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Kubernetes!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=15000)
```

## Step 3: Create the Docker Image

The Dockerfile uses Python 3.8, installs Flask, copies the application, and starts the server.

Build the image:

```bash
docker buildx build --builder default --no-cache --load -t flask-app:latest .
```

## Step 4: Load the Image into Minikube

```bash
minikube image load flask-app:latest -p devops-multinode
minikube image ls -p devops-multinode | grep flask-app
```

## Step 5: Configure Kubernetes

The `flask-deployment.yaml` file contains both a Deployment and a NodePort Service.

- **Deployment:** Manages the Flask Pod.
- **replicas: 1:** Requests one Pod.
- **imagePullPolicy: Never:** Uses the locally available image instead of pulling it from a registry.
- **containerPort: 15000:** Specifies the application's container port.
- **Service:** Exposes the application inside Kubernetes.
- **targetPort: 15000:** Forwards traffic to the Flask application.
- **NodePort:** Makes the application accessible through Minikube's service-access mechanism.

## Step 6: Deploy the Application

```bash
kubectl apply -f flask-deployment.yaml
kubectl rollout status deployment/flask-app
```

## Step 7: Verify the Deployment

```bash
kubectl get deployments
kubectl get pods -l app=flask-app
kubectl describe deployment flask-app
kubectl logs deployment/flask-app
kubectl get services flask-app-service
```

The Pod should reach the `Running` state, and the Deployment should show one ready replica.

## Step 8: Access the Application

Run:

```bash
minikube service flask-app-service -p devops-multinode --url
```

Use the URL printed by Minikube. The port may change between runs. When using the Docker driver on WSL, keep the forwarding terminal open.

Test from a second terminal, replacing the example URL with the actual one:

```bash
curl http://127.0.0.1:40341
```

Expected response:

```text
Hello from Flask on Kubernetes!
```

## Architecture

```text
Client (curl / Browser)
          |
          v
Minikube Service Access
          |
          v
NodePort Service
          |
          v
Flask Pod
          |
          v
Docker Container
          |
          v
Flask Application (Port 15000)
```

## Result

The Flask application was containerized using Docker and deployed to the existing Minikube cluster. Kubernetes managed the Pod through a Deployment, and a NodePort Service enabled access to the application. The application returned the expected response when tested with curl.
