# Trade-off analysis: Databases
## Software Architecture | Fall 2024  
### Team members: Mohamad Nour Shahin, Ali Hamdan, Yehia Sobeh, Kamil Mirgasimov 

---

## 1. Short description 
- **PostgreSQL**: a powerful, open-source, object-relational database system that extends the SQL language with advanced features. PostgreSQL is known for its robustness, supporting complex data workloads, and high scalability while ensuring data integrity.

- **SQLite**: a C-language-based library that provides a lightweight, fast, and self-contained SQL database engine. It is renowned for being highly reliable, full-featured, and is one of the most widely used database engines globally.

- **MongoDB**: a document-oriented, NoSQL database that stores data in flexible, JSON-like documents. This model allows for greater flexibility compared to traditional relational databases, making it popular for dynamic and unstructured data.

- **InfluxDB**: an open-source time-series database, highly optimized for fast storage and retrieval of time-stamped data. InfluxDB is widely used in monitoring, IoT, and real-time analytics applications.

- **Redis**: an open-source, in-memory data store that functions as a database, cache, and message broker. It is highly performant and is often used for caching purposes to reduce server load, with the ability to handle complex data structures.

- **Plain Files**: a basic storage system where data is stored as human-readable text in files. While it is extremely simple, it lacks the sophistication and features found in modern database systems, making it suitable for small, lightweight applications.

---
## 2. Pros and cons

- **PostgreSQL**
    - **Pros**:
        - transactional DDL (INSERT, DELETE, etc.)
        - code comments
        - open source
        - huge community support
    - **Cons**
        - slow performance
        - difficulties with backup recovery
- **SQLite**
    - **Pros**: 
        - lightweight and portable
        - ACID complaint
        - free and open-source
    - Cons:
        - not suitable for large scale apps
        - lack of security features.
- **MongoDB**
    - **Pros**:
        - performance
        - simplicity
        - scalability
        - documentation
    - Cons:
        - does not support transactions,
        - less flexibity with querying (e.g. no JOINs)
        - data size is typically higher.
- **InfluxDB**
  - **Pros**:
    - high performance
    - scalability
    - easy to use
  - **Cons**: 
    - Proprietary software, need to pay for some functionalities
    - Does not support transactions
- **Redis**
    - **Pros**:
        - performance
        - do not need to learn SQL to use it
        - adaptable (can accomodate most data structures)
    - Cons:
        - needs a lot of memory and CPU
        - no relational data integrity features
- **Plain Files**
    - **Pros**
        - simplicity
        - fits into anything
        - small size 
    - **Cons**:
        - not appropriate for big data
        - huge security problems
---


## 3. Comparison table
| Database | Read performance | Write performance | Data model | Data сonsistency
| ------ | ----------- | ----------- | ----------- | ----------- |
| PostgreSQL | High with indexing | High | Relational | Strong
| SQLite | High for small databases | Medium | Relaional | Strong |
| MongoDB | High for documents | High | Document-based | Eventual |
| InfluxDB | High for time queries | Good for time-series writes | Time-series | Eventual |
| Redis | Extremely high | Extremely high | Key-value (in-memory) | A signle instance is strongly consistent, many istances do not guarantee strong consistency
| Plain file | High for small files, but slow for large ones | Low | Custom, file-based | No consistency management |

---
## 4. Examples

- PostgreSQL.
    - *Banking system*. Since strong ACID properties ensure transactional integrity for financial data.
- SQLite.
    - *Offline note-taking app*. Ideal for single-user apps with simple and not big local data storage needs.
- MongoDB.
    - *Real estate listing platform*. Handles diverse and changing property data with flexible schema.
- InfluxDB.
    - *Server performance monitoring*. Perfect for capturing and analyzing time-series metrics like CPU usage.
- Redis. 
    - *Leaderboard system for games*. Fast in-memory storage allows real-time ranking updates.
- Plain file. 
    - *Configurations storage*. Simple and efficient for reading/writing app configurations.
---


