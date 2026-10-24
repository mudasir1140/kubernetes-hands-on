# Exercise 7: Jenkins CI Automation

## Aim
To set up Jenkins using Docker and access the Jenkins dashboard to understand the basics of Continuous Integration (CI).

## Tools and Technologies Used
- **Jenkins:** Automation server used for Continuous Integration and Continuous Delivery.
- **Docker:** Platform used to run Jenkins in a container.
- **Windows PowerShell / Ubuntu terminal:** Used to execute Docker commands.
- **Web Browser:** Used to access the Jenkins dashboard.

## Procedure

### Step 1: Verify Docker Installation

Check that Docker is installed and available:

```bash
docker --version
```

### Step 2: Obtain the Jenkins Docker Image

Download the Jenkins Long-Term Support image if required:

```bash
docker pull jenkins/jenkins:lts
```

### Step 3: Run Jenkins in a Docker Container

The standard command for a new installation is:

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
```

**Port mapping:**
- `8080:8080` exposes the Jenkins web interface.
- `50000:50000` is commonly used for inbound Jenkins agent connections.

*Note: Jenkins was already installed in the existing environment, so the existing container was reused instead of creating another one.*

### Step 4: Verify the Container

```bash
docker ps
```

Verify that the Jenkins container is running and the required ports are mapped.

### Step 5: Access Jenkins

Open the following address in a web browser:

http://localhost:8080

Log in to the Jenkins dashboard.

## Result

Successfully deployed Jenkins using Docker and accessed the Jenkins dashboard through a web browser.

## Conclusion

This exercise provided practical experience in running Jenkins inside a Docker container, configuring port mappings, verifying container status, and accessing the Jenkins web interface. Jenkins provides a foundation for automating software builds and Continuous Integration workflows.

## References
- [Jenkins Official Website](https://www.jenkins.io/)
- [Jenkins Docker Image](https://hub.docker.com/r/jenkins/jenkins)
- [Docker Documentation](https://docs.docker.com/)
