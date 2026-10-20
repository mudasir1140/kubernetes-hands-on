# Exercise 2: Deploy a Flask App on Minikube

## Aim
Deploy a Flask application on Kubernetes using Docker, Minikube, kubectl, and YAML.

## Files
- app.py: Flask application.
- Dockerfile: Builds the Docker image.
- flask-deployment.yaml: Defines the Deployment and NodePort Service.

## Procedure

1. Build the Docker image:
   docker buildx build --builder default --no-cache --load -t flask-app:latest .

2. Load the image into Minikube:
   minikube image load flask-app:latest -p devops-multinode

3. Deploy the application:
   kubectl apply -f flask-deployment.yaml

4. Check the deployment:
   kubectl rollout status deployment/flask-app
   kubectl get pods -l app=flask-app
   kubectl get services flask-app-service

5. Access the application:
   minikube service flask-app-service -p devops-multinode --url

6. Test the returned URL in another terminal using curl.

Expected response:
Hello from Flask on Kubernetes!

## Questions and Answers

### 1. What does minikube service --url do?
It provides a URL to access a Service running in Minikube.

### 2. What is targetPort?
It specifies the port on the application container that receives Service traffic.

### 3. What is the difference between port and targetPort?
port is the Service port, while targetPort is the destination port on the application Pod.

### 4. What is kubectl?
kubectl is the command-line tool used to manage Kubernetes resources.

### 5. What does kubectl apply -f do?
It creates or updates resources defined in a YAML file.

### 6. What is a Deployment?
A Deployment manages Pods and supports scaling and rolling updates.

### 7. What is a Service?
A Service provides a stable network endpoint for accessing selected Pods.

### 8. What is NodePort?
NodePort exposes a Service through a port on Kubernetes nodes.

### 9. Why use imagePullPolicy: Never?
It prevents Kubernetes from pulling the image from a registry. The image must already be available on the node running the Pod.

### 10. Why use port 15000?
The Flask application listens on port 15000, so the containerPort and Service targetPort are configured to match it.

## Result
The Flask application was deployed on Minikube using a Kubernetes Deployment and NodePort Service. A curl request returned the expected response.
