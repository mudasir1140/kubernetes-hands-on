import subprocess
import sys

print("Checking AppArmor status...")

status = subprocess.run(
    ["sudo", "aa-status"],
    capture_output=True,
    text=True
)

print(status.stdout)
print(status.stderr)

if "apparmor filesystem is not mounted" in (
    status.stdout + status.stderr
).lower():
    print("\nWARNING: AppArmor is not available in this WSL environment.")
    print("Profile enforcement cannot be verified here.")
else:
    print("\nReview the AppArmor status above before continuing.")

print("\nBuilding Docker image...")
result = subprocess.run(["docker", "build", "-t", "flask-apparmor", "."])

if result.returncode != 0:
    sys.exit(result.returncode)

print("\nDocker image build completed.")
print("This does not prove AppArmor profile enforcement.")
