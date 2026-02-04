# Pipeline: Creating a Parquet File from a Pandas DataFrame

This guide explains how to use `pipeline.py` to create a Parquet file from a Pandas DataFrame. It also includes instructions for setting up the environment and building a Docker image.

---

## Pre-requisites

1. Install `uv`:
   ```bash
   pip install uv
   ```
2. Initialize `uv` with Python 3.13:
   ```bash
   uv init --python 3.13
   ```
3. Verify Python version:
   ```bash
   uv run python -V
   ```
4. Add required dependencies:
   ```bash
   uv add pandas
   uv add pyarrow
   ```

---

## Running the Program

To run the program in GitHub Codespaces:

```bash
uv run python pipeline.py 1
```

---

## Building the Docker Image

1. Build the Docker image using the provided `Dockerfile`:
   ```bash
   docker build -t test:pandas .
   ```
   - `test` is the image name.
   - `pandas` is the tag.
   - Together, `test:pandas` is the full Docker image name.

2. Example build output:

   ```bash
   @deepaknrn ➜ /workspaces/docker-workshop/pipeline_test (main) $ docker build -t test:pandas .
   [+] Building 17.3s (15/15) FINISHED                                                   docker:default
    => [internal] load build definition from Dockerfile                                            0.1s
    => => transferring dockerfile: 1.85kB                                                          0.0s
    => [internal] load metadata for ghcr.io/astral-sh/uv:latest                                    2.5s
    => [internal] load metadata for docker.io/library/python:3.13.11-slim                          0.0s
    => [auth] astral-sh/uv:pull token for ghcr.io                                                  0.0s
    => [internal] load .dockerignore                                                               0.0s
    => => transferring context: 2B                                                                 0.0s
    => FROM ghcr.io/astral-sh/uv:latest@sha256:db9370c2b0b837c74f454bea914343da9f29232035aa7632a1  3.2s
    => => resolve ghcr.io/astral-sh/uv:latest@sha256:db9370c2b0b837c74f454bea914343da9f29232035aa  0.0s
    => => sha256:db9370c2b0b837c74f454bea914343da9f29232035aa7632a1b14dc03add9edb 2.19kB / 2.19kB  0.0s
    => => sha256:efeddf2eadc8e30f9ce73a8a8668574585237becef05213fe804b15a7c52037c 669B / 669B      0.0s
    => => sha256:513654e7c766781cee579ed025883063b413a21fc39f43ef4e56cd1d9b7417c2 1.29kB / 1.29kB  0.0s
    => => sha256:775492f2e5535751e69b07d132a06f8efea5ccb86d66df3f6ac63dd91a4321 22.75MB / 22.75MB  1.9s
    => => sha256:9fae40f2f407cb3fee2e987c7f4d8611d4a083f2f6fb60f290c28c65665abfc4 98B / 98B        0.5s
    => => extracting sha256:775492f2e5535751e69b07d132a06f8efea5ccb86d66df3f6ac63dd91a432197       0.3s
    => => extracting sha256:9fae40f2f407cb3fee2e987c7f4d8611d4a083f2f6fb60f290c28c65665abfc4       0.0s
    => [internal] load build context                                                               0.0s
    => => transferring context: 36.95kB                                                            0.0s
    => CACHED [stage-0 1/7] FROM docker.io/library/python:3.13.11-slim                             0.0s
    => [stage-0 2/7] COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/                             0.9s
    => [stage-0 3/7] WORKDIR /code                                                                 0.0s
    => [stage-0 4/7] COPY pyproject.toml .python-version uv.lock ./                                0.0s
    => [stage-0 5/7] RUN uv sync --locked                                                          7.4s
    => [stage-0 6/7] WORKDIR /code                                                                 0.1s
    => [stage-0 7/7] COPY pipeline.py  .                                                           0.0s
    => exporting to image                                                                          2.9s
    => => exporting layers                                                                         2.9s
    => => writing image sha256:9e271b04ef0a75ad60f46ec6b475f811269b9c0130e08466a846263cabe82f05    0.0s
    => => naming to docker.io/library/test:pandas                                                  0.0s
   ```

---

## Running the Docker Image

1. Run the Docker image interactively:
   ```bash
   docker run -it --entrypoint=bash --rm test:pandas
   ```
2. Inside the container, you can list the files to verify the contents:
   ```bash
   root@e463826dd274:/code# ls
   pipeline.py  pyproject.toml  uv.lock
   ```
3. Execute the script with the desired argument:
   ```bash
   root@e463826dd274:/code# python pipeline.py 2
   ```
   - Example output:
     ```
     Arguments passed to the script:['pipeline.py', '2']
     Month argument value: 2
        day  num_passengers  month
     0    1               3      2
     1    2               4      2
     ```
4. Alternatively, you can run the Docker image with the argument directly:
   ```bash
   docker run -it --rm test:pandas 2
   ```
   - This will execute the script with the argument `2` immediately.