#!/bin/bash

echo "Stopping all services..."

# Define process names for services
SERVICES=(
    "api_service.py"
    "filter_service.py"
    "screaming_service.py"
    "publish_service.py"
)

# Stop each service
for SERVICE in "${SERVICES[@]}"; do
    echo "Stopping $SERVICE..."
    pkill -f "$SERVICE" && echo "$SERVICE stopped." || echo "$SERVICE not running."
done

# Stop RabbitMQ container if running
echo "Stopping RabbitMQ container..."
if docker ps | grep -q "rabbitmq"; then
    docker stop rabbitmq && echo "RabbitMQ container stopped." || echo "Failed to stop RabbitMQ container."
else
    echo "RabbitMQ container not running."
fi

# Optional: Clean up RabbitMQ container
echo "Cleaning up RabbitMQ container..."
if docker ps -a | grep -q "rabbitmq"; then
    docker rm rabbitmq && echo "RabbitMQ container removed." || echo "Failed to remove RabbitMQ container."
else
    echo "No RabbitMQ container found to remove."
fi

echo "All services stopped."
