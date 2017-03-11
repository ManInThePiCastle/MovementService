#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import threading
import random

TYPE = Adafruit_MotorHAT.DOUBLE
STEPS = 100
# recommended for auto-disabling motors on shutdown!
#def turnOffMotors():
#    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
#    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
#    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
#    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
#
#atexit.register(turnOffMotors)

def test_motor(hat, motor):
    print hat
    print motor
    global TYPE
    hat = int(hat, 16)
    mh = Adafruit_MotorHAT(addr = hat)
    motor_number = motor
    myStepper = mh.getStepper(200, motor_number)      # 200 steps/rev, motor port #1
    myStepper.setSpeed(120)          # 30 RPM

    myStepper.step(STEPS, Adafruit_MotorHAT.FORWARD, TYPE)
    myStepper.step(STEPS, Adafruit_MotorHAT.BACKWARD, TYPE)

if __name__ == '__main__':
    hat = raw_input("Input hat number\n")
    motor = raw_input("Input motor number\n")

    test_motor("0x6{0}".format(hat), int(motor))

