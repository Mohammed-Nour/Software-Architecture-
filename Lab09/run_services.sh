#!/bin/bash

# Set up the script to exit on error
set -e

# Define variables
RABBITMQ_CONTAINER_NAME="rabbitmq"
RABBITMQ_IMAGE="rabbitmq:3-management"
RABBITMQ_PORT="5672"
RABBITMQ_UI_PORT="15672"
VENV_DIR="venv"

echo "### Starting Setup ###"

# Step 1: Pull and Run RabbitMQ
echo "Pulling RabbitMQ image..."
docker pull $RABBITMQ_IMAGE

echo "Starting RabbitMQ container..."
if docker ps -a --format '{{.Names}}' | grep -q "^$RABBITMQ_CONTAINER_NAME$"; then
    echo "RabbitMQ container already exists. Restarting..."
    docker start $RABBITMQ_CONTAINER_NAME
else
    docker run -d --name $RABBITMQ_CONTAINER_NAME -p $RABBITMQ_PORT:$RABBITMQ_PORT -p $RABBITMQ_UI_PORT:$RABBITMQ_UI_PORT $RABBITMQ_IMAGE
fi

# Wait for RabbitMQ to initialize
echo "Waiting for RabbitMQ to initialize..."
sleep 10

# Step 2: Set Up Python Virtual Environment
echo "Setting up Python virtual environment..."
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv $VENV_DIR
fi

source $VENV_DIR/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 3: Ensure Configuration for Publish Service
# echo "Checking configuration for Publish Service..."
# CONFIG_FILE="services/publish_service/config.json"
# if [ ! -f "$CONFIG_FILE" ]; then
#     echo "Creating default config.json in publish_service..."
#     cat > $CONFIG_FILE <<EOF
# {
#   "smtp_host": "smtp.gmail.com",
#   "smtp_port": 587,
#   "email": "your_email@gmail.com",
#   "password": "your_password"
# }
# EOF
#     echo "Please update $CONFIG_FILE with your email credentials."
#     exit 1
# fi

# Step 4: Run Services
echo "Starting services..."
LOGS_DIR="logs"
mkdir -p $LOGS_DIR

echo "Running API Service..."
# nohup python3 services/api_service/test_filters.py > $LOGS_DIR/api_service.log 2>&1 &

# echo "Running Filter Service..."
# nohup python3 services/filter_service/filter_service.py > $LOGS_DIR/filter_service.log 2>&1 &

# echo "Running Screaming Service..."
# nohup python3 services/screaming_service/screaming_service.py > $LOGS_DIR/screaming_service.log 2>&1 &

# echo "Running Publish Service..."
# nohup python3 services/publish_service/publish_service.py > $LOGS_DIR/publish_service.log 2>&1 &
gnome-terminal -- bash -c "python3 services/api_service/api_service.py; exec bash" &
gnome-terminal -- bash -c "python3 services/filter_service/filter_service.py; exec bash" &
gnome-terminal -- bash -c "python3 services/screaming_service/screaming_service.py; exec bash" &
gnome-terminal -- bash -c "python3 services/publish_service/publish_service.py; exec bash" &

# Display RabbitMQ Management UI Info
echo "### RabbitMQ is running ###"
echo "RabbitMQ UI: http://localhost:$RABBITMQ_UI_PORT"
echo "Default credentials: guest / guest"

echo "### All services started successfully! ###"
echo "Logs are available in the logs/ directory."
