# Server Application

This folder contains the `server.py` script for the chat application. The server listens for client connections, stores messages, and provides the `/count` endpoint to return the total number of messages.

## Contents

- `server.py`: The main script to start the server and handle client connections.

## Getting Started

### Prerequisites

- Python 3.x

### Usage

1. Navigate to the `server/` directory:
    ```bash
    cd server
    ```

2. Run the server script:
    ```bash
    python server.py
    ```

3. The server will start listening on the default address `127.0.0.1` and port `65432`. It will accept client connections and store anonymous messages.

## Customization

- You can change the server's host and port by modifying the `ChatServer` constructor in `server.py`.

## Notes

- The server is designed to handle multiple clients using multithreading.
- Messages are stored in memory and are not persistent; restarting the server will clear all previous messages.
- The server exposes the `/count` endpoint for clients to query the total number of messages.
"""
