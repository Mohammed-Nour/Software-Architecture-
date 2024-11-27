
# Twitter-Like System with Docker Compose

This project implements a simple Twitter-like system using multiple services, orchestrated by Docker Compose. The services include user registration, posting messages, and liking messages.

## Prerequisites

- Docker
- Docker Compose

## How to Run the Application

1. **Build and Start the Services**  
   Use the following command to build and start the services:
   ```bash
   sudo docker-compose up --build
   ```

2. **Shut Down the Services**  
   To stop and remove the containers, network, and volumes, use:
   ```bash
   sudo docker-compose down
   ```
3. **If you rebuild the image and and Error occure use this command**
   ```bash
   sudo docker system prune
   ```

## API Endpoints

### 1. Register a User

Register a new user with a `POST` request to the registration service.
```bash
curl -X POST http://localhost:5000/register \
-H "Content-Type: application/json" \
-d '{"username": "yehia"}'
```

### 2. Attempt to Post with Unregistered User

This will attempt to post a message using a non-registered username (this should fail).
```bash
curl -X POST http://localhost:5001/post \
-H "Content-Type: application/json" \
-d '{"username": "yeh", "content": "This should not work"}'
```

### 3. Post a Message

Post a message from a registered user.
```bash
curl -X POST http://localhost:5001/post \
-H "Content-Type: application/json" \
-d '{"username": "yehia", "content": "This is my first message!"}'
```

### 4. View Feed

Fetch all messages from the feed.
```bash
curl http://localhost:5001/feed
```

### 5. Like a Message

Like a specific message by its ID.
```bash
curl -X POST http://localhost:5002/like \
-H "Content-Type: application/json" \
-d '{"message_id": "1"}'
```

### 6. View Likes for a Message

Check how many likes a specific message has received.
```bash
curl http://localhost:5002/likes/1
```

### 7. Post Additional Messages

Post more messages from the registered user.
```bash
curl -X POST http://localhost:5001/post \
-H "Content-Type: application/json" \
-d '{"username": "yehia", "content": "Second message"}'

curl -X POST http://localhost:5001/post \
-H "Content-Type: application/json" \
-d '{"username": "yehia", "content": "Third message"}'
```

### 8. View Updated Feed

Fetch the updated feed to see all posted messages.
```bash
curl http://localhost:5001/feed
```

### 9. Like Another Message

Like the second message by its ID.
```bash
curl -X POST http://localhost:5002/like \
-H "Content-Type: application/json" \
-d '{"message_id": "2"}'
```

### 10. View Likes for the Second Message

Check how many likes the second message has received.
```bash
curl http://localhost:5002/likes/2
```


