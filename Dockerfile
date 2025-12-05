# Dockerfile
# Stage 1: Builder
FROM python:3.11-slim-bookworm as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies into a virtual environment
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Copy dependency definition
COPY pyproject.toml .
# Install pip and dependencies (using pip to install from pyproject.toml via a trick or just installing hatchling)
# Simpler approach: Export requirements from pyproject.toml or just install libraries directly if we want to avoid complex build tools in docker
# For simplicity and robustness without extra tools, we will upgrade pip and install based on the file content manually or use pip install .
COPY . .
RUN pip install --upgrade pip && pip install .

# Stage 2: Runtime
FROM python:3.11-slim-bookworm as runtime

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Copy virtual env from builder
COPY --from=builder /app/venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Copy application code
COPY app /app/app
COPY frontend /app/frontend

# Set ownership
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

EXPOSE 8080

# Run application
CMD ["uvicorn", "app.api.gateway:app", "--host", "0.0.0.0", "--port", "8080"]
