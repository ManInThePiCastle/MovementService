#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import threading
import random

# create a default object, no changes to I2C address or frequency
hat0 = Adafruit_MotorHAT(addr = 0x60)
hat1 = Adafruit_MotorHAT(addr = 0x61)
hat2 = Adafruit_MotorHAT(addr = 0x62)
hat3 = Adafruit_MotorHAT(addr = 0x63)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

def art_motor_translation(art):
    """ Takes an articulation number
        Returns a 
    """
    if art == '1':
        return 


def move_articulation(articulation: int, direction: int, steps: int, step_type: str):
    
    myStepper = mh.getStepper(200, motor_num)      # 200 steps/rev, motor port #1
    myStepper.setSpeed(120)          # 30 RPM



    stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE, Adafruit_MotorHAT.MICROSTEP]

    myStepper.step(50, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.INTERLEAVE)
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
