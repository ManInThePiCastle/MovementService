#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import curses

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

def input_char(message):
    try:                                  
        win = curses.initscr()            
        win.addstr(0, 0, message)         
        while True:                       
            ch = win.getch()              
            if ch in range(32, 127): break
            time.sleep(0.05)              
    except: raise                         
    finally:                              
        curses.endwin()                   
    return chr(ch)                        

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

dwell_time = 1

while True:
    command = input_char("Command (x to quit):")
    if command.lower() == 'x':
        exit(0)
    elif command == '1':
        Motor_1.run(Adafruit_MotorHAT.FORWARD);
        time.sleep(dwell_time)
        Motor_1.run(Adafruit_MotorHAT.RELEASE)
    elif command == '2':
        Motor_2.run(Adafruit_MotorHAT.FORWARD);
        time.sleep(dwell_time)
        Motor_2.run(Adafruit_MotorHAT.RELEASE)
    elif command == '3':
        Motor_3.run(Adafruit_MotorHAT.FORWARD);
        time.sleep(dwell_time)
        Motor_3.run(Adafruit_MotorHAT.RELEASE)
    elif command == '4':
        Motor_4.run(Adafruit_MotorHAT.FORWARD);
        time.sleep(dwell_time)
        Motor_4.run(Adafruit_MotorHAT.RELEASE)
    elif command.lower() == 'q':                    
        Motor_1.run(Adafruit_MotorHAT.BACKWARD);
        time.sleep(dwell_time)                 
        Motor_1.run(Adafruit_MotorHAT.RELEASE)  
    elif command.lower() == 'w':                    
        Motor_2.run(Adafruit_MotorHAT.BACKWARD);
        time.sleep(dwell_time)                 
        Motor_2.run(Adafruit_MotorHAT.RELEASE)
    elif command.lower() == 'e':                          
        Motor_3.run(Adafruit_MotorHAT.BACKWARD);     
        time.sleep(dwell_time)                       
        Motor_3.run(Adafruit_MotorHAT.RELEASE)        
    elif command.lower() == 'r':                          
        Motor_4.run(Adafruit_MotorHAT.BACKWARD);     
        time.sleep(dwell_time)                       
        Motor_4.run(Adafruit_MotorHAT.RELEASE)       
