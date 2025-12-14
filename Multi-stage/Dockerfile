# Stage 1: Build
FROM ubuntu:22.04 AS builder

# Install Python and build tools
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip3 install --user -r requirements.txt

# Copy the app code
COPY . .

# Stage 2: Runtime
FROM ubuntu:22.04

# Install only Python runtime (lighter than build stage)
RUN apt-get update && apt-get install -y python3 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy installed dependencies and app code from builder
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

# Set PATH for pip packages
ENV PATH=/root/.local/bin:$PATH

# Expose port
EXPOSE 5000

# Run the app
CMD ["python3", "app.py"]
