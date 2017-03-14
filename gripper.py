#!/usr/bin/env python3

"""
Gripper
Code for testing, calibrating, and open/closing the gripper
"""

import time
import wiringpi
import curses


# Setup the Gpio and the pin.
wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01
pulse_delta = 5

# Set initial position
pulse = 150
wiringpi.pwmWrite(18, pulse)

# Minimum pulse is 85 (Gripper Open)
# Maximum pulse is 185 (Gripper Closed)
MAX_PULSE = 175
MIN_PULSE = 80


def input_char(message):
    """
       Takes an input of a char from the input stream.
       Allows for manual testing
    """
    try:
        win = curses.initscr()
        win.addstr(0, 0, message)
        while True:
            ch = win.getch()
            if ch in range(32, 127): break
            time.sleep(0.05)
    except: raise
    finally:
        curses.endwin()
    return chr(ch)


def change_pulse(current_pulse, direction):
    """
        Changes the puluse up or down
        Basically moves the servo in a direction
    """
    print("Trying to move pulse {0} {1} by  {2}".format(str(current_pulse), str(direction), str(pulse_delta)))
    if direction == 'up':
        if current_pulse > MAX_PULSE - pulse_delta:
            print('Cannot increment further')
            return current_pulse
        else:
            return current_pulse + pulse_delta
    if direction == 'down':
        if current_pulse < MIN_PULSE + pulse_delta:
            print('Cannot decrement further')
            return current_pulse
        else:
            return current_pulse - pulse_delta


def open_close_gripper(command):
    """
        Opens or closes the gripper
    """
    if command == 'close':
        wiringpi.pwmWrite(18, MAX_PULSE)
    if command == 'open':
        wiringpi.pwmWrite(18, MIN_PULSE)
    time.sleep(delay_period)


if __name__ == '__main__':
    while True:
        keystroke = input("Command (q to quit):")
        if keystroke.lower() == 'q':
            break
        elif keystroke == 'up':
            pulse = change_pulse(pulse, 'up')
            wiringpi.pwmWrite(18, pulse)
            time.sleep(delay_period)
        elif keystroke == 'down':
            pulse = change_pulse(pulse, 'down')
            wiringpi.pwmWrite(18, pulse)
            time.sleep(delay_period)
        else:
            open_close_gripper(keystroke)

        print(str(pulse) + '\n')

