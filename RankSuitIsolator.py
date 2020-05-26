import os
from picamera.array import PiRGBArray
from picamera import PiCamera

IM_WIDTH = 1280
IM_HEIGHT = 720
RANK_WIDTH = 70
RANK_HEIGHT = 125
SUIT_WIDTH = 70
SUIT_HEIGHT = 100

img_path = os.path.dirname(os.path.abspath(__file__)) + '/CardsImg/'

camera = PiCamera()
camera.resolution = (IM_WIDTH,IM_HEIGHT)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(IM_WIDTH,IM_HEIGHT))