import sys
import cv2
from utils import my_cam, app_layout
from PyQt5 import QtCore, QtWidgets, QtGui


"""탭바 클릭 이벤트 부여"""
def clickable(widget):
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

# ui에 전처리된 이미지 실시간으로 적용
def update_image(cv_img):
    qt_img = convert_cv_qt(cv_img)
    ui.cam_image.setPixmap(qt_img)


# 가져온 실시간 이미지를 QLabel에 적용하기위한 전처리 함수
def convert_cv_qt(cv_img):
    rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    heigth, width, ch = rgb_image.shape
    bytes_per_line = ch * width
    convert_to_Qt_format = QtGui.QImage(rgb_image.data, width, heigth, bytes_per_line, QtGui.QImage.Format_RGB888)
    p = convert_to_Qt_format.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
    return QtGui.QPixmap.fromImage(p)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = app_layout.Ui_MainWindow()


    cam_thread = my_cam.VideoThread()
    cam_thread.VIDEO_SIGNAL.connect(update_image)
    cam_thread.start()

    ui.setupUi(MainWindow)

    # 초기 설정값 저장
    ui.apply_current_setting()
    # 저장되지 않은 설정 변경 값 삭제
    clickable(ui.tab_widget.tabBar()).connect(ui.return_current_setting)
    #apply 버튼 누룰 시 현재 변경 값 저장
    # ui.set_reset_button.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(ui.apply_current_setting)
    # #reset 버튼 누를 시 모든 설정 초기화
    # ui.set_reset_button.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(ui.return_initial_setting) #reset 버튼 누를 시 설정 초기화

    MainWindow.show()
    sys.exit(app.exec_())