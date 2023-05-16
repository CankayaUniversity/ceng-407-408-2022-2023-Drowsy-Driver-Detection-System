import cv2
from tensorflow.keras import backend, layers
from tensorflow.keras.models import load_model
from PIL import Image
import winsound
import time
import tensorflow as tf
from tensorflow import keras
import os
import numpy as np

def ModelDeployed():
    class FixedDropout(layers.Dropout):
                def _get_noise_shape(self, inputs):
                    if self.noise_shape is None:
                           return self.noise_shape

                    symbolic_shape = backend.shape(inputs)
                    noise_shape = [symbolic_shape[axis] if shape is None else shape
                                               for axis, shape in enumerate(self.noise_shape)]
                    return tuple(noise_shape)

    model = keras.models.load_model('best.h5', compile=False,custom_objects={'FixedDropout':FixedDropout(rate=0.2)})
    model.compile(optimizer='adam',loss = 'sparse_categorical_crossentropy',metrics=['accuracy'])
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    return (model,eye_cascade,face_cascade)