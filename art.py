#!/usr/bin/env python3

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import motor
import logging

log = logging.getLogger('Thor_Art')
hdlr = logging.FileHandler('thor.log')
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
log.addHandler(hdlr)
log.setLevel(logging.DEBUG)

class art(object):
    """
        An articulation is one or more motors with a default direction
        EX: art([[motor1,0],[motor2,1]])
    """
    def __init__(self, motors, degrees_per_step):
        log.info("Initializing articulation")
        self._motors = motors
        self._deg_per_step = degrees_per_step
        for motor, def_direction in self._motors:
            motor.step(True)

    def addmotor(self, motor_number, reverse):
        self._motors.append([motor_number, reverse])
        print(self._motors)

    def move_steps(self, reverse, steps):
        log.info("move_steps - Starting")
        for step in range(steps):
            for motor, def_direction in self._motors:
                current_direction = bool(int(reverse)) ^ bool(int(def_direction))
                log.debug("Stepping motor {0} direction {1}".format(motor, current_direction))
                motor.step(current_direction)

    def move_degrees(self, degrees):
        log.info("move_degrees - Start")
        try:
            float(degrees)
        except ValueError:
            log.error("move_degrees - ValueError")
            return None
        num_steps = (degrees * self._deg_per_step)
        if degrees < 0:
            direction = 1
        elif degrees > 0:
            direction = 0
        else:
            log.error("move_degrees - Number of degrees is 0")
            return None
        log.info("move_degrees - Moving {0} steps. Reverse: {1}".format(int(num_steps), direction))
        log.debug("move_degrees - type(direction)={0} type(num_steps)={1}".format(type(direction), type(num_steps)))
        move_steps(direction, int(num_steps))

