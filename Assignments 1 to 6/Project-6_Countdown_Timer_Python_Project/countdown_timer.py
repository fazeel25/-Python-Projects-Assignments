# Countdown Timer Project


import time

def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("\n⏳ Timer completed!")

try:
    t = int(input("⏱ Enter the time in seconds: "))
    if t < 0:
        print("❌ Please enter a positive number!")
    else:
        countdown(t)
except ValueError:
    print("❌ Invalid input! Please enter a valid number.")