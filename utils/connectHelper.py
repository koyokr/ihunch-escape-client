from utils.appLayout import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets

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
