import sys

import cv2
import requests
from PyQt5 import uic
from PyQt5.QtCore import (QBuffer, QEvent, QObject, QRect, QRunnable, Qt,
                          QThreadPool, QTimer, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtMultimedia import QCamera, QCameraImageCapture, QCameraInfo
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType('dialog.ui')


def clickable(widget):
    """탭바 클릭 이벤트 부여"""
    class Filter(QObject):
        clicked = pyqtSignal()  # pyside2 사용자는 pyqtSignal() -> Signal()로 변경

        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
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
    convert_to_Qt_format = QImage(rgb_image.data, width, heigth, bytes_per_line, QImage.Format_RGB888)
    p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
    return QPixmap.fromImage(p)


def upload_image_api(img_bytes: bytes, *, s: requests.Session = requests.session()) -> requests.Response:
    url = 'http://api.ihunch.koyo.io/upload'
    files = {'file': img_bytes}
    return s.post(url, files=files)


def qimage_to_bytes(qimg: QImage) -> bytes:
    buffer = QBuffer()
    buffer.open(QBuffer.ReadWrite)
    try:
        qimg.save(buffer, 'jpg')
        return bytes(buffer.data())
    finally:
        buffer.close()


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.fn(*self.args, **self.kwargs)


class WorkerSignals(QObject):
    pass


class MyWindow(Window, Form):
    __slots__ = [
        # camera
        'cameraViewfinder',
        'available_cameras',
        'camera',
        'capture',
        'timer',
        'threadpool'
    ]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.cameraButton.clicked.connect(test)

        # viewfinder
        self.cameraViewfinder = QCameraViewfinder(self.cameraWidget)
        self.cameraViewfinder.setGeometry(QRect(20, 110, 641, 481))
        self.cameraViewfinder.setObjectName('cameraViewfinder')

        # camera, capture, timer
        self.available_cameras = QCameraInfo.availableCameras()
        self.camera = self.setup_camera(
            self.available_cameras, 0) if self.available_cameras else None
        self.capture = self.setup_capture(self.camera) if self.camera else None
        self.timer = self.setup_timer(self.capture) if self.capture else None
        if self.camera is not None:
            self.camera.start()

        # threadpool
        self.threadpool = QThreadPool()

        # connect other widgets
        self.cameraButton.toggled.connect(
            lambda toggle: self.cameraButton.setText('정지' if toggle else '시작'))
        self.cameraButton.toggled.connect(
            lambda toggle: self.start_timer_with_check() if toggle else self.stop_timer())

    def setup_camera(self, cameras: list, i: int) -> QCamera:
        camera = QCamera(cameras[i])
        camera.setViewfinder(self.cameraViewfinder)
        camera.setCaptureMode(QCamera.CaptureStillImage)
        camera.error.connect(self.handle_error_camera_capture)
        return camera

    def setup_capture(self, camera: QCamera) -> QCameraImageCapture:
        capture = QCameraImageCapture(camera)
        capture.setCaptureDestination(QCameraImageCapture.CaptureToBuffer)
        capture.imageCaptured.connect(self.upload_image_async)
        capture.error.connect(self.handle_error_camera_capture)
        return capture

    def setup_timer(self, capture: QCameraImageCapture) -> QTimer:
        timer = QTimer()
        timer.setInterval(4_000)
        timer.timeout.connect(self.capture_with_check)
        return timer

    def resetup_camera_capture_timer(self) -> bool:
        self.available_cameras = QCameraInfo.availableCameras()
        if not self.available_cameras:
            return False
        self.camera = self.setup_camera(self.available_cameras, 0)
        self.camera.start()
        self.capture = self.setup_capture(self.camera)
        self.timer = self.setup_timer(self.timer)
        return True

    def check_and_repair_capture(self) -> bool:
        if self.camera is None and not self.resetup_camera_capture_timer():
            return False
        if not self.capture.isReadyForCapture():
            if not self.camera.isAvailable():
                return False
            self.camera.start()
        return True

    def start_timer_with_check(self) -> None:
        if self.check_and_repair_capture():
            self.timer.start()
        else:
            self.cameraButton.setChecked(False)

    def stop_timer(self) -> None:
        if self.timer is not None and self.timer.isActive():
            self.timer.stop()

    def capture_with_check(self) -> None:
        if self.check_and_repair_capture():
            self.capture.capture()
        else:
            self.cameraButton.setChecked(False)

    def upload_image_async(self, id: int, qimg: QImage) -> None:
        def upload_image(qimg):
            # timestamp = datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
            img_bytes = qimage_to_bytes(qimg)
            r = upload_image_api(img_bytes)
            print(r.status_code, r.text)
        worker = Worker(upload_image, qimg)
        self.threadpool.start(worker)

    def handle_error_camera_capture(self, *args) -> None:
        self.cameraButton.setChecked(False)


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = app_layout.Ui_MainWindow()
    status = ihunch_warning.IhunchWarn()

    ui.setupUi(MainWindow)

    cam_thread = my_cam.VideoThread()
    cam_thread.VIDEO_SIGNAL.connect(update_image)
    ui.video_button.toggled.connect(cam_thread.stop_start)
    ui.video_button.toggled.connect(ui.video_on_off)
    cam_thread.start()

    status = ihunch_warning.IhunchWarn()
    status.status_ihunch(ui.status_bar_1)
    status.status_normal(ui.status_bar_2)
    status.status_no_human(ui.status_bar_3)
    status.status_ihunch(ui.status_bar_4)

    # 초기 설정값 저장
    ui.apply_current_setting()
    # 저장되지 않은 설정 변경 값 삭제
    clickable(ui.tab_widget.tabBar()).connect(ui.return_current_setting)

    # ui.set_reset_button.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(ui.apply_current_setting)
    # ui.set_reset_button.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(ui.return_initial_setting) #reset 버튼 누를 시 설정 초기화

    MainWindow.show()
    sys.exit(app.exec_())
