import cv2
from simple_facerec import SimpleFacerec

#Encode faces from the images folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

#Initializes the camera
cam = cv2.VideoCapture(2)

face_recognized = False

#Compares a list of detected faces with a search variable and returns True if faces matches the search variable and False if it does not.
def face_detect (face):
    while face_recognized == False:
        ret, frame = cap.read()

        #Recieves a list of faces detected by the simple face recognition.
        face_locations, face_names = sfr.detect_known_faces(frame)
        for name in zip(face_names):
            
            #If the name of the user is detected then set variable to True to end the loop.
            if name == face
                face_recognized = True

        #Ends the loop if the esc key is pressed.
        key = cv2.waitKey(1)
        if key == 27:
            break
        
face_detect("variable_name")

#Displays True or False to the screen if the face was detected.
print(face_recognized)

cam.release()
cv2.destroyAllWindows()
