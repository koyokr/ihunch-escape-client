from utils.app_layout import Ui_MainWindow
from PyQt5 import QtCore
import datetime
import cv2

class Setting(Ui_MainWindow):

    """탭바 클릭 이벤트 부여"""

    def clickable(self, widget):
        class Filter(QtCore.QObject):

            clicked = QtCore.pyqtSignal()  # pyside2 사용자는 pyqtSignal() -> Signal()로 변경

            def eventFilter(self, obj, event):

                if obj == widget:
                    if event.type() == QtCore.QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            # The developer can opt for .emit(obj) to get the object within the slot.
                            return True

                return False

        filter = Filter(widget)
        widget.installEventFilter(filter)
        return filter.clicked


class Timer(QtCore.QThread):

    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer()
        print("hid")

    def run(self):
        self.timer.setInterval(self.ui.now_capturecycle)
        self.timer.timeout.connect(self.captureImage)
        self.timer.start
        print("hi")

    """이미지 캡쳐하기"""
    #현재 시간 가져오기
    def getNow(self):
        now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        return now

    #이미지 캡쳐
    def captureImage(self, image):
        now = self.getNow()
        cv2.imwrite("C:/pythonproject/pyqt/pythonProject1/savedimage/" + str(now) + ".png", image)