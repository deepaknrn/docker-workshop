#Dockerfile for pipeline.py

FROM python:3.13.11-slim
#The first line is FROM instruction which specifies the base image for the docker container
#The base image is the official python slim image
#The docker container test with the label of pandas will be created from this base image
#docker build -t test:pandas .
#Take the Dockerfile from the current directory and build the docker image with the tag test:pandas


ENV PATH="/code/.venv/bin:$PATH"
#Set the PATH variable to include the virtual environment created by uv

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
#Copy the uv binary from the uv docker image to the /bin/ directory of this docker container

#set the working directory in the docker container
WORKDIR /code
COPY pyproject.toml .python-version uv.lock ./  
#Copy the UV related dependency files
#Here uv.lock is the lock file created by uv to lock the dependencies, created manually and not when calling uv init --python 3.13

#RUN pip install pandas pyarrow 
#Install the dependencies required for executing pipeline.py file

RUN uv sync --locked 
#Install the dependencies from uv.lock file 
#Thus ensuring that the same versions of the dependencies are installed every time the docker container is built

WORKDIR /code
COPY pipeline.py  .

ENTRYPOINT ["python", "pipeline.py"]
#ENTRYPOINT ["uv","run","python", "pipeline.py"]
#Set the entrypoint to execute the pipeline.py file when the container starts

#If you don't like writing uv run in the ENTRYPOINT CREATe the following entry at the top of this script
#ENV PATH="/code/.venv/bin:$PATH"
#This will add the virtual environment created by uv to the PATH variable
