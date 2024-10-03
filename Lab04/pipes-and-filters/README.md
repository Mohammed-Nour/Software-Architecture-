# Pipes-and-Filters Video Processing Application

This application demonstrates a video processing pipeline based on the pipes-and-filters architectural pattern, as described in [BCK13]. It captures a video stream from the webcam and processes each frame in real-time through a series of filters.

## Features

The following filters are applied sequentially:
1. **Grayscale**: Converts each frame to black and white.
2. **Mirror**: Horizontally flips each frame.
3. **Resize**: Reduces the frame size to 50% of the original.
4. **Edge Detection**: Detects edges in the frame to highlight significant features.

## Project Structure

- `filters/`: Contains the modules for each filter.
- `main.py`: The main script to capture and process the video stream.
- `requirements.txt`: Lists the required dependencies for the project.

## How to Run

### Prerequisites
- Python 3.x installed on your system.
- A working webcam (or a video file can be substituted for input if desired).

### Setup
1. **Clone the Repository**
    ```bash
    git clone <repository_url>
    cd pipes-and-filters
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**
    ```bash
    python main.py
    ```
    The application will start capturing the video from your webcam and apply the filters sequentially in real-time. Press `q` to exit.

## Cardinality
The design ensures that each filter is isolated and can be used independently. The order and number of filters (or "cardinality") can be modified easily by adjusting the sequence of function calls in `main.py`.

## Codebase Organization

1. **Separation of Concerns**: Each filter is encapsulated within its own module, allowing for easy reuse, testing, and maintenance.
2. **Naming and Structure**: File and folder names are clear and descriptive. The `README.md` provides setup instructions and an overview of the project.

## Video Demonstration
You can find a demonstration video showing the real-time video processing and effects [here](#). (Replace `#` with the actual link to your demo video).
