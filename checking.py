import RPi.GPIO as GPIO
import os
import sys
import time
import subprocess
from guizero import App, Picture, Text
in1 = 12
in2 = 11
IR_sensor =  8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.setup(IR_sensor, GPIO.IN)

GPIO.output(in1, False)
GPIO.output(in2, False)


def fillings():
    subprocess.Popen("python guiwork.py", shell=True)



try:
    while True:
        for x in range(3):
            GPIO.output(in1, True)
            time.sleep(2)
            GPIO.output(in1, False)
            print(x)
            if x ==1:
                val = "Bottle Status : Detected"
                fillings()
                GPIO.output(in2, True)
                time.sleep(1.5)
                GPIO.output(in2, False)

except KeyboardInterrupt:
    GPIO.cleanup()