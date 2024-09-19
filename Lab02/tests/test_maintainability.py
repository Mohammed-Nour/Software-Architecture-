import subprocess
import sys
import os

# Get the directory of this script (tests folder in this case)
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute paths to the server.py and client.py scripts relative to the script's location
server_script_path = '/server/server.py'
client_script_path = '/client/client.py'


def run_maintainability_tests():
    # Determine python command based on platform (using the current interpreter)
    python_command = sys.executable  # This will use the Python interpreter running this script

    print(f"Running pylint for {server_script_path}...")
    try:
        result = subprocess.run([python_command, "-m", "pylint", server_script_path], capture_output=True, text=True)
        print(result.stdout)  # Output Pylint results
        print(result.stderr)  # Print any Pylint errors
    except subprocess.CalledProcessError as e:
        print(f"Error while running pylint on {server_script_path}: {e}")

    print(f"\nRunning pylint for {client_script_path}...")
    try:
        result = subprocess.run([python_command, "-m", "pylint", client_script_path], capture_output=True, text=True)
        print(result.stdout)  # Output Pylint results
        print(result.stderr)  # Print any Pylint errors
    except subprocess.CalledProcessError as e:
        print(f"Error while running pylint on {client_script_path}: {e}")


if __name__ == "__main__":
    run_maintainability_tests()
