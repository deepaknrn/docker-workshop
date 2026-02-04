# Docker Volume Example: Folder `test`

This folder demonstrates the use of **Volumes** with Docker containers. The `test` folder is mapped as a volume to a Docker container created from the image `python:3.13.11-slim`. This example also shows how to execute a Python program within a Docker container, with a folder from the local machine (e.g., GitHub Codespaces) mapped as a volume to the container.

---

## Steps to Reproduce

### Step 1: Map the `test` Folder as a Volume
Map the `test` folder to `/app/test` within the Docker container:

```bash
docker run -it --entrypoint=bash -v $(pwd)/test:/app/test python:3.13.11-slim
```

### Step 2: Navigate to the Mapped Folder
Once inside the container, navigate to the mapped folder:

```bash
root@<container_id>:/# ls
app  boot  etc   lib    media  opt   root  sbin  sys  usr
bin  dev   home  lib64  mnt    proc  run   srv   tmp  var

root@<container_id>:/# cd app
root@<container_id>:/app# ls
test

root@<container_id>:/app# cd test
root@<container_id>:/app/test# ls
file1  file2  file3  script.py
```

### Step 3: Execute the Python Program
Run the Python script to list the files in the `/app/test` directory:

```bash
root@<container_id>:/app/test# python3 script.py
```

#### Output:
```
Files in /app/test:
  - file1
    Content: Hello
  - file3
    Content: I am fine
  - file2
    Content: How are you
```

---

This example highlights how Docker volumes can be used to share data between the host machine and a container.
