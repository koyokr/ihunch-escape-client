from PyQt5 import QtGui, QtCore
import cv2
import numpy as np

class VideoThread(QtCore.QThread):
    VIDEO_SIGNAL = QtCore.pyqtSignal(np.ndarray)

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, image = cap.read()
            if ret:
                self.VIDEO_SIGNAL.emit(image)


class ShowVideo():

    # ui에 전처리된 이미지 실시간으로 적용
    def update_image(self, cv_img, cam_image):
        qt_img = self.convert_cv_qt(cv_img)
        cam_image.setPixmap(qt_img)

    # 가져온 실시간 이미지를 QLabel에 적용하기위한 전처리 함수
    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        heigth, width, ch = rgb_image.shape
        bytes_per_line = ch * width
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, width, heigth, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
        return QtGui.QPixmap.fromImage(p)