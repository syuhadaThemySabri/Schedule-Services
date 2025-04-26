import schedule
import time
from datetime import datetime, timedelta
import threading
import logging

# Configure logging to track service activity
logging.basicConfig(
    filename='D:\\College\\Semester 6 (Magang)\\Iseng\\SERVICE SCHEDULER\\service.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def write_time_to_file():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("D:\\College\\Semester 6 (Magang)\\Iseng\\SERVICE SCHEDULER\\current_time.txt", "a") as file:
        file.write(f"Current time: {formatted_time}\n")
    logging.info(f"Written: {formatted_time}")
    print(f"Written: {formatted_time}")

def schedule_task():
    # Schedule the task every 5 minutes
    schedule.every(1).minutes.do(write_time_to_file)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    logging.info("Service started")
    # Run the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=schedule_task, daemon=True)
    scheduler_thread.start()
    try:
        # Keep the main thread alive
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        logging.info("Service stopped")