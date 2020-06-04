import cv2
import time
import os
import VideoStream
import Cards

IM_WIDTH = 1280
IM_HEIGHT = 720
FRAME_RATE = 10

frame_rate_calc = 1
freq = cv2.getTickFrequency()
font = cv2.FONT_HERSHEY_SIMPLEX

videostream = VideoStream.VideoStream((IM_WIDTH, IM_HEIGHT), FRAME_RATE, 2,
                                      'localhost').start()
time.sleep(1)

path = os.path.dirname(os.path.abspath(__file__))

def most_frequent(List):
    return max(set(List), key=List.count)

cam_quit = 0
while cam_quit == 0:
    image = videostream.read()
    t1 = cv2.getTickCount()
    pre_proc = Cards.preprocess_image(image)
    cnts_sort, cnt_is_card = Cards.find_cards(pre_proc)


    break

cv2.destroyAllWindows()
videostream.stop()
