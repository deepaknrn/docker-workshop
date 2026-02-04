
## Setup

1. Navigate to the directory:
   ```bash
   cd SQL-refresher
   ```

2. Initialize the Python project:
   ```bash
   uv init --python 3.13
   uv run python -V
   ```

3. Install dependencies:
   ```bash
   uv add pandas sqlalchemy psycopg2-binary tqdm click
   ```

4. View available options:
   ```bash
   uv run ingest_taxi_zone_lookup.py --help
   ```


# NYC Taxi Zone Lookup Data Ingestion

## Overview
This service ingests NYC taxi zone lookup data into a PostgreSQL database using Docker.

## Building the Docker Image

```bash
docker build -t taxi_zone_lookup:nyc_taxi_zone_lookup .
```

docker run -it --rm \
  --network=pg-network \
  taxi_zone_lookup:nyc_taxi_zone_lookup \
  --pg-user root \
  --pg-password root \
  --pg-host pg-database \
  --pg-port 5432 \
  --pg-db ny_taxi \
  --target-table zones \
  --chunksize 100000

## Check if the postgres container is running :
docker ps 

## Find out what network they're on:
docker inspect pipeline-pg-database-1 | grep -A 5 "Networks"

## Expected output 
@deepaknrn ➜ /workspaces/docker-workshop/SQL-refresher (main) $ docker inspect pipeline-pg-database-1 | grep -A 5 "Networks"
            "Networks": {
                "pipeline_pg-network": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "pipeline-pg-database-1",
@deepaknrn ➜ /workspaces/docker-workshop/SQL-refresher (main) $ docker inspect pipeline-pgadmin-1 | grep -A 5 "Networks"
            "Networks": {
                "pipeline_pg-network": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "pipeline-pgadmin-1",


docker inspect pg-database | grep -A 5 "Networks"
            "Networks": {
                "pg-network": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "MacAddress": "d6:e4:ca:40:fb:61",

## Usage

Run the container to ingest data into PostgreSQL:

```bash
docker run -it --rm \
  --network=pipeline_pg-network \
  taxi_zone_lookup:nyc_taxi_zone_lookup \
  --pg-user root \
  --pg-password root \
  --pg-host pipeline-pg-database-1 \
  --pg-port 5432 \
  --pg-db ny_taxi \
  --target-table zones \
  --chunksize 100000
```

## Options

- `--pg-user`: PostgreSQL username (default: `root`)
- `--pg-password`: PostgreSQL password (default: `root`)
- `--pg-host`: PostgreSQL host (default: `localhost`)
- `--pg-port`: PostgreSQL port (default: `5432`)
- `--pg-db`: PostgreSQL database name (default: `ny_taxi`)
- `--target-table`: Target table name (default: `zones`)
- `--chunksize`: Chunk size for bulk inserts (default: `100000`)

## Data Source

The data is ingested from `taxi_zone_lookup.csv` in this directory.
Build the docker image using the following : 
(pipeline) @deepaknrn ➜ /workspaces/docker-workshop/SQL-refresher (main) $ docker build -t taxi_zone_lookup:nyc_taxi_zone_lookup .

## Expected Output

[+] Building 12.0s (15/15) FINISHED                                   docker:default
 => [internal] load build definition from Dockerfile                            0.0s
 => => transferring dockerfile: 1.94kB                                          0.0s
 => [internal] load metadata for docker.io/library/python:3.13.11-slim          0.0s
 => [internal] load metadata for ghcr.io/astral-sh/uv:latest                    1.2s
 => [auth] astral-sh/uv:pull token for ghcr.io                                  0.0s
 => [internal] load .dockerignore                                               0.0s
 => => transferring context: 2B                                                 0.0s
 => FROM ghcr.io/astral-sh/uv:latest@sha256:9a23023be68b2ed09750ae636228e903a5  0.0s
 => [internal] load build context                                               0.0s
 => => transferring context: 56.95kB                                            0.0s
 => [stage-0 1/7] FROM docker.io/library/python:3.13.11-slim                    0.0s
 => CACHED [stage-0 2/7] COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/      0.0s
 => CACHED [stage-0 3/7] WORKDIR /code                                          0.0s
 => [stage-0 4/7] COPY pyproject.toml .python-version uv.lock ./                0.1s
 => [stage-0 5/7] RUN uv sync --locked                                          7.5s
 => [stage-0 6/7] WORKDIR /code                                                 0.0s
 => [stage-0 7/7] COPY ingest_taxi_zone_lookup.py .                             0.0s
 => exporting to image                                                          2.9s
 => => exporting layers                                                         2.9s
 => => writing image sha256:aa837760d710f74a0c1026d87d9a38e78a8922d4cc998922b1  0.0s
 => => naming to docker.io/library/taxi_zone_lookup:nyc_taxi_zone_lookup        0.0s