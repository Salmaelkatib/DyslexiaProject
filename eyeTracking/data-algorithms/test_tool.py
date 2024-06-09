import cv2
import dlib
import os
import numpy as np

# Absolute path to the shape predictor file
predictor_path = "d:/DyslexiaProject/eye_tracking/shape_predictor_68_face_landmarks.dat"

# Check if the file exists
if not os.path.isfile(predictor_path):
    raise FileNotFoundError(f"The file {predictor_path} does not exist. Please check the path and try again.")

# Load the pre-trained facial landmark predictor
predictor = dlib.shape_predictor(predictor_path)
detector = dlib.get_frontal_face_detector()

# Define a function to get the coordinates of the left and right eyes
def get_eye_coordinates(shape):
    left_eye = np.array(shape[36:42])
    right_eye = np.array(shape[42:48])
    left_eye_coords = left_eye.mean(axis=0).astype(int)
    right_eye_coords = right_eye.mean(axis=0).astype(int)
    return left_eye_coords, right_eye_coords

# Open a connection to the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = detector(gray)
    
    for face in faces:
        # Get the landmarks for the face
        shape = predictor(gray, face)
        shape = [(p.x, p.y) for p in shape.parts()]
        
        # Get the coordinates of the left and right eyes
        left_eye_coords, right_eye_coords = get_eye_coordinates(shape)
        
        # Print the x, y coordinates of each eye
        print(f"Left eye coordinates: {left_eye_coords}")
        print(f"Right eye coordinates: {right_eye_coords}")
        
        # Draw circles at the eye coordinates
        cv2.circle(frame, tuple(left_eye_coords), 3, (0, 255, 0), -1)
        cv2.circle(frame, tuple(right_eye_coords), 3, (0, 255, 0), -1)
        
        # Optionally, draw the full set of landmarks
        for (x, y) in shape:
            cv2.circle(frame, (x, y), 1, (255, 0, 0), -1)
    
    # Display the resulting frame
    cv2.imshow('Video', frame)
    
    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture and close windows
video_capture.release()
cv2.destroyAllWindows()