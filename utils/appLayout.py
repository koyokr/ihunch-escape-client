# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import cv2
from utils.myCam import VideoThread
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 709)
        MainWindow.setMinimumSize(QtCore.QSize(689, 709))
        MainWindow.setMaximumSize(QtCore.QSize(689, 709))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 691, 711))
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(144, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.realTime = QtWidgets.QWidget()
        self.realTime.setObjectName("realTime")
        self.videoFrame = QtWidgets.QGroupBox(self.realTime)
        self.videoFrame.setGeometry(QtCore.QRect(12, 10, 661, 511))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.videoFrame.setFont(font)
        self.videoFrame.setObjectName("videoFrame")
        self.videoImage = QtWidgets.QLabel(self.videoFrame)
        self.videoImage.setGeometry(QtCore.QRect(10, 20, 640, 480))
        self.videoImage.setFrameShape(QtWidgets.QFrame.Panel)
        self.videoImage.setText("")
        self.videoImage.setObjectName("videoImage")
        self.warningFrame_1 = QtWidgets.QGroupBox(self.realTime)
        self.warningFrame_1.setGeometry(QtCore.QRect(12, 530, 661, 141))
        self.warningFrame_1.setTitle("")
        self.warningFrame_1.setFlat(False)
        self.warningFrame_1.setCheckable(False)
        self.warningFrame_1.setObjectName("warningFrame_1")
        self.warning_turtle = QtWidgets.QLabel(self.warningFrame_1)
        self.warning_turtle.setGeometry(QtCore.QRect(266, 10, 130, 130))
        self.warning_turtle.setText("")
        self.warning_turtle.setPixmap(QtGui.QPixmap("resource/realtime_warning_red.png"))
        self.warning_turtle.setObjectName("warning_turtle")
        self.warning_bg = QtWidgets.QLabel(self.warningFrame_1)
        self.warning_bg.setGeometry(QtCore.QRect(0, 0, 661, 141))
        self.warning_bg.setAutoFillBackground(False)
        self.warning_bg.setStyleSheet("rgb255, 0, 0")
        self.warning_bg.setText("")
        self.warning_bg.setObjectName("warning_bg")
        self.warning_bg.raise_()
        self.warning_turtle.raise_()
        self.warningFrame_1.raise_()
        self.videoFrame.raise_()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/realtime_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.realTime, icon, "")
        self.ratio = QtWidgets.QWidget()
        self.ratio.setObjectName("ratio")
        self.barGraphFrame = QtWidgets.QGroupBox(self.ratio)
        self.barGraphFrame.setGeometry(QtCore.QRect(12, 10, 661, 511))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.barGraphFrame.setFont(font)
        self.barGraphFrame.setObjectName("barGraphFrame")
        self.barGraph = QtWidgets.QLabel(self.barGraphFrame)
        self.barGraph.setGeometry(QtCore.QRect(10, 20, 640, 480))
        self.barGraph.setFrameShape(QtWidgets.QFrame.Panel)
        self.barGraph.setText("")
        self.barGraph.setObjectName("barGraph")
        self.warningFrame_2 = QtWidgets.QGroupBox(self.ratio)
        self.warningFrame_2.setGeometry(QtCore.QRect(12, 530, 661, 141))
        self.warningFrame_2.setTitle("")
        self.warningFrame_2.setFlat(False)
        self.warningFrame_2.setCheckable(False)
        self.warningFrame_2.setObjectName("warningFrame_2")
        self.warning_turtle_2 = QtWidgets.QLabel(self.warningFrame_2)
        self.warning_turtle_2.setGeometry(QtCore.QRect(266, 10, 130, 130))
        self.warning_turtle_2.setText("")
        self.warning_turtle_2.setPixmap(QtGui.QPixmap("resource/realtime_warning_red.png"))
        self.warning_turtle_2.setObjectName("warning_turtle_2")
        self.warning_bg_2 = QtWidgets.QLabel(self.warningFrame_2)
        self.warning_bg_2.setGeometry(QtCore.QRect(0, 0, 661, 141))
        self.warning_bg_2.setText("")
        self.warning_bg_2.setObjectName("warning_bg_2")
        self.warning_bg_2.raise_()
        self.warning_turtle_2.raise_()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resource/ratio_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.ratio, icon1, "")
        self.setting = QtWidgets.QWidget()
        self.setting.setObjectName("setting")
        self.settingFrame = QtWidgets.QGroupBox(self.setting)
        self.settingFrame.setGeometry(QtCore.QRect(12, 10, 661, 661))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.settingFrame.setFont(font)
        self.settingFrame.setObjectName("settingFrame")
        self.applyButton = QtWidgets.QDialogButtonBox(self.settingFrame)
        self.applyButton.setGeometry(QtCore.QRect(480, 370, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.applyButton.setFont(font)
        self.applyButton.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Reset)
        self.applyButton.setObjectName("applyButton")
        self.captureCycleFrame = QtWidgets.QGroupBox(self.settingFrame)
        self.captureCycleFrame.setGeometry(QtCore.QRect(20, 40, 621, 81))
        self.captureCycleFrame.setObjectName("captureCycleFrame")
        self.captureCycleBox = QtWidgets.QSpinBox(self.captureCycleFrame)
        self.captureCycleBox.setGeometry(QtCore.QRect(10, 30, 601, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.captureCycleBox.setFont(font)
        self.captureCycleBox.setWrapping(False)
        self.captureCycleBox.setFrame(True)
        self.captureCycleBox.setReadOnly(False)
        self.captureCycleBox.setMinimum(5)
        self.captureCycleBox.setMaximum(60)
        self.captureCycleBox.setProperty("value", 10)
        self.captureCycleBox.setObjectName("captureCycleBox")
        self.warningCycleFrame = QtWidgets.QGroupBox(self.settingFrame)
        self.warningCycleFrame.setGeometry(QtCore.QRect(20, 150, 621, 81))
        self.warningCycleFrame.setObjectName("warningCycleFrame")
        self.warningCycleBox = QtWidgets.QSpinBox(self.warningCycleFrame)
        self.warningCycleBox.setGeometry(QtCore.QRect(10, 30, 601, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.warningCycleBox.setFont(font)
        self.warningCycleBox.setFrame(True)
        self.warningCycleBox.setMinimum(1)
        self.warningCycleBox.setMaximum(60)
        self.warningCycleBox.setProperty("value", 5)
        self.warningCycleBox.setObjectName("warningCycleBox")
        self.alarmFrame = QtWidgets.QGroupBox(self.settingFrame)
        self.alarmFrame.setGeometry(QtCore.QRect(20, 260, 621, 81))
        self.alarmFrame.setObjectName("alarmFrame")
        self.alarmOnButtonLabel = QtWidgets.QLabel(self.alarmFrame)
        self.alarmOnButtonLabel.setGeometry(QtCore.QRect(100, 30, 211, 31))
        self.alarmOnButtonLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.alarmOnButtonLabel.setText("")
        self.alarmOnButtonLabel.setObjectName("alarmOnButtonLabel")
        self.alarmOffButtonLabel = QtWidgets.QLabel(self.alarmFrame)
        self.alarmOffButtonLabel.setGeometry(QtCore.QRect(310, 30, 211, 31))
        self.alarmOffButtonLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.alarmOffButtonLabel.setText("")
        self.alarmOffButtonLabel.setObjectName("alarmOffButtonLabel")
        self.alarmOnButton = QtWidgets.QPushButton(self.alarmFrame)
        self.alarmOnButton.setGeometry(QtCore.QRect(100, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.alarmOnButton.setFont(font)
        self.alarmOnButton.setAutoFillBackground(False)
        self.alarmOnButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.alarmOnButton.setCheckable(True)
        self.alarmOnButton.setChecked(False)
        self.alarmOnButton.setAutoRepeat(False)
        self.alarmOnButton.setDefault(False)
        self.alarmOnButton.setFlat(True)
        self.alarmOnButton.setObjectName("alarmOnButton")
        self.alarmOffButton = QtWidgets.QPushButton(self.alarmFrame)
        self.alarmOffButton.setGeometry(QtCore.QRect(310, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.alarmOffButton.setFont(font)
        self.alarmOffButton.setAutoFillBackground(False)
        self.alarmOffButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.alarmOffButton.setCheckable(True)
        self.alarmOffButton.setChecked(True)
        self.alarmOffButton.setAutoRepeat(False)
        self.alarmOffButton.setDefault(True)
        self.alarmOffButton.setFlat(True)
        self.alarmOffButton.setObjectName("alarmOffButton")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resource/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.setting, icon2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.thread = VideoThread()
        self.thread.video_signal.connect(self.update_image)
        self.thread.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TurtleNeck"))
        MainWindow.setWindowIcon(QtGui.QIcon("resource/app_icon.png"))
        self.videoFrame.setTitle(_translate("MainWindow", "화상카메라"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.realTime), _translate("MainWindow", "실시간 화면"))
        self.barGraphFrame.setTitle(_translate("MainWindow", "막대그래프"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ratio), _translate("MainWindow", "거북목 통계"))
        self.settingFrame.setTitle(_translate("MainWindow", "설정"))
        self.captureCycleFrame.setTitle(_translate("MainWindow", "이미지 촬영 주기(초)"))
        self.warningCycleFrame.setTitle(_translate("MainWindow", "경고 알림 주기(분)"))
        self.alarmFrame.setTitle(_translate("MainWindow", "알람 설정"))
        self.alarmOnButton.setText(_translate("MainWindow", "On"))
        self.alarmOffButton.setText(_translate("MainWindow", "Off"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting), _translate("MainWindow", "환경설정"))

    def update_image(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.videoImage.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch*w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
        return QtGui.QPixmap.fromImage(p)

    def clickOnButton(self):
        self.alarmOnButton.setChecked(True)
        self.alarmOffButton.setChecked(False)

    def clickOffButton(self):
        self.alarmOnButton.setChecked(False)
        self.alarmOffButton.setChecked(True)



    """환경 설정 변경 사항 저장"""
    #변경사항 저장

    def changeApply(self):
        self.now_capturecycle = self.getCaptureCycle()
        self.now_warningcycle = self.getWarningCycle()
        self.now_turn = self.getAlarmOn_Off()
        self.captureCycleBox.setProperty("value", self.now_capturecycle)
        self.warningCycleBox.setProperty("value", self.now_warningcycle)
        if self.now_turn:
            self.clickOnButton()
        else:
            self.clickOffButton()

    #촬영 주기 값 가져오기
    def getCaptureCycle(self):
        capturecycle = self.captureCycleBox.value()
        return capturecycle

    #알림 주기 값 가져오기
    def getWarningCycle(self):
        warningcycle = self.warningCycleBox.value()
        return warningcycle

    #알림 설정 값 가져오기
    def getAlarmOn_Off(self):
        turn = self.alarmOnButton.isChecked()
        return turn


    """환경설정 탭 클릭"""
    #저장안된 변경사항 제거
    def returnToNow(self):
        self.undoCaptureCycle()
        self.undoWarningCycle()
        self.undoAlarmOn_Off()

    #이미지 촬영 주기 변경
    def undoCaptureCycle(self):
        self.captureCycleBox.setValue(self.now_capturecycle)

    #경고 알림 주기 변경
    def undoWarningCycle(self):
        self.warningCycleBox.setValue(self.now_warningcycle)

    #알람 설정 변경
    def undoAlarmOn_Off(self):
        if self.now_turn:
            self.clickOnButton()
        else:
            self.clickOffButton()

    """환경설정 초기화"""
    def returnInitial(self):
        self.now_capturecycle = 10
        self.now_warningcycle = 5
        self.now_turn = False
        self.captureCycleBox.setValue(self.now_capturecycle)
        self.warningCycleBox.setValue(self.now_warningcycle)
        self.clickOffButton()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

