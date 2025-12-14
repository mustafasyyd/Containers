# ALways use the latest patch version
FROM python:3.10.16-slim

WORKDIR /app

COPY requirements.txt .

#RUN apt-get update && apt-get upgrade 
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m appuser
USER appuser

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]

