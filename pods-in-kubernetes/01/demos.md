### Step 1: Create a Simple Application

#### File: `app.py`
###########
import logging
from flask import Flask

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO
logger = logging.getLogger()

@app.route('/')
def hello():
    logger.info("Processing request for '/' endpoint")
    return "Hello, Kubernetes!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
###########
#### File: `requirements.txt`
flask

#### File: `Dockerfile`
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]

# Build the Docker image
docker build -t dbclinton/simple-app:latest .

# Push the image to Docker Hub
docker push dbclinton/simple-app:latest

### Step 4: Create a Kubernetes Pod Manifest
Write a Kubernetes manifest file to deploy the application.

#### File: `pod.yaml`
apiVersion: v1
kind: Pod
metadata:
  name: simple-app
  labels:
    app: simple-app
spec:
  containers:
  - name: simple-app
    image: dbclinton/simple-app:latest
    ports:
    - containerPort: 5000

# Install kubectl
sudo snap install kubectl --classic
kubectl version --client

## Install kind:
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.26.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind


