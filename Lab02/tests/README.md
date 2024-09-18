# Tests for Chat Application

This folder contains the test scripts for evaluating the quality attributes of the chat application, focusing on time behavior, recoverability, and maintainability.

## Contents

- `test_time_behavior.py`: Tests the response time for sending messages and querying the message count.
- `test_recoverability.py`: Simulates a server crash and measures the server's ability to recover.
- `test_maintainability.py`: Analyzes code complexity and adherence to coding standards using `pylint`.

## Prerequisites

- Python 3.x
- `pylint` for code analysis:
    ```bash
    pip install pylint
    ```
- The server must be running before running `test_time_behavior.py`.

## Usage

### Running the Tests

1. Navigate to the `tests/` directory:
    ```bash
    cd tests
    ```

2. **Time Behavior Test:**
    - Run the script to measure the time it takes to send messages and query the message count:
    ```bash
    python test_time_behavior.py
    ```

3. **Recoverability Test:**
    - Simulate a server crash and test its ability to recover:
    ```bash
    python test_recoverability.py
    ```
    - Note: This test will attempt to terminate the server process and restart it. Ensure you save any work before running this script.

4. **Maintainability Test:**
    - Analyze the code's complexity and adherence to standards using `pylint`:
    ```bash
    python test_maintainability.py
    ```

## Notes

- **Time Behavior Test**: Requires a running server to measure response times.
- **Recoverability Test**: Uses commands specific to Unix-based systems (`pkill` and `python3`). Adjust the script if using a different OS.
- **Maintainability Test**: Uses `pylint` for static code analysis.
"""
