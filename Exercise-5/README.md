# Exercise 5: Docker Security with AppArmor and Python

## Objective
Build a Flask application in Docker and explore container security using AppArmor and Python-based tests.

## Project Files
- `app.py` — Flask application with three endpoints.
- `Dockerfile` — Builds the `flask-apparmor` Docker image.
- `my-apparmor-profile` — AppArmor profile for testing.
- `apply_apparmor.py` — Checks AppArmor status and builds the Docker image.
- `test_restricted_actions.py` — Tests the Flask endpoints.

## Requirements
- Docker
- Python 3
- Flask
- Python `requests` package for the test script
- AppArmor-enabled Linux host for actual AppArmor enforcement

## Build the Docker Image

```bash
docker build -t flask-apparmor .
```

## Run the Application

```bash
docker run --rm -p 5000:5000 flask-apparmor
```

Open another terminal and test:

```bash
curl http://localhost:5000/
curl http://localhost:5000/read-file
curl http://localhost:5000/run-command
```

## AppArmor Profile Test

Check AppArmor status:

```bash
sudo aa-status
```

Attempt to load the profile:

```bash
sudo apparmor_parser -r my-apparmor-profile
```

On an AppArmor-enabled Linux host, load and verify the profile before running the container with:

```bash
docker run --rm \
  --security-opt="apparmor=my-apparmor-profile" \
  -p 5000:5000 \
  flask-apparmor
```

## Python Tests

Install the `requests` package in your Python environment, then run:

```bash
python3 test_restricted_actions.py
```

Run the status-check and image-build script with:

```bash
python3 apply_apparmor.py
```

## Results and Environment Limitation

The Docker image built successfully, and the Flask endpoints responded successfully in WSL Ubuntu 24.04.

The `/read-file` endpoint was able to read `/etc/passwd`, and `/run-command` successfully executed Bash. These results show that the tested operations were permitted in this environment.

The AppArmor status command reported that the AppArmor module was loaded but the AppArmor filesystem was not mounted. The profile parser also could not load the profile. Therefore, AppArmor enforcement was **not verified** in this WSL environment.

For a valid AppArmor restriction test, use a Linux host with AppArmor active, load the profile successfully, verify that it is attached to the container, and repeat the endpoint tests.

## Conclusion

The Flask application and Docker image were created and tested. The AppArmor enforcement portion remains pending verification on a supported Linux environment.
