#!/usr/bin/env python3

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import motor

class art(object):
    """
        An articulation is one or more motors with a default direction
        EX: art([[motor1,0],[motor2,1]])
    """
    def __init__(self, motors):
        self._motors = motors

    def addmotor(self, motor_number, reverse):
        self._motors.append([motor_number, reverse])
        print(self._motors)

    def move_steps(self, reverse, steps):
        for step in range(steps):
            for motor, def_direction in self._motors:
                motor.step(bool(int(reverse)) ^ bool(int(def_direction)))
