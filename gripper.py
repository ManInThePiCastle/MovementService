#!/usr/bin/env python

import time
import wiringpi
import curses


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
max_pulse = 185
min_pulse = 85


def input_char(message):
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


def open_close_gripper(command):
    if command == 'close':
        wiringpi.pwmWrite(18, max_pulse)
    if command == 'open':
        wiringpi.pwmWrite(18, min_pulse)
    time.sleep(delay_period)

def change_pulse(current_pulse, direction):
    print("Trying to move pulse {0} {1} by  {2}".format(str(current_pulse), str(direction), str(pulse_delta))) 
    if direction == 'up':
        if current_pulse > max_pulse - pulse_delta:
            print('Cannot increment further')
            return current_pulse
        else:
            return current_pulse + pulse_delta
    if direction == 'down':
        if current_pulse < min_pulse + pulse_delta:
            print('Cannot decrement further')
            return current_pulse
        else:
            return current_pulse - pulse_delta
            

while True:
    keystroke = raw_input("Command (q to quit):")
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
   #
   # for pulse in range(50,250,1):
   #     print(pulse)
   #     wiringpi.pwmWrite(18, pulse)
   #     time.sleep(delay_period)
   # for pulse in range(250,50,-1):
   #     print(pulse)
   #     wiringpi.pwmWrite(18, pulse)
   #     time.sleep(delay_period)

