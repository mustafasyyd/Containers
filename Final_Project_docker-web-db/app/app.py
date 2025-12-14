from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Web App is running!"

@app.route("/db")
def db():
    try:
        conn = psycopg2.connect(
            host=os.environ["DB_HOST"],
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASS"]
        )
        return "Connected to database!"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

