# Exercise 3: Scaling Flask App on a Single Node Using ReplicaSets

## Objective

- Deploy a Flask application on Kubernetes.
- Scale the application from three to five replicas.
- Test application endpoints.
- Demonstrate ReplicaSet self-healing.
- Observe Pod distribution on a single node.

## Real-World Use Case

During an e-commerce flash sale, multiple application Pods help handle incoming requests. A Kubernetes ReplicaSet maintains the desired number of Pods and replaces Pods that are deleted or fail.

**Note:** A ReplicaSet does not automatically scale based on traffic. Manual scaling or a Horizontal Pod Autoscaler is required for automatic scaling.

## Technologies Used

- Python and Flask
- Gunicorn
- Docker
- Kubernetes and Minikube
- kubectl and YAML

## Project Files

- `app.py` — Flask application
- `Dockerfile` — Builds the application image
- `flashsale-replicaset.yaml` — Defines the ReplicaSet and Service
- `README.md` — Exercise documentation

## Step 1: Build the Docker Image

```bash
docker buildx build --builder default --no-cache --load -t flashsale:1.0 .
minikube image load flashsale:1.0 -p flashsale-single
```

## Step 2: Deploy the Application

```bash
kubectl config use-context flashsale-single
kubectl apply -f flashsale-replicaset.yaml
kubectl get rs
kubectl get pods -l app=flashsale
```

Initially, the ReplicaSet creates three Pods.

## Step 3: Scale to Five Replicas

```bash
kubectl scale rs flashsale-rs --replicas=5
kubectl wait --for=condition=Ready pod -l app=flashsale --timeout=120s
kubectl get rs
kubectl get pods -l app=flashsale
```

The ReplicaSet creates two additional Pods to reach five replicas.

## Step 4: Verify Self-Healing

Delete one Pod:

```bash
kubectl delete pod "$(kubectl get pods -l app=flashsale -o jsonpath='{.items[0].metadata.name}')"
```

Verify the replacement:

```bash
kubectl wait --for=condition=Ready pod -l app=flashsale --timeout=120s
kubectl get rs flashsale-rs
kubectl get pods -l app=flashsale
```

The ReplicaSet automatically creates a replacement to maintain five Pods.

## Step 5: Check Node Distribution

```bash
kubectl get pods -l app=flashsale -o wide
```

All five Pods were observed running on the single node `flashsale-single`.

## Step 6: Test the Application

Start port forwarding:

```bash
kubectl port-forward svc/flashsale-svc 8080:80
```

Keep that terminal open. In a second terminal, run:

```bash
curl http://127.0.0.1:8080/
curl "http://127.0.0.1:8080/buy?user=123"
curl http://127.0.0.1:8080/health
```

The endpoints return the welcome message, simulated purchase details, and health status. Responses include the Pod hostname.

## Architecture

Client → Port Forwarding → ClusterIP Service → Flask Pods → Single Kubernetes Node

## Key Learnings

- ReplicaSets maintain the desired number of Pods.
- Scaling from three to five replicas creates two additional Pods.
- Deleted Pods are automatically replaced.
- Services provide a stable endpoint for accessing application Pods.
- Multiple Pods can run on one node.
- ReplicaSets do not automatically scale based on traffic.

## Result

The Flask flash-sale application was deployed successfully on Minikube. It was scaled from three to five replicas, its endpoints were tested, and self-healing was verified by deleting a Pod and observing its replacement.
