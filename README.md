# Docker Workshop

This repository is part of the **Data Engineering ZoomCamp - January 2026**. It has been created for self-learning and practicing Docker-related concepts for Data Engineering.

- **Original Content**: [Data Engineering ZoomCamp Docker Workshop](https://github.com/alexeygrigorev/workshops/tree/main/dezoomcamp-docker)
- **YouTube Playlist**: [ZoomCamp Docker Playlist](https://www.youtube.com/watch?v=lP8xXebHmuE&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=3)

---

## Folder Structure

### `test`
Demonstrates the usage of **Volumes** with Docker containers, including the execution of a Python program within a Docker container.

### `pipeline_test`
Demonstrates the usage of a Dockerized data pipeline, including the execution of a data pipeline within a Docker container. Dependencies installed include `pandas` and `pyarrow`.

### `pipeline`
Demonstrates inserting data from one Dockerized container (running the Python script `taxi_ingest:v001`) into another Docker container running PostgreSQL (`postgres:18`). The target table is `yellow_taxi_data`. Both containers are within the same network (`pg-network`).

### `SQL-refresher`
Demonstrates inserting data from one Dockerized container (running the Python script `taxi_zone_lookup:nyc_taxi_zone_lookup`) into another Docker container running PostgreSQL (`postgres:18`). The target table is `zones`. Both containers are within the same network (`pg-network`).

### `homework1_docker_sql`
Contains the homework assignment listed here: [Homework 1 - Docker and SQL](https://courses.datatalks.club/de-zoomcamp-2026/homework/hw1).
