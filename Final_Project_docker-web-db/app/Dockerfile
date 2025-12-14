# -------- Stage 1: Builder --------
FROM python:3.10.16-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# -------- Stage 2: Runtime --------
FROM python:3.10.16-slim

WORKDIR /app

RUN useradd -m appuser

# Copy system-wide Python packages and app
COPY --from=builder /usr/local /usr/local
COPY --from=builder /app/app.py ./app.py

USER appuser

EXPOSE 5000
CMD ["python", "app.py"]

