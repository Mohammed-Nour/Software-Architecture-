"""
This module implements a simple chat server.

The `ChatServer` class handles multiple client connections, allowing
clients to send messages, broadcast them to all connected clients,
and retrieve a history of messages.
"""

import socket
import threading
from datetime import datetime
from typing import List, Tuple


class ChatServer:
    """
    A chat server that manages client connections and message broadcasting.

    The server listens for incoming client connections and handles the
    transmission of messages between clients. Clients can retrieve the
    message history, send new messages, and broadcast them to all clients.
    """

    def __init__(self, host: str = '127.0.0.1', port: int = 20_000):
        """
        Initializes the chat server with a specific host and port.

        Args:
            host (str): The IP address of the host. Defaults to '127.0.0.1'.
            port (int): The port number. Defaults to 20,000.
        """
        self.host = host
        self.port = port
        self.server_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Enable SO_REUSEADDR to allow socket reuse
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.messages: List[Tuple[str, datetime]] = []
        self.clients: List[socket.socket] = []

    def start(self):
        """
        Starts the chat server and begins listening for client connections.

        This function binds the server socket to the specified host and port,
        then listens for incoming client connections. Each client is handled
        in a separate thread.
        """
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, _ = self.server_socket.accept()
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket: socket.socket):
        """
        Handles an individual client connection.

        This function receives messages from the client, processes special
        commands like `/count` and `/show`, and broadcasts new messages to
        all connected clients.

        Args:
            client_socket (socket.socket): The client's socket connection.
        """
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
        """
        Adds a new message to the server's message history.

        Args:
            content (str): The message content to be added.
        """
        timestamp = datetime.now()
        self.messages.append((content, timestamp))

    def send_all_messages(self, client_socket: socket.socket):
        """
        Sends the entire message history to a connected client.

        Args:
            client_socket (socket.socket): The client's socket connection.
        """
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
        """
        Broadcasts a message to all connected clients.

        Args:
            message (str): The message to broadcast to all clients.
        """
        for client in self.clients:
            try:
                client.send(message.encode())
            except (ConnectionResetError, BrokenPipeError):
                print("Failed to broadcast message to a client. Removing client.")
                self.clients.remove(client)


if __name__ == "__main__":
    server = ChatServer()
    server.start()
