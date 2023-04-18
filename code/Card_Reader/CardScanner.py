import cv2
import numpy as np
import os

# Ensure that interpreter's working directory is the same as the location of the script file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Use the following values to crop to the corner of the card
CORNER_HEIGHT_RATIO = 2/3
CORNER_WIDTH_RATIO = 1/4

# Load all suit and rank template images before starting the loop
ranks = {"ace","2","3","4","5","6","7","8","9","10","jack","queen","king"}
suits = {"clubs", "diamonds", "hearts", "spades"}
rankTemplates = {}
suitTemplates = {}

for rank in ranks:
    rankTemplates[rank] = cv2.imread(f"Ranks/{rank}.png", cv2.IMREAD_GRAYSCALE)
for suit in suits:
    suitTemplates[suit] = cv2.imread(f"Suits/{suit}.png", cv2.IMREAD_GRAYSCALE)

# Initialize camera object
cap = cv2.VideoCapture(0)

def picture(thresh, crop, offset):
    # Create contours to isolate the rank/suit from the image passed in
    contours, hierarchy = cv2.findContours(crop, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    x, y, w, h = cv2.boundingRect(contours[1])

    return thresh[y+offset:y+h+offset, x:x+w]

def matchValue(test, template):
    # Get the dimensions of the template image
    templateHeight, templateWidth = template.shape[:2]

    # Determine the scale factor for resizing the test image
    scale = min(templateWidth/test.shape[1], templateHeight/test.shape[0])

    # Resize the test image while maintaining its aspect ratio
    test = cv2.resize(test, None, fx=scale, fy=scale)

    # Create a white background image with the same dimensions as the template image
    background = np.ones((template.shape[0], template.shape[1]), dtype=np.uint8) * 255

    # Determine the position to paste the resized image onto the white background
    x = int((templateWidth - test.shape[1]) / 2)
    y = int((templateHeight - test.shape[0]) / 2)

    # Paste the resized image onto the white background
    background[y:y+test.shape[0], x:x+test.shape[1]] = test

    # Perform the template match with the template image
    match_result = cv2.matchTemplate(background, template, cv2.TM_CCOEFF_NORMED)

    # Get the maximum value from the match result
    _, maxVal, _, _ = cv2.minMaxLoc(match_result)

    return maxVal

def scanCard():
    rankPic = None
    suitPic  = None
    printRank = "None"
    printSuit = "None"
    bestRank = 0
    bestSuit = 0

    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Crop the frame to show only the suit and rank
    fh, fw, c = frame.shape
    frame = frame[:int(fh*CORNER_HEIGHT_RATIO), :int(fw*CORNER_WIDTH_RATIO)]
    
    # Convert the frame to grayscale then apply a threshold to improve reading accuracy
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    y, x = thresh.shape
    rankPic = picture(thresh, thresh[0:int(y/2),0:x], 0)
    suitPic = picture(thresh, thresh[int(y/2):y,0:x], int(y/2))

    # Use each cropped image to determine their respective value of the suit and card rank
    for rank in rankTemplates:
        match = matchValue(rankPic, rankTemplates[rank])
        if match > bestRank:
            bestRank = match
            printRank = rank

    for suit in suitTemplates:
        match = matchValue(suitPic, suitTemplates[suit])
        if match > bestSuit:
            bestSuit = match
            printSuit = suit
            
    return f"{printRank}_of_{printSuit}"