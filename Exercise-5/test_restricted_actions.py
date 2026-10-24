import requests

BASE_URL = "http://localhost:5000"

for path in ["/", "/read-file", "/run-command"]:
    try:
        response = requests.get(BASE_URL + path, timeout=5)
        print(f"\n{path} -> HTTP {response.status_code}")
        print(response.text[:300])
    except requests.RequestException as error:
        print(f"\n{path} -> Request failed: {error}")
