import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

qwe = 6

GPIO.setup(qwe, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(6))