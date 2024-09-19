import time
import socket
import subprocess
import signal
import platform


HOST = '127.0.0.1'
PORT = 20_000
server_process = None  # Global variable to keep track of the server process


def is_server_alive():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        client_socket.close()
        return True
    except ConnectionRefusedError:
        return False


def simulate_crash():
    global server_process
    if server_process:
        print("Simulating server crash...")
        if platform.system() == 'Windows':
            server_process.terminate()  # Graceful termination on Windows
        else:
            server_process.send_signal(signal.SIGTERM)  # Graceful termination on Unix-like systems
        server_process.wait()  # Ensure process is terminated
        server_process = None


def start_server():
    global server_process
    if platform.system() == 'Windows':
        server_process = subprocess.Popen(["python", "../server/server.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        server_process = subprocess.Popen(["python3", "../server/server.py"])


def test_recoverability():
    # Start the server initially
    print("Starting server...")
    start_server()

    # Wait for the server to start
    time.sleep(2)

    # Simulate a crash
    simulate_crash()

    # Wait before restarting the server
    time.sleep(2)
    print("Attempting to restart server...")

    # Restart the server
    start_server()

    # Wait to give the server time to start
    time.sleep(2)

    # Check if the server comes back online
    if is_server_alive():
        print("Server successfully recovered!")
    else:
        print("Server did not recover.")


if __name__ == "__main__":
    test_recoverability()
