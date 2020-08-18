from PyQt5 import QtGui, QtCore

class IhunchWarn():

    def __init__(self):
        self.font = QtGui.QFont()
        self.font.setFamily("HY중고딕")
        self.font.setPointSize(50)
        self.font.setBold(True)
        self.font.setWeight(50)

    def status_ihunch(self, label):
        label.setFont(self.font)
        label.setText("거북목")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("color: black;"
                            "background-color: #FF0000;"
                            "border-style: solid;"
                            # "border-width: 5px;"
                            # "border-radius: 3px"
                            )

    def status_normal(self, label):
        label.setFont(self.font)
        label.setText("정상")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("color: black;"
                            "background-color: #23f200;"
                            "border-style: solid;"
                            # "border-width: 5px;"
                            # "border-radius: 3px"
                            )

    def status_no_human(self, label):
        label.setFont(self.font)
        label.setText("자리 비움")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("color: black;"
                            "background-color: #ff971e;"
                            "border-style: solid;"
                            # "border-width: 5px;"
                            # "border-radius: 3px"
                            )