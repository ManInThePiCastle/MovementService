#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import threading
import random

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr = 0x63)

# create empty threads (these will hold the stepper 1 and 2 threads)
st1 = threading.Thread()
st2 = threading.Thread()


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper = mh.getStepper(200, 1)      # 200 steps/rev, motor port #1
myStepper.setSpeed(120)          # 30 RPM

stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE, Adafruit_MotorHAT.MICROSTEP]

myStepper.step(1000, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
#myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)


# while (True):
#         print("Single coil steps")
#         myStepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
#         myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
#         print("Double coil steps")
#         myStepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
#         myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
#         print("Interleaved coil steps")
#         myStepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.INTERLEAVE)
#         myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)
#         print("Microsteps")
#         myStepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
#         myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
