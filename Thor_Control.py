#!/usr/bin/env python3

from Adafruit_MotorHAT import Adafruit_MotorHAT, \
    Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import connexion
import logging
import copy
from motor import motor
from art import art

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
log = logging.getLogger("ThorControl")
log.setLevel(logging.INFO)

STEP_STYLE = Adafruit_MotorHAT.DOUBLE

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

def post_manualcontrol(articulation: int, reverse: int, numsteps: int):
    """
        Uses the swagger defined manualcontrol endpoint
        Allows for manual control of an articulation
    """
    art_dict = {1: art1, 2: art2, 3: art3, 4: art4, 5: art5, 6: art6}
    art_dict[int(articulation)].move_steps(reverse, numsteps)
    return "Moving art{0} reverse {1} by {2} steps\n".format(articulation, bool(reverse), numsteps)

def post_grippercontrol(direction: str):
    """
        Swagger defined gripper control endpoint
        commands are 'open' or 'close'
    """
    print("Trying to {0} the gripper".format(direction))

if __name__ == '__main__':
    """
        Load the connexion app to run the API
    """
    app = connexion.App(__name__, 8080, specification_dir='swagger/')
    app.add_api('thor_control.yaml', arguments={'title': 'Thor Arm Control'})
    log.info("Starting API Service on Port 8080")
    app.run()

