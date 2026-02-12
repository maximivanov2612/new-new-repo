import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

state = 0

period = 1.0

while True:
    GPIO.output(led, state)
    if (state == 0):
        print(0)
    else:
        print(1)
    state = not state 
    time.sleep(period)