import socket
import threading
from datetime import datetime
from typing import List, Tuple


class ChatServer:
    def __init__(self, host: str = '127.0.0.1', port: int = 20_000):
        self.host = host
        self.port = port
        self.server_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Enable SO_REUSEADDR to allow socket reuse
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.messages: List[Tuple[str, datetime]] = []
        self.clients: List[socket.socket] = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, _ = self.server_socket.accept()
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket: socket.socket):
        self.send_all_messages(client_socket)

        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                if message == '/count':
                    count = len(self.messages)
                    client_socket.sendall(f"Total messages: {count}".encode())
                elif message == '/show':
                    self.send_all_messages(client_socket)
                else:
                    self.add_message(message)
                    self.broadcast_message(f"New message: {message}")
            except (ConnectionResetError, BrokenPipeError):
                break

        self.clients.remove(client_socket)
        client_socket.close()

    def add_message(self, content: str):
        timestamp = datetime.now()
        self.messages.append((content, timestamp))

    def send_all_messages(self, client_socket: socket.socket):
        for content, timestamp in self.messages:
            try:
                message = f"[{timestamp}] {content}"
                client_socket.sendall(message.encode())
                threading.Event().wait(0.1)
            except (ConnectionResetError, BrokenPipeError):
                print("Failed to send messages to a client. Removing client.")
                self.clients.remove(client_socket)
                break

    def broadcast_message(self, message: str):
        for client in self.clients:
            try:
                client.send(message.encode())
            except (ConnectionResetError, BrokenPipeError):
                print("Failed to broadcast message to a client. Removing client.")
                self.clients.remove(client)


if __name__ == "__main__":
    server = ChatServer()
    server.start()
