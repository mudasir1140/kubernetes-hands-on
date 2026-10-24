from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Flask App Running",
        "security": "Docker security lab"
    })

@app.route("/read-file")
def read_file():
    try:
        with open("/etc/passwd", "r") as file:
            return jsonify({"content": file.read()})
    except Exception as e:
        return jsonify({"error": str(e)}), 403

@app.route("/run-command")
def run_command():
    import subprocess
    try:
        result = subprocess.run(
            ["/bin/bash", "-c", "echo test"],
            capture_output=True,
            text=True,
            timeout=3
        )
        return jsonify({"output": result.stdout, "error": result.stderr})
    except Exception as e:
        return jsonify({"error": str(e)}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
