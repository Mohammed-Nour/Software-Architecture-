import socket
import time

HOST = '127.0.0.1'
PORT = 65432

def measure_response_time(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    start_time = time.time()
    client_socket.sendall(message.encode())
    client_socket.recv(1024)
    end_time = time.time()

    client_socket.close()
    return end_time - start_time

if __name__ == "__main__":
    # Test sending a message
    send_time = measure_response_time("Hello, World!")
    print(f"Response time for sending message: {send_time:.4f} seconds")

    # Test getting message count
    count_time = measure_response_time("/count")
    print(f"Response time for getting message count: {count_time:.4f} seconds")


