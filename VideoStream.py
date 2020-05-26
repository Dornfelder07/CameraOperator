import cv2
from threading import Thread

class VideoStream:
    """Camera object"""
    def __init__(self, resolution=(640,480),framerate=10,PiOrUSB=1,src=0):
        self.PiOrUSB = PiOrUSB
        self.stopped = False

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

    def update(self):
        for f in self.stream:
            self.frame = f.array
            self.rawCapture.truncate(0)

            if self.stopped:
                self.stream.close()
                self.rawCapture.close()
                self.camera.close()
