import cv2
import datetime

class Capture():

    def getNow(self):
        now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        return now

    def saveImage(self, image):
        now = self.getNow()
        cv2.imwrite("../savedimage/" + str(now) + ".png", image)
