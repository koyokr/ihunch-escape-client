import sys
import cv2
from utils import app_layout, button_setting, my_cam
from PyQt5 import QtCore, QtWidgets, QtGui

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
    # """on_off 버튼 누를 때 한쪽은 꺼지게 하기"""
    # ui.alarmOnButton.clicked.connect(ui.clickOnButton)
    # ui.alarmOffButton.clicked.connect(ui.clickOffButton)
    # ui.changeApply()

    # helper = connect_helper.Setting()
    # helper.clickable(ui.tabWidget.tabBar()).connect(ui.returnToNow)
    #
    # ui.applyButton.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(ui.changeApply)
    # ui.applyButton.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(ui.returnInitial)

    MainWindow.show()
    sys.exit(app.exec_())