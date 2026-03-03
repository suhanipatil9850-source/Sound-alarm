import time
from datetime import datetime

# Get alarm time from user
alarm_time = input("Enter alarm time (HH:MM, 24-hour format): ")

print("Alarm set for", alarm_time)

while True:
    now = datetime.now().strftime("%H:%M")

    if now == alarm_time:
        print("⏰ Wake up! Alarm ringing!")
        break

    time.sleep(30)  # Check every 30 seconds