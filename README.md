# Movement Service for Man in the Pi Castle

## Thor_Control.py

This must be run on a RaspberryPi.

Run this via `sudo python3 Thor_Control.py` and it will start an API service running on port 8080.  This will allow control of the robot via the api defined in the swagger directory.

## External Libraries

### ikpy

This is an inverse kinematics python modules that can do the calculations for the robot.

https://github.com/Phylliade/ikpy

### matplotlib

Allows plotting of the inverse kinematics.

### Adafruit motor hat library

This is for controlling the stepper motors via the Adafruit stepper motor hat

https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library

