import sys
from lib import appLayout, imageCapture, connectHelper
from PyQt5 import QtCore, QtWidgets, QtGui

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = appLayout.Ui_MainWindow()
    ui.setupUi(MainWindow)
    """on_off 버튼 누를 때 한쪽은 꺼지게 하기"""
    ui.alarmOnButton.clicked.connect(ui.clickOnButton)
    ui.alarmOffButton.clicked.connect(ui.clickOffButton)
    ui.changeApply()

    helper = connectHelper.Setting()
    helper.clickable(ui.tabWidget.tabBar()).connect(ui.returnToNow)

    ui.applyButton.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(ui.changeApply)
    ui.applyButton.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(ui.returnInitial)

    MainWindow.show()
    sys.exit(app.exec_())