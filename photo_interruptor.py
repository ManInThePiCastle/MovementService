#!/usr/bin/env python

import RPi.GPIO as GPIO

PIN = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def get_open_closed(_pin):
    """
        Gets the open or closed value of a photo interrupter pin
        0 is blocked
        1 is open
    """
    if GPIO.input(_pin) == 1:
        return 'open'
    if GPIO.input(_pin) == 0:
        return 'closed'
    else:
        return 'error'


while True:
    print(get_open_closed(PIN))
