#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ml = Motor(Port.B)
mr = Motor(Port.C)
ts = TouchSensor(Port.S1)

while(1):

    if ts.pressed()==False:
        ml.stop()
        mr.stop()
    
    else:
        ml.run(300)
        mr.run(300)
         if ts.pressed()==False:
            ml.stop()
            mr.stop()
    
        else:
            ml.run(300)
            mr.run(300)