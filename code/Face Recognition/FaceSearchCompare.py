import cv2
from simple_facerec import SimpleFacerec

#Encode faces from the images folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

#Initializes the camera
cam = cv2.VideoCapture(0)



#Compares a list of detected faces with a search variable and returns True if faces matches the search variable and False if it does not.
def face_detect (face):
    face_recognized = False
    while (True):
        ret, frame = cam.read()
        
        #Detect faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        
        #Recieves a list of faces detected by the simple face recognition.
        #face_locations, face_names = sfr.detect_known_faces(frame)
        #for name in zip(face_names):
         #Display face locations and names.
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        
            #Display name on face. (name, location, font, text size, text color, text thickness)
            #cv2.putText(frame, name,(x1, y1 -10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            #Draw rectangle around face. (location, color, frame width)
            #cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 2) 
            #If the name of the user is detected then set variable to True to end the loop.
            if name == face:
                face_recognized = True
                print("Face Found")
                print(x1, y1, x2, y2)
        #resize = cv2.resize(frame, (720, 720))
        #cv2.imshow('FaceTest', resize)   
        

        #Ends the loop if the esc key is pressed.
        key = cv2.waitKey(1)
        if key == 27:
            break
        
face_detect("Sean Connery")

#Displays True or False to the screen if the face was detected.
#print(face_recognized)

cam.release()
cv2.destroyAllWindows()
