
# Client Application

This folder contains the `client.py` script for the chat application. The client connects to the server to send anonymous messages and query the total number of messages.

## Contents

- `client.py`: The main script to connect to the server and send or query messages.

## Getting Started

### Prerequisites

- Python 3.x
- The server must be running before starting the client. Ensure the server's IP and port match the values in `client.py`.

### Usage

1. Navigate to the `client/` directory:
    ```bash
    cd client
    ```

2. Run the client script:
    ```bash
    python client.py
    ```

3. After running, you can:
   - Enter any text to send it as an anonymous message.
   - Type `/count` to request the total number of messages.
   - Type `quit` to exit the client application.

## Customization

- The default server address is set to `127.0.0.1` and port `65432`. Modify the `ChatClient` constructor in `client.py` if you need to connect to a different server.

## Notes

- The client communicates with the server using TCP sockets.
- If the server is not running, the client will fail to connect.
