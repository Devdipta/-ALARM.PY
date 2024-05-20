import datetime
import time
import threading
import os

# If you're using Windows, you can use winsound to play a default sound
# For Linux or macOS, you can use os.system to play a sound using available system commands
try:
    import winsound
except ImportError:
    # If winsound is not available, we'll define a simple function to play a beep sound
    def beep_sound(frequency, duration):
        # Use a system command to play a beep sound
        os.system('play -nq -t alsa synth {} sine {}'.format(duration/1000, frequency))

    winsound.Beep = beep_sound

def play_alarm_sound():
    for _ in range(5):  # Number of beeps
        winsound.Beep(2500, 1000)  # Frequency in Hz, Duration in ms
        time.sleep(1)  # Wait between beeps

def set_alarm(alarm_time, message):
    print(f"Setting an alarm for {alarm_time}...")
    while True:
        current_time = datetime.datetime.now()
        if current_time >= alarm_time:
            print(f"ALARM! {message}")
            # Play the alarm sound in a separate thread so it's non-blocking
            threading.Thread(target=play_alarm_sound).start()
            break
        time.sleep(1)

def main():
    alarm_hour = int(input("Enter the hour for the alarm (24-hour format): "))
    alarm_minute = int(input("Enter the minute for the alarm: "))
    alarm_second = int(input("Enter the second for the alarm: "))
    reminder_message = input("Enter a gentle reminder message: ")

    # Set the alarm time
    now = datetime.datetime.now()
    alarm_time = now.replace(hour=alarm_hour, minute=alarm_minute, second=alarm_second)

    # Check if the alarm time is not in the past
    if alarm_time < now:
        print("The alarm time is in the past. Please enter a future time.")
        return

    set_alarm(alarm_time, reminder_message)

if __name__ == "__main__":
    main()