FROM python:3.10-slim-bookworm

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Set the working directory
WORKDIR /app

# Copy the relevant files into the image
COPY conf conf
COPY src src
COPY pyproject.toml pyproject.toml
COPY app_fastapi/main.py main.py

# Sync the project into a new environment
RUN uv sync --no-dev --extra api

# Run the project
CMD [".venv/bin/uvicorn", "app_fastapi.main:app", "--port", "80", "--host", "0.0.0.0"]