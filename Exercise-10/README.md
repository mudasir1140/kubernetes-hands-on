# Exercise 10: Multi-Node Kubernetes Deployment

## Objective
Deploy Product Catalog and Shopping Cart applications on a three-node Kubernetes cluster using Deployments and Services.

## Cluster
- Cluster name: devops-multinode
- Nodes: 3
- Node status: Ready

## Applications

### Product Catalog
- Replicas: 2
- Image: product-catalog:latest
- Service: product-catalog-service
- API endpoint: /products

### Shopping Cart
- Replicas: 3
- Image: shopping-cart:latest
- Service: shopping-cart-service
- API endpoint: /cart

## Project Files
- Dockerfile.product
- Dockerfile.shopping
- product_catalog.py
- shopping_cart.py
- product_catalog_deployment.yaml
- shopping_cart_deployment.yaml
- product_catalog_service.yaml
- shopping_cart_service.yaml

## Deployment
Run these commands from the Exercise-10 directory:

    kubectl apply -f product_catalog_deployment.yaml
    kubectl apply -f shopping_cart_deployment.yaml
    kubectl apply -f product_catalog_service.yaml
    kubectl apply -f shopping_cart_service.yaml

## Verification

    kubectl get nodes
    kubectl get deployments
    kubectl get pods -o wide
    kubectl get services

Expected replicas: Product Catalog 2/2 and Shopping Cart 3/3.

## API Testing

Product Catalog:

    kubectl port-forward service/product-catalog-service 8081:80
    curl http://127.0.0.1:8081/products

Shopping Cart:

    kubectl port-forward service/shopping-cart-service 8082:80
    curl http://127.0.0.1:8082/cart

To add a product, use another terminal:

    curl -X POST http://127.0.0.1:8082/cart -H "Content-Type: application/json" -d '{"id":1,"name":"Laptop","quantity":1}'

## Results
Both applications have been deployed with the specified replica counts and their APIs have been tested using port forwarding and curl.

## Note
Shopping Cart stores data in memory. Cart contents may be lost after a pod restart or differ between replicas.
