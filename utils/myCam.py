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


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.image_label = QtWidgets.QLabel(self)
        self.image_label.resize(640, 480)

        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.video_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

    @QtCore.pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
        return QtGui.QPixmap.fromImage(p)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())