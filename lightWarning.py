import threading
import RPi.GPIO as GPIO
from time import sleep

class WarningThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        # GPIO.output(25, GPIO.LOW)
        # sleep(0.1)
        # GPIO.output(25, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
        sleep(5)
        GPIO.output(24, GPIO.HIGH)