
from datetime import datetime
from flask import Flask,render_template,g
from FlaskWebProject5 import app
import cv2
from tensorflow.keras import backend, layers
from tensorflow.keras.models import load_model
import winsound
import time
from PIL import Image
import tensorflow as tf
from tensorflow import keras
import os
import numpy as np

def detect(frame, output_folder,counter_yawn, counter_eye, model, eye_cascade, face_cascade):
             
                        # Define the function to detect eyes and yawning and save the output frames
                
                        duration = 1000  # in milliseconds
                        frequency = 440   # frequency of the sound in Hz

                        # Resize the frame to (256, 256) and convert to RGB
                        resized = cv2.resize(frame, (256, 256))
                        rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        rgb = rgb.reshape((1,256, 256,3))
                        eye_roi_rgb= rgb
    
                        # Detect faces in the image using Haar cascades
    
                        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
                        #try:
                            # Loop through each face in the image
                        for (x, y, w, h) in faces:
                                # Extract the face region from the input image
                            face_roi = gray[y:y+h, x:x+w]
                            # Detect eyes in the face region
                            eyes = eye_cascade.detectMultiScale(face_roi)

                            # Loop through each eye in the face region
                            for (ex, ey, ew, eh) in eyes:
                                # Extract the eye region from the face region
                                eye_roi = face_roi[ey:ey+eh, ex:ex+ew]
                                eye_roi = cv2.resize(eye_roi, (256, 256))

                                cv2.imwrite("eyes.png", eye_roi)
    
                        img_eye = cv2.imread("eyes.png")
                        # Increase brightness
                        brightness = 50
                        img_eye = cv2.add(img_eye, brightness)

                        # Apply contrast adjustment
                        alpha = 1.5
                        beta = 0
                        img_eye = cv2.convertScaleAbs(img_eye, alpha=alpha, beta=beta)

                        # Apply Gaussian blur
                        kernel_size = (5, 5)
                        sigma_x = 0
                        img_eye = cv2.GaussianBlur(img_eye, kernel_size, sigma_x)

                        # Display the original and improved images
                        img = img_eye.reshape((1,256, 256,3))
                        #rgb_img = rgb_img.astype('float32') / 255.0
    
                        predictions_eye = model.predict(img)
                        #print(predictions_eye)
                        predictions_mouth = model.predict(rgb)
                        if(predictions_eye[0][0] > 0.55):
                            label = "Closed"
                            counter_eye = counter_eye + 1
                        elif(predictions_eye[0][1] > 0.55):
                            label = "Open"
                            counter_eye = 0
                        else:
                            label =""

                        if(predictions_mouth[0][2] > 0.55):
                            label1 = "no_yawn"
                        elif(predictions_mouth[0][3] > 0.55):
                            label1 = "yawn"
                            counter_yawn = counter_yawn + 1
                        else:
                            label1=" "

                            # Draw the predicted labels on the frame
                        if (label == "Open" ):
                            cv2.putText(frame, "Normal.", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        elif(label == "Closed" and counter_eye > 12):
                            cv2.putText(frame, "Drowsiness is detected. Given alarm!!!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            time.sleep(0.2)
                            winsound.Beep(frequency, duration)
         
                        if (label1 == "yawn" and counter_yawn > 15):
                            #cv2.putText(frame, f"Yawn: {counter}", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            cv2.putText(frame, "Fatigue is detected. Please give break!", (10, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                  
                        return frame,counter_yawn,counter_eye
