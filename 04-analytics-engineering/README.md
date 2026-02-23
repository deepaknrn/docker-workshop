# Analytics Engineering Workshop

This repository is based on the **Data Engineering Zoomcamp 2026 - Analytics Engineering Workshop**.  
You can find the YouTube playlist [here](https://www.youtube.com/watch?v=J0XCDyKiU64&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=32).  
Learn more about dbt [here](https://www.getdbt.com/lp/persona-paths?utm_medium=paid-search&utm_source=google&utm_campaign=q1-2025_apac-nonbrand-datatransformation_co&utm_content=_kw-datatransformationtools-ph___&utm_term=all_apac_anz&cq_cmp=21195055622&utm_term=data%20transformation&utm_campaign=&utm_source=adwords&utm_medium=ppc&hsa_acc=8253637521&hsa_cam=21195055622&hsa_grp=164743458161&hsa_ad=783662596456&hsa_src=g&hsa_tgt=kwd-18219416&hsa_kw=data%20transformation&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=21195055622&gbraid=0AAAAABONxYjvxm0rcX3RlX-eBKuTvHBeR&gclid=CjwKCAiAkvDMBhBMEiwAnUA9BfYl5ZmRg3dm1BSn8wkftm3XOrpFFxBwXtvclKbit93jxEYBlddWPRoC-FUQAvD_BwE).

Dbt local setup here : https://www.youtube.com/watch?v=GoFAbJYfvlw
--- Codespaces 

## Pre-requisites: Python

### 1. Create the Project Folder
Create a folder `/04-analytics-engineering` under the Codespace `/docker-workshop`.

### 2. Initialize the Project
Run the following command to initialize the project using `uv`:
```bash
uv init --python 3.13
```

### 3. Create the Virtual Environment
Check the Python version to confirm the virtual environment is created:
```bash
uv run python -V
```

### 4. Activate the Virtual Environment
Activate the virtual environment:
```bash
source .venv/bin/activate
```

### 5. Add Required Packages
Install the required packages using `uv`:
```bash
uv add duckdb
uv add dbt-duckdb
uv add dbt-bigquery
```

### 6. View Installed Packages
List the installed packages:
```bash
uv pip list
```
Example output:
| Package           | Version   |
|-------------------|-----------|
dbt-adapters              1.22.6
dbt-common                1.37.2
dbt-core                  1.11.6
dbt-duckdb                1.10.1
dbt-extractor             0.6.0
dbt-protos                1.0.431
dbt-semantic-interfaces   0.9.0
deepdiff                  8.6.1
duckdb                    1.4.4

Verify the version 

(04-analytics-engineering) @deepaknrn ➜ /workspaces/docker-workshop/04-analytics-engineering (main) $ dbt --version
Core:
  - installed: 1.11.6
  - latest:    1.11.6 - Up to date!

Plugins:
  - duckdb: 1.10.1 - Up to date!


Ensure dbt-bigquery plugin is installed.

Create the dbt project

(.venv) @deepaknrn ➜ /workspaces/docker-workshop/04-analytics-engineering (main) $ dbt init taxi_rides_ny

To configure dbt to use DuckDB, you need to set up your dbt profile in the file ~/.dbt/profiles.yml. Here’s a minimal example for a DuckDB profile:

taxi_rides_ny:
  target: dev
  outputs:
    # DuckDB Development profile
    dev:
      type: duckdb
      path: taxi_rides_ny.duckdb
      schema: dev
      threads: 1
      extensions:
        - parquet
      settings:
        memory_limit: '2GB'
        preserve_insertion_order: false

    # DuckDB Production profile
    prod:
      type: duckdb
      path: taxi_rides_ny.duckdb
      schema: prod
      threads: 1
      extensions:
        - parquet
      settings:
        memory_limit: '2GB'
        preserve_insertion_order: false

# Troubleshooting:
# - If you have less than 4GB RAM, try setting memory_limit to '1GB'
# - If you have 16GB+ RAM, you can increase to '4GB' for faster builds
# - Expected build time: 5-10 minutes on most systems