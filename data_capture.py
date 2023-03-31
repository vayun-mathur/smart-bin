from picamera import Picamera
from time import time
import random

# Set up classes
classes = ['paper', 'plastic', 'glass', 'metal', 'other', 'empty']
print(enumerate(classes))

# Initialize Picamera
camera = Picamera()
camera.resolution = (500, 500)
camera.start_preview()

# Allow camera to warm up
time.sleep(2)


while True:
    classId = input('> ')
    if classId not in range(0, len(classes)):
        print('Invalid input, please try again')
        continue
    
    cl = classes[classId]
    rand = random.randint(1, 100000) 

    camera.capture(f'~/home/Pi/Desktop/smart-bin/images/{cl}/{rand}.jpg') # Save with random id
