
# Event-Driven and Pipes-and-Filters Simulations with Docker Compose

We have created two separate systems to simulate **Event-Driven Architecture** and **Pipes-and-Filters Architecture**:

- **Event-Driven Architecture** is accessible on port `5000`.  
- **Pipes-and-Filters Architecture** is accessible on port `6000`.

## Getting Started

To build and run the systems using Docker Compose, execute the following command in your terminal:

```bash
docker-compose down && docker-compose build --no-cache && docker-compose up
```

## Testing the Systems

### 1. Valid Test Case

This test sends a valid message that doesn't contain any stop words.

#### Event-Driven Architecture (Port 5000):

```
curl -X POST -H "Content-Type: application/json" \
-d '{"alias": "user1", "text": "This is a valid message!"}' \
http://127.0.0.1:5000/submit_message
```

#### Pipes-and-Filters Architecture (Port 6000):

```
curl -X POST -H "Content-Type: application/json" \
-d '{"alias": "user1", "text": "This is a valid message!"}' \
http://127.0.0.1:6000/submit_message
```

---

### 2. Invalid Test Case

This test sends a message containing a stop word (`"mango"`) and verifies it gets filtered out.

#### Event-Driven Architecture (Port 5000):

```
curl -X POST -H "Content-Type: application/json" \
-d '{"alias": "user1", "text": "I love mango smoothies!"}' \
http://127.0.0.1:5000/submit_message
```

#### Pipes-and-Filters Architecture (Port 6000):

```
curl -X POST -H "Content-Type: application/json" \
-d '{"alias": "user1", "text": "I love mango smoothies!"}' \
http://127.0.0.1:6000/submit_message
```

---

## Performance Testing

We conducted performance tests using **Apache Bench** to measure the following metrics for both architectures:

1. **Latency**  
2. **Stress**  
3. **Concurrency**  
4. **Throughput**  

The tests were automated using a script: [run_performance_tests.sh](run_performance_tests.sh).

To execute the performance tests, run:

```
 run_performance_tests.sh
```

The script will provide a  performance report comparing both architectures.

---

## Results

The results from the performance tests include:

- **Load Test**
- **Latency Test**
- **Stress Test**


The detailed results are documented in [Performance Results](Performance_test_report).

---

## Project Structure
```
├── event-driven 
│    ├── services/
│    │   ├── api_service/
│    │   │   ├── api_service.py
│    │   │   ├── Dockerfile
│    │   │   ├── requirements.txt
│    │   ├── filter_service/
│    │   │   ├── filter_service.py
│    │   │   ├── Dockerfile
│    │   │   ├── requirements.txt
│    │   ├── publish_service/
│    │   │   ├── publish_service.py
│    │   │   ├── config.ini
│    │   │   ├── Dockerfile
│    │   │   ├── requirements.txt
│    │   ├── screaming_service/
│    │       ├── screaming_service.py
│    │       ├── Dockerfile
│    │       ├── requirements.txt
├── pipes-and-filters/
│   ├── app.py
│   ├── config.ini
│   ├── Dockerfile
│   ├── requirements.txt
├── docker-compose.yml
├── Performance_test_report.md
├── README.md
└── run_performance_tests.sh
```

## Event-Driven Architecture Structure

The Event-Driven system follows this hierarchical structure:

```
Event-Driven Architecture
├── API Service
│   ├── Receives messages from users.
│   ├── Sends messages to the RabbitMQ queue (`filter_queue`).
├── Filter Service
│   ├── Consumes messages from the RabbitMQ queue (`filter_queue`).
│   ├── Filters out messages containing stop words.
│   ├── Sends valid messages to the RabbitMQ queue (`screaming_queue`).
├── Screaming Service
│   ├── Consumes messages from the RabbitMQ queue (`screaming_queue`).
│   ├── Converts message text to uppercase.
│   ├── Sends updated messages to the RabbitMQ queue (`publish_queue`).
├── Publish Service
    ├── Consumes messages from the RabbitMQ queue (`publish_queue`).
    ├── Sends the messages to a preconfigured email address.
```

This structure enables an asynchronous, loosely coupled system where each service is responsible for a single task.
