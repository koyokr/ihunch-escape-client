import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class IhunchWarn():

    def status_ihunch(self, label):
        label.setText("거북목")
        # label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("color: black;"
                            "background-color: #FF0000;"
                            "border-style: #FF0000;"
                            "border-style: solid;"
                            "border-width: 2px;"
                            "border-radius: 3px"
                            )

    def status_normal(self, label):
        label.setText("정상")
        # label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("color: black;"
                            "background-color: #FF0000;"
                            "border-style: #FF0000;"
                            "border-style: solid;"
                            "border-width: 2px;"
                            "border-radius: 3px"
                            )

    def status_no_human(self, label):
        label.setText("No Human")
        # label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet("color: black;"
                            "background-color: #FF0000;"
                            "border-style: #FF0000;"
                            "border-style: solid;"
                            "border-width: 2px;"
                            "border-radius: 3px"
                            )