
# Anonymous Chat Application

This is a simple client-server chat application where users can send anonymous messages. The system also supports querying the total number of messages sent and retrieving all previous messages. This project focuses on key software architecture quality attributes like time behavior, recoverability, and maintainability.

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Features](#features)
- [Quality Attribute Scenarios](#quality-attribute-scenarios)
- [Fitness Functions](#fitness-functions)
- [Ideas for Improvement](#ideas-for-improvement)

## Project Structure

The project is structured as follows:

```
/project-root
│
├── client/
│   ├── client.py            # Main client code to connect to the server and send messages
│   └── README.md            # Client-specific README for more details on usage
│
├── server/
│   ├── server.py            # Main server code to handle client connections and messages
│   └── README.md            # Server-specific README for more details on usage
│
├── tests/
│   ├── test_time_behavior.py     # Tests for time behavior scenario
│   ├── test_recoverability.py    # Tests for recoverability scenario
│   ├── test_maintainability.py   # Code complexity and coverage tests
│   └── README.md                # Details on how to run tests
│
├── README.md                # Main project README (this file)
└── requirements.txt         # List of dependencies (if using Python)
```

- **`client/`**: Contains the client code. The `client.py` file allows clients to connect to the server, send messages, and request all previous messages.
- **`server/`**: Contains the server code. The `server.py` file manages client connections, stores messages, and handles broadcasting of messages to all clients.
- **`tests/`**: Includes scripts for testing various quality attributes such as time behavior, recoverability, and maintainability.
- **`requirements.txt`**: Lists the dependencies required to run the project (e.g., `socket`, `threading` for Python).

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages can be installed using:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Server

1. Navigate to the `server/` directory:
   ```bash
   cd server
   ```
2. Run the server:
   ```bash
   python server.py
   ```

### Running the Client

1. Navigate to the `client/` directory:
   ```bash
   cd client
   ```
2. Run the client:
   ```bash
   python client.py
   ```

## Usage

- **Sending Messages**: Once the client is running, type any message to send it anonymously to the server.
- **Message Count**: Type `/count` to retrieve the total number of messages sent.
- **Show All Messages**: Type `/show` to display all previous messages.
- **Exit**: Type `quit` to close the client application.

## Features

1. **Anonymous Messaging**: Users can send messages to a chat room without revealing their identity.
2. **Broadcasting**: The server broadcasts new messages to all connected clients.
3. **Message Count**: Clients can request the total number of messages sent.
4. **Retrieve All Messages**: Clients can request to view all previous messages.
5. **Multi-Client Support**: The server can handle multiple clients simultaneously.

## Quality Attribute Scenarios

The system focuses on the following quality attributes:

1. **Time Behavior**:
   - **Scenario**: When a client sends a message or requests the `/count` endpoint, the system processes and returns a response within 500 milliseconds.
   - **Fitness Function**: A script (`test_time_behavior.py`) measures the response time of these operations to ensure they meet the specified limit.

2. **Recoverability**:
   - **Scenario**: If the server crashes, it should be able to restart within 2 seconds, restoring all previous messages and reconnecting to clients.
   - **Fitness Function**: A script (`test_recoverability.py`) simulates server crashes and measures recovery time.

3. **Maintainability**:
   - **Scenario**: The system's code should be modular and easy to modify. Changes such as adding a new client feature should take no longer than 30 minutes.
   - **Fitness Function**: A script (`test_maintainability.py`) uses `pylint` to check code quality, complexity, and adherence to coding standards.

## Fitness Functions

To run the fitness functions (tests), navigate to the `tests/` directory:

```bash
cd tests
```

### Running the Tests

1. **Time Behavior Test**:
    ```bash
    python test_time_behavior.py
    ```

2. **Recoverability Test**:
    ```bash
    python test_recoverability.py
    ```
    - This test simulates a server crash and attempts to restart it, measuring the recovery time.

3. **Maintainability Test**:
    ```bash
    python test_maintainability.py
    ```
    - This test uses `pylint` to analyze the code for maintainability issues.

## Ideas for Improvement

- **Message Persistence**: Introduce a database to store messages permanently instead of keeping them in memory, so every time users reconnect, history keeps saved.
- **Security**: Implement message encryption to ensure secure communication between clients and the server.
- **User Interface**: Develop a graphical user interface (GUI) (website, telegram bot, etc.) for a more user-friendly client experience.
- **Enhanced Error Handling**: Improve error handling to gracefully manage network issues and client disconnections.
