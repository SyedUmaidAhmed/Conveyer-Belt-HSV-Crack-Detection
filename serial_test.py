import RPi.GPIO as GPIO
import time
import subprocess
import sys
GPIO.setmode(GPIO.BOARD)
read_pin = 8
GPIO.setup(read_pin, GPIO.IN)

while True:
    got_signal = GPIO.input(read_pin)
    if got_signal ==0:
        print("Nothing found")
        time.sleep(1)

    else:
        print("There is a Signal")
        time.sleep(1)
        subprocess.Popen("python guiwork.py", shell=True)


