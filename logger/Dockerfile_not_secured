FROM python:3.10-slim

WORKDIR /app

COPY app.py .

# Create logs directory inside container
RUN mkdir /logs

CMD ["python", "app.py"]

