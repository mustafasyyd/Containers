import time
from datetime import datetime

while True:
    with open("/logs/app.log", "a") as f:
        f.write(f"{datetime.now()} - Application is running\n")
    time.sleep(5)

