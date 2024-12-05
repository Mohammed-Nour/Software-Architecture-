# **Performance Test Report**

## **Summary**

The performance tests evaluated two systems: **Inter-Process Communication (IPC) (pipes-and-filters)** and **RabbitMQ(Event-Driven)**. Below are the key observations:

- **IPC** generally outperformed RabbitMQ in terms of requests per second and response times, especially under low concurrency.
- RabbitMQ handled higher concurrency and stress better but at the cost of higher latency and lower throughput.

---

## **Load Testing Results**

| Concurrency | Metric                 | IPC (Port 6000)         | RabbitMQ (Port 5000)    |
|-------------|------------------------|-------------------------|-------------------------|
| **1 User**  | Requests/sec           | 72.00                  | 32.06                  |
|             | Avg Time per Request   | 13.889 ms              | 31.193 ms              |
| **10 Users**| Requests/sec           | 305.88                 | 53.23                  |
|             | Avg Time per Request   | 3.269 ms               | 187.869 ms             |
| **50 Users**| Requests/sec           | Failed (117 requests)   | 52.46                  |
|             | Avg Time per Request   | N/A                    | 19.062 ms              |
| **100 Users**| Requests/sec          | Failed                 | 54.12                  |
|             | Avg Time per Request   | N/A                    | 18.476 ms              |
| **500 Users**| Requests/sec          | Failed                 | 49.73                  |
|             | Avg Time per Request   | N/A                    | 20.107 ms              |

---

## **Stress Testing Results**

| Metric                   | IPC (Port 6000)         | RabbitMQ (Port 5000)    |
|--------------------------|-------------------------|-------------------------|
| Requests/sec (1000 reqs) | Failed                 | 36.39                  |
| Avg Time per Request      | N/A                    | 5495.760 ms            |

---

## **Latency Testing Results**

| Metric                   | IPC (Port 6000)         | RabbitMQ (Port 5000)    |
|--------------------------|-------------------------|-------------------------|
| Avg Latency (1 user)     | Timeout                | 31.263 ms              |
| Throughput (100 users)   | N/A                    | 50.97 [#/sec]          |

---

## **Analysis**

1. **Throughput and Requests Per Second**:
   - IPC outperformed RabbitMQ significantly at lower concurrency levels. 
   - RabbitMQ provided better stability at higher concurrency but had slightly lower throughput compared to IPC when tested with smaller user loads.

2. **Latency**:
   - IPC demonstrated better latency under low-concurrency scenarios. However, it started failing under moderate to high concurrency.

3. **Fault Tolerance**:
   - IPC struggled with higher concurrency levels and stress tests, failing to process all requests.
   - RabbitMQ maintained consistent performance even under stress tests, showing higher resilience and better fault tolerance.

---

## **Recommendations**

1. **When to Use IPC**:
   - Suitable for low-latency and low-concurrency applications.
   - Ideal for systems where components are closely coupled, and low overhead is critical.

2. **When to Use RabbitMQ**:
   - Recommended for high-concurrency or distributed systems.
   - Offers better scalability and fault tolerance for systems with unpredictable load patterns.
