#!/usr/bin/env python3

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import connexion
import logging

class motor(object):
    """
        A motor is defined by a hat and a position
        You can move the motor forward or backward
    """
    def __init__(self, hat, position):
        self._hat = hat
        self._position = position
        self._stepper = Adafruit_MotorHAT(addr = self._hat).getStepper(200, self._position)

    @classmethod
    def step(self, reverse: int):
        if reverse == 0:
            self._stepper.oneStep(Adafruit_MotorHAT.FORWARD, STEP_STYLE)
        elif reverse == 1:
            self._stepper.oneStep(Adafruit_MotorHAT.BACKWARD, STEP_STYLE)

class art(object):
    """
        An articulation is one or more motors with a default direction
        EX: art([[motor1,0],[motor2,1]])
    """
    def __init__(self, motors):
        self._motors = motors
    
    @classmethod
    def move_steps(self, reverse: int, steps):
        for step in range(steps):
            for motor, def_direction in self._motors:
                motor.step(bool(reverse) ^ bool(def_direction))

m1 = motor(0x62, 2)
m2 = motor(0x63, 2)
m3 = motor(0x61, 1)
m4 = motor(0x63, 1)
m5 = motor(0x60, 2)
m6 = motor(0x62, 1)
m7 = motor(0x60, 1)

art1 = art([[m1, 0]])
art2 = art([[m2, 0], [m3, 0]])
art3 = art([[m4, 0]])
art4 = art([[m5, 0]])
art5 = art([[m6, 0], [m7, 0]])
art6 = art([[m6, 0], [m7, 1]])

# recommended for auto-disabling motors on shutdown!
#def turnOffMotors():
#    for hat in [0x60, 0x61, 0x62, 0x63]:
#        for motor in [1,2,3,4]:
#            Adafruit_MotorHAT(addr = hat).getMotor(motor).run(Adafruit_MotorHAT.RELEASE)
#
#atexit.register(turnOffMotors)

def post_manualcontrol(articulation: int, reverse: int, numsteps: int) -> str:
    art_dict = {1: art1, 2: art2, 3: art3, 4: art4, 5: art5, 6: art6}
    art_dict[articulation].move_steps(reverse, numsteps)
    return "Moving {0} {1} by {2} steps\n".format(articulation, direction, numsteps)

if __name__ == '__main__':
    art_dict = {1: art1, 2: art2, 3: art3, 4: art4, 5: art5, 6: art6}
    test.move_steps(0,1)
    #art_dict[1].move_steps(0, 1)              
    #app = connexion.App(__name__, 8080, specification_dir='swagger/')
    #app.add_api('thor_control.yaml', arguments={'title': 'Thor Arm Control'})
    app.run()

