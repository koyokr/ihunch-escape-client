from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import cv2
import numpy as np
import datetime


class VideoThread(QtCore.QThread):
    video_signal = QtCore.pyqtSignal(np.ndarray)

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, image = cap.read()
            if ret:
                self.video_signal.emit(image)