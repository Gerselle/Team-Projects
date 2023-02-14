import cv2
import os

# Ensure that interpreter's working directory is the same as the location of the CardScanner.py file 
os.chdir(os.getcwd())

# IMPORTANT: Make sure image file names match up with the arrays below
suits = {"Clubs", "Diamonds", "Hearts", "Spades"}
values = {"Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"}


def scanCard():

    # TODO: Object for default camera of the system, might need to change when player camera is added
    camera = cv2.VideoCapture(0)

    # Variables to determine most accurate card reading
    bestSuit = 0 
    bestValue = 0
    printSuit = "Clubs"
    printValue = "Ace"

    # Take a single frame from the camera feed
    ret, frame = camera.read()

    # Convert frame from RGB to greyscale, then apply threshold for better reading
    check = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(check, 125, 255, cv2.THRESH_BINARY)

    # For both suits and value (17 checks a frame), look for the most accurate "suit of value" reading
    for suit in suits:
        suitPic =  cv2.imread("Suits/" + suit + ".png",  cv2.IMREAD_GRAYSCALE)
        test = cv2.matchTemplate(thresh, suitPic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(test)

        if max_val > bestSuit:
            bestSuit = max_val
            printSuit = suit
        
    for value in values:
        valuePic =  cv2.imread("Values/" + value + ".png",  cv2.IMREAD_GRAYSCALE)
        test = cv2.matchTemplate(thresh, valuePic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(test)

        if max_val > bestValue:
            bestValue = max_val
            printValue = value

    camera.release()
    return printValue + " of " + printSuit