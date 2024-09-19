import subprocess
import sys


def run_maintainability_tests():
    # Determine python command based on platform
    python_command = sys.executable  # This will use the Python interpreter running this script

    print("Running pylint for server.py...")
    try:
        subprocess.run([python_command, "-m", "pylint", "../server/server.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running pylint on server.py: {e}")

    print("\nRunning pylint for client.py...")
    try:
        subprocess.run([python_command, "-m", "pylint", "../client/client.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running pylint on client.py: {e}")


if __name__ == "__main__":
    run_maintainability_tests()
