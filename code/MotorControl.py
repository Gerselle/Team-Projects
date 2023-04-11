import time
import board
from adafruit_motorkit import MotorKit
import card_reader.CardScanner as CardScanner

kit1 = MotorKit()
kit2 = MotorKit(address = 0x62)

#Rotates the shuffler motors to shuffle a deck of cards.
def shuffle():

    kit1.motor2.throttle = -.4
    kit1.motor3.throttle = .4
    time.sleep(3)

    kit1.motor2.throttle = None
    kit1.motor3.throttle = None

#Rotates the dealer motor to deal cards to players.
def deal(facedUp):

    card = CardScanner.scanCard()

    if(facedUp):
        kit1.motor4.throttle = 0.5
        time.sleep(0.5)
        kit1.motor4.throttle = None
    else:
        kit1.motor4.throttle = -0.5
        time.sleep(0.5)
        kit1.motor4.throttle = None
        
    return card

#Rotates the turntable motor to turn the robot left or right.
def turntable(right):

    if(right):
        
    else:

#Remove this after integrating with main code.
shuffle()
