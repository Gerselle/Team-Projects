import time
import board
from adafruit_motorkit import MotorKit

moto1 = MotorKit()
moto2 = MotorKit(address = 0x62)

def shuffle():

    moto1.motor1.throttle = -.4
    moto2.motor1.throttle = .4
    time.sleep(8)

    moto1.motor1.throttle = None
    moto2.motor1.throttle = None

#Remove this after integrating with main code.
shuffle()
