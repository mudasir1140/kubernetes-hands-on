# Exercise 4: Docker Networking with Multiple Containers

## 1. Objective

Understand Docker container networking by creating a custom bridge network and running multiple containers that communicate with each other.

This exercise demonstrates:
- Creating and inspecting a custom Docker bridge network.
- Running Flask, MySQL, and Redis containers.
- Container-to-container communication.
- Docker's internal DNS-based service discovery.
- Publishing a container port to the host system.
- Verifying network connectivity.

## 2. Technologies Used

- Docker
- Docker Bridge Networking
- Python 3.9
- Flask
- MySQL 8.0
- Redis

## 3. Project Structure

```text
Exercise-4/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## 4. Flask REST API

A simple REST API was developed using Flask. The application provides an `/about` endpoint that returns information about the API in JSON format.

The application listens on port `5001` and uses `0.0.0.0` so that it is accessible from outside the container.

Example response:

```json
{
  "description": "This is a simple REST API built with Flask.",
  "name": "Simple REST API",
  "version": "1.0"
}
```

## 5. Build the Docker Image

The Flask application was containerized using the provided Dockerfile.

```bash
docker build -t flask-api .
```

The image was successfully built with the name `flask-api`.

## 6. Create a Custom Bridge Network

Create the network:

```bash
docker network create --driver bridge my-bridge-net
```

Verify the network:

```bash
docker network ls
```

Inspect its configuration:

```bash
docker network inspect my-bridge-net
```

The network uses Docker's `bridge` driver and provides an isolated virtual network for the connected containers.

## 7. Launch the Containers

### MySQL container

```bash
docker run -d \
  --name mysql \
  --network my-bridge-net \
  -e MYSQL_ROOT_PASSWORD=LabRoot123! \
  mysql:8.0
```

MySQL listens on port `3306`.

### Redis container

```bash
docker run -d \
  --name redis \
  --network my-bridge-net \
  redis:latest
```

Redis listens on port `6379`.

### Flask container

```bash
docker run -d \
  --name flask \
  --network my-bridge-net \
  -p 5001:5001 \
  flask-api
```

The Flask API listens on port `5001`, which is published to the host system.

Verify that the containers are running:

```bash
docker ps
```

## 8. Docker Network Architecture

All three containers are connected to the same custom bridge network, `my-bridge-net`.

```text
                 my-bridge-net
                       |
          +------------+------------+
          |            |            |
          v            v            v
      +--------+   +--------+   +--------+
      | Flask  |   | MySQL  |   | Redis  |
      | :5001  |   | :3306  |   | :6379  |
      +--------+   +--------+   +--------+
          |
          v
    Host: localhost:5001
```

The Flask API is accessible from the host through port mapping. The containers can communicate over the bridge network using their container names and service ports.

## 9. Docker DNS and Container Name Resolution

Docker provides automatic name resolution for containers connected to the same user-defined bridge network.

Instead of relying on changing IP addresses, containers can use names such as `mysql` and `redis`.

Test name resolution from the Flask container:

```bash
docker exec flask python -c "import socket; print('MySQL:', socket.gethostbyname('mysql')); print('Redis:', socket.gethostbyname('redis'))"
```

Verified results:

- MySQL: `172.18.0.2`
- Redis: `172.18.0.3`
- Flask: `172.18.0.4`

These IP addresses are specific to this run and may change if the containers are recreated.

## 10. Test Container Connectivity

Test TCP connectivity from Flask to MySQL and Redis:

```bash
docker exec flask python -c "import socket; s=socket.create_connection(('mysql',3306),5); print('MySQL connection successful'); s.close(); s=socket.create_connection(('redis',6379),5); print('Redis connection successful'); s.close()"
```

Verified output:

```text
MySQL connection successful
Redis connection successful
```

This confirms that the Flask container can resolve the container names and establish TCP connections to the MySQL and Redis listening ports.

Note: These tests verify network connectivity. The Flask application does not currently execute database queries or Redis cache operations.

## 11. Test the Flask API

Run:

```bash
curl http://localhost:5001/about
```

The endpoint returned the expected JSON response:

```json
{
  "description": "This is a simple REST API built with Flask.",
  "name": "Simple REST API",
  "version": "1.0"
}
```

## 12. Network Verification

Inspect the network:

```bash
docker network inspect my-bridge-net
```

The inspection confirmed that the following containers were attached:

- `flask`
- `mysql`
- `redis`

All three containers received IP addresses from the bridge network's subnet.


## 13. Cleanup

After completing the demonstration, stop and remove the containers:

```bash
docker stop flask mysql redis
docker rm flask mysql redis
```

Remove the custom network:

```bash
docker network rm my-bridge-net
```

These commands remove the lab containers and network. The Docker image and project files remain.

## 14. Result

The Docker networking exercise was successfully completed. A custom bridge network was created, and Flask, MySQL, and Redis containers were connected to it.

The Flask API was tested successfully, Docker DNS resolved the MySQL and Redis container names, and TCP connectivity to both services was verified.

The exercise demonstrated custom bridge networking, container-name resolution, multi-container communication, and host port publishing.
