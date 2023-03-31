import os
import tensorflow as tf
from tensorflow import keras
import PIL
from picamera import Picamera
import time

classes = ['paper', 'plastic', 'glass', 'metal', 'other', 'empty']

# Import model from weights
model = keras.models.load_model('models/imagenet_transfer.h5')

# Set up Picamera
camera = Picamera()
camera.resolution = (500, 500)

# Allow camera to warm up
time.sleep(2)

while True:
    # Capture image and save to temp file 
    camera.capture('current.jpg')
   
    # Preprocess image
    image = keras.preprocessing.image.load_img('current.jpg', target_size=(500, 500))
    img_arr = keras.preprocessing.image.img_to_arr(image)
    img_arr = img_arr.reshape((1, my_image.shape[0], my_image.shape[1], my_image.shape[2]))
    img_arr = keras.applications.vgg16.preprocess_input(img_arr)
    
    # Get prediction
    pred_list = model.predict(img_arr)
    max_val = max(pred_list)
    pred = pred_list.index(max_val)

    if pred != 5: # If there is in an object (not empty)
        print(classes[pred])
