from CaptureandDetect import detect
import cv2
from tensorflow import keras
import os
import numpy as np
from ModelPreTrained import ModelDeployed

def gen_frames():
    save_path = 'C://Users//VOLKAN MAZLUM//Desktop//ProjeData'
    video_capture = cv2.VideoCapture(0)
    while True:
        success, frame = video_capture.read()
        if not success:
            break
        else:      # Create the output folder
                    output_folder = save_path
                    if not os.path.exists(output_folder):
                        os.makedirs(output_folder)
                    # Process each frame in the video stream
                    counter_yawn= 0 
                    counter_eye = 0
                    model, eye_cascade, face_cascade = ModelDeployed()
                    while True:
                        ret, frame = video_capture.read()
                        if not ret:
                            break
                        frame,counter_yawn, counter_eye = detect(frame, output_folder,counter_yawn, counter_eye,model, eye_cascade, face_cascade)
                        #cv2.imshow('Frame', frame)
                        ret, buffer = cv2.imencode('.jpg', frame)
                        frame = buffer.tobytes()
                        yield (b'--frame\r\n'
                                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                        # Exit the program when 'q' is pressed
                        if cv2.waitKey(1) == ord('q'):
                            break
