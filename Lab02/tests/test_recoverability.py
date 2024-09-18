import os
import time
import socket

HOST = '127.0.0.1'
PORT = 65432

def is_server_alive():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        client_socket.close()
        return True
    except ConnectionRefusedError:
        return False

def simulate_crash():
    print("Simulating server crash...")
    os.system("pkill -f server.py")  # This command may vary based on OS

def test_recoverability():
    # Simulate a crash
    simulate_crash()

    # Wait for a bit before restarting the server
    time.sleep(2)
    print("Attempting to restart server...")
    os.system("python3 ../server/server.py &")  # Start the server in the background

    # Check if the server comes back online
    time.sleep(2)
    if is_server_alive():
        print("Server successfully recovered!")
    else:
        print("Server did not recover.")

if __name__ == "__main__":
    test_recoverability()

