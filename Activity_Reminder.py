from plyer import notification
from datetime import datetime, timezone, timedelta
from time import sleep

# Array to track notification sent status for each hour
is_notification_sent = [0] * 24

def send_reminder(msg):
    notification.notify(title = 'Urgent Reminder',
                        message = msg,
                        timeout = 20)

def schedule(date):
    hour = date.hour

    # Remind for lunch and water at 1 PM
    if hour == 13 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("It's time for lunch and water!!")

    # Remind for snacks at 4 PM
    if hour == 16 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("It's time for snacks and water!!")

    # Remind to turn off your system and take break.
    if hour == 18 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("Turn off your system, it's time to take break")

    # Remind for drinking water during my studing time
    for i in range(8, 18):
        if hour == i and hour not in [13, 16] and is_notification_sent[hour] == 0:
            is_notification_sent[hour] = 1
            send_reminder("It's time to drink water!!")

if __name__ == "__main__":
    prev_date = datetime.now(timezone.utc).astimezone() - timedelta(days=1)
    while True:
        date = datetime.now(timezone.utc).astimezone()
        if date.day != prev_date.day:
            is_notification_sent = [0] * 24
            prev_date = date
        schedule(date)
        sleep(300)  # Sleep for 5 minutes
