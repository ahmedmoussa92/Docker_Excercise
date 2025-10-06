# Dockerfile
FROM python:3.9-slim
WORKDIR /app

ARG TEST_FILE
COPY ${TEST_FILE} /app/test.py

# Disable pip progress bar and avoid rich output to save resources
ENV PIP_NO_PROGRESS_BAR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN pip install --no-cache-dir --progress-bar off requests

CMD ["python", "test.py"]
