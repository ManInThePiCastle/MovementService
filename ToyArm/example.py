#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
Motor_1 = mh.getMotor(1)
Motor_2 = mh.getMotor(2)
Motor_3 = mh.getMotor(3)
Motor_4 = mh.getMotor(4)

# set the speed to start, from 0 (off) to 255 (max speed)
Motor_1.setSpeed(50)
Motor_2.setSpeed(50)
Motor_3.setSpeed(50)
Motor_4.setSpeed(50)

print("Motor 1")
Motor_1.run(Adafruit_MotorHAT.FORWARD);
time.sleep(1)

print("Motor 2")
Motor_2.run(Adafruit_MotorHAT.FORWARD);
time.sleep(1)

print("Motor 3")
Motor_3.run(Adafruit_MotorHAT.FORWARD);
time.sleep(1)

print("Motor 4")
Motor_4.run(Adafruit_MotorHAT.FORWARD);
time.sleep(1)


print("Motor 1")
Motor_1.run(Adafruit_MotorHAT.BACKWARD);
time.sleep(1)

print("Motor 2")
Motor_2.run(Adafruit_MotorHAT.BACKWARD);
time.sleep(1)

print("Motor 3")
Motor_3.run(Adafruit_MotorHAT.BACKWARD);
time.sleep(1)

print("Motor 4")
Motor_4.run(Adafruit_MotorHAT.BACKWARD);
time.sleep(1)

turnOffMotors()

#while (True):
#    print "Forward! "
#    myMotor.run(Adafruit_MotorHAT.FORWARD)
#
#    print "\tSpeed up..."
#    for i in range(255):
#        myMotor.setSpeed(i)
#        time.sleep(0.01)
#
#    print "\tSlow down..."
#    for i in reversed(range(255)):
#        myMotor.setSpeed(i)
#        time.sleep(0.01)
#
#    print "Backward! "
#    myMotor.run(Adafruit_MotorHAT.BACKWARD)
#
#    print "\tSpeed up..."
#    for i in range(255):
#        myMotor.setSpeed(i)
#        time.sleep(0.01)
#
#    print "\tSlow down..."
#    for i in reversed(range(255)):
#        myMotor.setSpeed(i)
#        time.sleep(0.01)
#
#    print "Release"
#    myMotor.run(Adafruit_MotorHAT.RELEASE)
#    time.sleep(1.0)
