#!/usr/bin/env python3

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

class motor(object):
    """
        A motor is defined by a hat and a position
        You can move the motor forward or backward
    """
    def __init__(self, hat, position):
        self._hat = hat
        self._position = position
        self._stepper = Adafruit_MotorHAT(addr = self._hat).getStepper(200, self._position)

    def step(self, reverse: int):
    """
        Steps the motor a single step in a direction
    """
        if reverse == 0:
            self._stepper.oneStep(Adafruit_MotorHAT.FORWARD, STEP_STYLE)
        elif reverse == 1:
            self._stepper.oneStep(Adafruit_MotorHAT.BACKWARD, STEP_STYLE)
