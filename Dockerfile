# Python image from the docker repo
FROM python:3.11-slim

# Establishes working directory within the container
WORKDIR /app

# Copies local code into the container's working directory "." for execution
COPY auditor.py .

CMD ["python","auditor.py"]

