#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

# Needs to be BCM. GPIO.BOARD lets you address GPIO ports by periperal
# connector pin number, and the LED GPIO isn't on the connector
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(16, GPIO.OUT)

for _ in range(25):
    # On
    GPIO.output(16, GPIO.LOW)
    # Off
    GPIO.output(16, GPIO.HIGH)
    sleep(0.2)

