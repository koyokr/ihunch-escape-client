# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TurtleNeck(object):
    def setupUi(self, TurtleNeck):
        TurtleNeck.setObjectName("TurtleNeck")
        TurtleNeck.resize(689, 709)
        TurtleNeck.setMinimumSize(QtCore.QSize(689, 709))
        TurtleNeck.setMaximumSize(QtCore.QSize(689, 709))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TurtleNeck.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TurtleNeck)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 691, 711))
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(143, 20))
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
        self.warning_red = QtWidgets.QLabel(self.warningFrame_1)
        self.warning_red.setGeometry(QtCore.QRect(0, 0, 326, 141))
        self.warning_red.setText("")
        self.warning_red.setPixmap(QtGui.QPixmap("../resource/realtime_warning_red.png"))
        self.warning_red.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_red.setObjectName("warning_red")
        self.warning_blue = QtWidgets.QLabel(self.warningFrame_1)
        self.warning_blue.setGeometry(QtCore.QRect(330, 0, 331, 141))
        self.warning_blue.setText("")
        self.warning_blue.setPixmap(QtGui.QPixmap("../resource/realtime_warning.png"))
        self.warning_blue.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_blue.setObjectName("warning_blue")
        self.warningFrame_1.raise_()
        self.videoFrame.raise_()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../resource/realtime_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.realTime, icon1, "")
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
        self.warning_red_2 = QtWidgets.QLabel(self.warningFrame_2)
        self.warning_red_2.setGeometry(QtCore.QRect(0, 0, 326, 141))
        self.warning_red_2.setText("")
        self.warning_red_2.setPixmap(QtGui.QPixmap("../resource/realtime_warning_red.png"))
        self.warning_red_2.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_red_2.setObjectName("warning_red_2")
        self.warning_blue_2 = QtWidgets.QLabel(self.warningFrame_2)
        self.warning_blue_2.setGeometry(QtCore.QRect(330, 0, 331, 141))
        self.warning_blue_2.setText("")
        self.warning_blue_2.setPixmap(QtGui.QPixmap("../resource/realtime_warning.png"))
        self.warning_blue_2.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_blue_2.setObjectName("warning_blue_2")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../resource/ratio_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.ratio, icon2, "")
        self.setting = QtWidgets.QWidget()
        self.setting.setObjectName("setting")
        self.settingFrame = QtWidgets.QGroupBox(self.setting)
        self.settingFrame.setGeometry(QtCore.QRect(12, 12, 661, 661))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../resource/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.setting, icon3, "")
        TurtleNeck.setCentralWidget(self.centralwidget)

        self.retranslateUi(TurtleNeck)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TurtleNeck)

    def retranslateUi(self, TurtleNeck):
        _translate = QtCore.QCoreApplication.translate
        TurtleNeck.setWindowTitle(_translate("TurtleNeck", "Turtleneck"))
        self.videoFrame.setTitle(_translate("TurtleNeck", "화상카메라"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.realTime), _translate("TurtleNeck", "실시간 화면"))
        self.barGraphFrame.setTitle(_translate("TurtleNeck", "막대그래프"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ratio), _translate("TurtleNeck", "거북목 통계"))
        self.settingFrame.setTitle(_translate("TurtleNeck", "설정"))
        self.captureCycleFrame.setTitle(_translate("TurtleNeck", "이미지 촬영 주기(초)"))
        self.warningCycleFrame.setTitle(_translate("TurtleNeck", "경고 알림 주기(분)"))
        self.alarmFrame.setTitle(_translate("TurtleNeck", "알람 설정"))
        self.alarmOnButton.setText(_translate("TurtleNeck", "On"))
        self.alarmOffButton.setText(_translate("TurtleNeck", "Off"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting), _translate("TurtleNeck", "환경설정"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TurtleNeck = QtWidgets.QMainWindow()
    ui = Ui_TurtleNeck()
    ui.setupUi(TurtleNeck)
    TurtleNeck.show()
    sys.exit(app.exec_())

