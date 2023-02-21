from adafruit_motorkit import MotorKit
import card_reader.CardScanner as CardScanner


# IMPORTANT: Ensure that motorAddr is the IC2 address of the dealer motor
motorAddr = 0x60
kit = MotorKit(motorAddr)

#  Note that value of facedUp is dependent on the game that calls the function 
def deal(facedUp):

    card = CardScanner.scanCard()

    if(facedUp):
        kit.motor1.throttle = 0.5
    else:
        kit.motor1.throttle = -0.5

    return card