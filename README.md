# Activity_Reminder_Application

** What the Script Will Do:
  . Daily Reset: The script will reset the is_notification_sent array at the start of each new day to ensure notifications are sent again the next day.
  . Hourly Notifications: Throughout the specified hours (8 AM to 6 PM), it will check the current time every 5 minutes and send notifications based on the predefined schedule:
  . 1 PM: Reminder for lunch and water.
  . 4 PM: Reminder for snacks and water.
  . 6 PM: Reminder for Turn off your system and take break.
  . Every Hour from 8 AM to 6 PM (excluding 1 PM and 4 PM): Reminder to drink water.
  . This script will continue to run in the background, sending these reminders at the specified times, as long as it is not interrupted or stopped.


** The script is designed to run continuously and send notifications at specific times of the day.
  
** Overview of what the script does:

1) Imports and Initialization:
  . Imports the 'notification' module from 'plyer' for sending system notifications.
  . Imports 'datetime', 'timezone', and 'timedelta' from 'datetime' for handling date and time.
  . Imports 'sleep' from 'time' to pause the script for a specified interval.
  . Initializes an array 'is_notification_sent' with 24 zeros to track whether a notification has been sent for each hour of the day.

2) send_reminder Function:
  . Defined the 'send_reminder' function to send a notification with a given message.
  . Used 'notification.notify' to display the notification with a title, message, and a timeout of 20 seconds.

3) schedule Function:
  . Defined the 'schedule' function to check the current hour and send the appropriate notification if it hasn't been sent yet for that hour.
  . Checks if the current hour is 1 PM (13:00) and sends a "lunch and water" reminder if it hasn't been sent yet.
  . Checks if the current hour is 4 PM (16:00) and sends a "snacks and water" reminder if it hasn't been sent yet.
  . Checks if the current hour is 6 PM (18:00) and sends a "Turn off your system, it's time to take break" reminder if it hasn't been sent yet.
  . Loops through the hours from 8 AM (8:00) to 6 PM (18:00), excluding 1 PM and 4 PM, and sends a "drink water" reminder if it hasn't been sent yet for the current hour.
   
4) Main Loop:
  . Sets 'prev_date' to the previous day to track when a new day starts.
  . Enters an infinite loop (while True).
  . Updates 'date' to the current local time.
  . Resets 'is_notification_sent' array if a new day has started.
  . Calls the 'schedule' function to check and send notifications based on the current time.
  . Pauses the script for 5 minutes ('sleep(300)') before the next iteration.
