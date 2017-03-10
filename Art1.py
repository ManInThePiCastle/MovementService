#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import threading
import sys

# Using the top hat address for Art1
mh = Adafruit_MotorHAT(addr = 0x63)

# Set the global step style used.  
STEP_STYLE = Adafruit_MotorHAT.DOUBLE

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

Stepper1 = mh.getStepper(200, 1)      # 200 steps/rev, motor port #1
Stepper2 = mh.getStepper(200, 2)      # 200 steps/rev, motor port #1

stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE, Adafruit_MotorHAT.MICROSTEP]

def move_effector(steps, command, direction):
    """
        Moves the end effector.
        command: either tilt or spin
        direction: if tilt, up or down
                   if spin, clockwise or counterclockwise
        Returns 1 if you don't send a valid commande
    """
    global STEP_STYLE
    if command == 'tilt':
        if direction == 'up':
            for i in range(steps):
                Stepper1.oneStep(Adafruit_MotorHAT.FORWARD, STEP_STYLE)
                Stepper2.oneStep(Adafruit_MotorHAT.FORWARD, STEP_STYLE)
            return 0
        elif direction == 'down':
            for i in range(steps):
                Stepper1.oneStep(Adafruit_MotorHAT.BACKWARD, STEP_STYLE)
                Stepper2.oneStep(Adafruit_MotorHAT.BACKWARD, STEP_STYLE)
            return 0
        else:
            return 1
    elif command == 'spin':
        if direction == 'clockwise':
            for i in range(steps):
                Stepper1.oneStep(Adafruit_MotorHAT.BACKWARD, STEP_STYLE)
                Stepper2.oneStep(Adafruit_MotorHAT.FORWARD, STEP_STYLE)
            return 0
        elif direction == 'counterclockwise':
            for i in range(steps):
                Stepper1.oneStep(Adafruit_MotorHAT.FORWARD, STEP_STYLE)
                Stepper2.oneStep(Adafruit_MotorHAT.BACKWARD, STEP_STYLE)
            return 0
        else:
            return 1
    else:
        return 1

if __name__ == '__main__':
    """ Testing code.  Allows manual control """
    try: 
        num_steps = raw_input("Number of testing steps: ")
        num_steps = int(num_steps)
    except ValueError:
        print("That is not a valid number!!!")
        sys.exit(1)

    while True:
        command = raw_input("Command (q to quit):")
        if command.lower() == 'q':
            turnOffMotors()
            break
        elif command == 'up' or command == 'down':
            move_effector(num_steps, 'tilt', command) 
        elif command == 'clockwise' or command == 'counterclockwise':
            move_effector(num_steps, 'spin', command)
        elif command == '1 cw':
            for i in range(num_steps):
                Stepper1.oneStep(Adafruit_MotorHAT.FORWARD, STEP_STYLE)
        elif command == '1 ccw':
            for i in range(num_steps):
                Stepper1.oneStep(Adafruit_MotorHAT.BACKWARD, STEP_STYLE)
        elif command == '2 cw':
            for i in range(num_steps):
                Stepper2.oneStep(Adafruit_MotorHAT.FORWARD, STEP_STYLE)
        elif command == '2 ccw':
            for i in range(num_steps):
                Stepper2.oneStep(Adafruit_MotorHAT.BACKWARD, STEP_STYLE)

        else:
            print("I don't know that command.  Options are up, down, clockwise, counterclockwise")

