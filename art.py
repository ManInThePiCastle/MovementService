#!/usr/bin/env python3

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import motor

class art(object):
    """
        An articulation is one or more motors with a default direction
        EX: art([[motor1,0],[motor2,1]])
    """
    def __init__(self, motors, degrees_per_step):
        self._motors = motors
        self._deg_per_step = degrees_per_step
        for motor, def_direction in self._motors:
            motor.step(True)

    def addmotor(self, motor_number, reverse):
        self._motors.append([motor_number, reverse])
        print(self._motors)

    def move_steps(self, reverse, steps):
        for step in range(steps):
            for motor, def_direction in self._motors:
                motor.step(bool(int(reverse)) ^ bool(int(def_direction)))
    
    def move_degrees(self, degrees):
        try:
            float(degrees)
        except ValueError:
            print("You must move a number of degrees")
            break
        num_steps = degrees * self.deg_per_step
        if degrees < 0:
            direction = 1
        elif degrees > 0:
            direction = 0
        else:
            print("Something went wrong with number of degrees")
            break
        
        move_steps(direction, num_steps)            

        
