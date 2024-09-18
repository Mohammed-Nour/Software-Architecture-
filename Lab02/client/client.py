import socket
import threading

class ChatClient:
    def __init__(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")
        # Start a thread to listen for incoming messages
        threading.Thread(target=self.receive_messages).start()

    def send_message(self, message):
        self.client_socket.sendall(message.encode())

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                print(f"Server: {message}")
            except ConnectionResetError:
                print("Connection to the server was lost.")
                break

    def close(self):
        self.client_socket.close()

if __name__ == "__main__":
    client = ChatClient()
    client.connect()

    while True:
        message = input("Enter message ('/count' to get message count, '/show' to display all messages, 'quit' to exit): ")
        if message.lower() == 'quit':
            client.close()
            break
        client.send_message(message)

