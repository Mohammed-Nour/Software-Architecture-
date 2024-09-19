"""
Client module for the anonymous chat application.
Connects to the server, sends messages, and listens for broadcasts.
"""

import socket
import threading


class ChatClient:
    """
    A class to represent the chat client.
    Connects to the server, sends messages, and listens for broadcasts.
    """

    def __init__(self, host='127.0.0.1', port=20_000):
        """
        Initializes the ChatClient with a host and port.

        Args:
            host (str): The server's host address.
            port (int): The server's port number.
        """
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Connects to the server and starts the message listening thread.
        """
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")
        # Start a thread to listen for incoming messages
        threading.Thread(target=self.receive_messages).start()

    def send_message(self, message):
        """
        Sends a message to the server.

        Args:
            message (str): The message content.
        """
        self.client_socket.sendall(message.encode())

    def receive_messages(self):
        """
        Listens for incoming messages from the server and displays them.
        """
        while True:
            try:
                server_message = self.client_socket.recv(1024).decode()
                if not server_message:
                    break
                print(f"Server: {server_message}")
            except ConnectionResetError:
                print("Connection to the server was lost.")
                break

    def close(self):
        """
        Closes the connection to the server.
        """
        self.client_socket.close()


if __name__ == "__main__":
    client = ChatClient()
    client.connect()

    while True:
        user_input = input(
            "Enter message ('/count' to get message count,"
            " '/show' to display all messages, 'quit' to exit): "
        )
        if user_input.lower() == 'quit':
            client.close()
            break
        client.send_message(user_input)
