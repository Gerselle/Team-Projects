import cv2
import os
import sys

# Ensure that the current directory path is the same as the running python script
os.chdir(sys.path[0])

# Object for default cam of the system, might need to change when player cam is added
camera = cv2.VideoCapture(0)

# IMPORTANT: Make sure image file names match up with the arrays below
suits = {"Clubs", "Diamonds", "Hearts", "Spades"}
values = {"Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"}


while(True):

    # Take a single frame from the camera feed
    ret, frame = camera.read()

    # Exit if esc is pressed 
    k = cv2.waitKey(1)
    if k%256 == 27:
        break
    
    # Convert frame from RGB to greyscale, then apply threshold for better reading
    check = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(check, 125, 255, cv2.THRESH_BINARY)

    # Variable to determine most accurate card reading
    bestSuit = 0 
    bestValue = 0
    printSuit = "Clubs"
    printValue = "Ace"

    # For both suits and value (13 checks a frame), look for the most accurate "suit of value" reading
    for suit in suits:
        suitPic =  cv2.imread("suits\\" + suit + ".png",  cv2.IMREAD_GRAYSCALE)
        test = cv2.matchTemplate(thresh, suitPic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(test)

        if max_val > bestSuit:
            bestSuit = max_val
            printSuit = suit
        
    for value in values:
        valuePic =  cv2.imread("values\\" + value + ".png",  cv2.IMREAD_GRAYSCALE)
        test = cv2.matchTemplate(thresh, valuePic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(test)

        if max_val > bestValue:
            bestValue = max_val
            printValue = value

    # Show the output
    savedSuit = cv2.imread("suits\\" + printSuit + ".png",  cv2.IMREAD_GRAYSCALE)
    savedValue = cv2.imread("values\\" + printValue + ".png",  cv2.IMREAD_GRAYSCALE)

    thresh[0:savedValue.shape[0], 75 : 75 + savedValue.shape[1]] = savedValue
    thresh[savedValue.shape[0]: savedValue.shape[0] + savedSuit.shape[0], 75 : 75 + savedSuit.shape[1]] = savedSuit
    dim = (int(thresh.shape[1]/3), int(thresh.shape[0]/3))
    cv2.imshow("It's the", thresh)

camera.release()
cv2.destroyAllWindows()