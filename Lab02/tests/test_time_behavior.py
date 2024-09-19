import socket
import time

HOST = '127.0.0.1'
PORT = 20_000


def measure_response_time(message):
    # Use time.perf_counter() for better precision
    start_time = time.perf_counter()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.sendall(message.encode())
    client_socket.recv(1024)
    client_socket.close()

    end_time = time.perf_counter()
    return end_time - start_time


if __name__ == "__main__":
    # Test sending a message
    send_time = measure_response_time("Hello, World!")
    print(f"Response time for sending message: {send_time:.6f} seconds")

    # Test getting message count
    count_time = measure_response_time("/count")
    print(f"Response time for getting message count: {count_time:.6f} seconds")
