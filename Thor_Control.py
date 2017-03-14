#!/usr/bin/env python3

from Adafruit_MotorHAT import Adafruit_MotorHAT, \
    Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import connexion
import logging
import copy
import sys
from motor import motor
from art import art

log = logging.getLogger('Thor_Main')
hdlr = logging.FileHandler('/var/log/thor_control.log')
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
log.addHandler(hdlr)
log.setLevel(logging.DEBUG)

# Define motors 1-7 from the bottom of the bot to the top.
# The definition is a motor hat, and a hat position
m1 = motor(0x61, 2)
m2 = motor(0x63, 2)
m3 = motor(0x61, 1)
m4 = motor(0x63, 1)
m5 = motor(0x60, 2)
m6 = motor(0x62, 1)
m7 = motor(0x60, 1)

# Define the articulations.  These are a list of lists
# that inculde a motor and a default reverse spec
# Also include a number of degrees per step as a float
art1 = art([[m1, 0]], 1.8)
art2 = art([[m2, 0], [m3, 0]], 0.35)
art3 = art([[m4, 0]], 1.0)
art4 = art([[m5, 0]], 1.0)
art5 = art([[m6, 0], [m7, 0]], 1.0)
art6 = art([[m6, 0], [m7, 1]], 1.0)

# Fake for testing
art7 = art([[m6, 0]], 1.0)
art8 = art([[m7, 0]], 1.0)

art_dict = {1: art1, 2: art2, 3: art3, 4: art4, 5: art5, 6: art6, 7: art7, 8: art8}

def post_motorsteps(hat: int, position: int, reverse: int, numsteps: int):
    """
        Allows a single motor to be controlled by address
    """
    log.debug("post_motorsteps - Starting. hat={0} position={1} reverse={2} numsteps={3}".format(hat, position, reverse, numsteps))
    try:
        hat = int('0x6{0}'.format(hat), 16)
    except Exception as e:
        log.error("{0}".format(str(e)))
    test_motor = motor(hat, position)
    for step in range(numsteps):
        log.debug("Stepping hat {0} position {1} reverse {2}".format(hat, position, bool(int(reverse))))
        test_motor.step(bool(int(reverse)))


def post_artsteps(articulation: int, reverse: int, numsteps: int):
    """
        Uses the swagger defined manualcontrol endpoint
        Allows for manual control of an articulation
    """
    log.debug("post_artsteps - starting")
    art_dict[int(articulation)].move_steps(reverse, numsteps)
    log.info("POST ManualControl Art {0} Steps {1} Reverse {2}".format(articulation, numsteps, reverse))
    return "Moving art{0} reverse {1} by {2} steps\n".format(articulation, reverse, numsteps)


def post_artdegrees(articulation: int, reverse: int, degrees: float):
    """
        Uses the degrees endpoint
        Allows movement of a single articulation by degrees
    """
    log.debug("post_artdegrees - starting")
    art_dict[int(articulation)].move_degrees(reverse, degrees)
    log.info("POST ManualControl Art {0} Degrees {1} Reverse {2}".format(articulation, degrees, reverse))
    return "Moving art{0} reverse {1} by {2} degrees\n".format(articulation, bool(reverse), degrees)

def post_gripper(command):
    """
        Swagger defined gripper control endpoint
        commands are 'open' or 'close'
    """
    log.info("Trying to {0} the gripper".format(command))
    return "Trying to {0} the gripper".format(command)

if __name__ == '__main__':
    """
        Load the connexion app to run the API
    """
    app = connexion.App(__name__, 8080, specification_dir='swagger/')
    app.add_api('thor_control.yaml', arguments={'title': 'Thor Arm Control'})
    log.info("Starting API Service on Port 8080")
    app.run()

