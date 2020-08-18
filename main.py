import json
import sys
import traceback
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Union

import requests
from filelock import FileLock
from PyQt5 import uic
from PyQt5.QtCore import (QBuffer, QObject, QRect, QRunnable, Qt, QThreadPool,
                          QTimer, pyqtSignal, pyqtSlot)
from PyQt5.QtGui import QFont, QImage, QPixmap
from PyQt5.QtMultimedia import QCamera, QCameraImageCapture, QCameraInfo
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtWidgets import QApplication, QLabel

API_HOST = 'api.ihunch.koyo.io'
DATETIME_FORMAT = '%Y%m%d-%H%M%S'

BASE_DIR = Path(__file__).resolve(strict=True).parent
DATA_DIR = BASE_DIR / 'data'
PHOTOS_DIR = BASE_DIR / 'photos'

RecordType = Dict[str, Union[str, bool, float]]
SettingsType = Dict[str, Union[bool, int]]

Form, Window = uic.loadUiType('dialog.ui')


def qimage_to_bytes(qimg: QImage) -> bytes:
    buffer = QBuffer()
    buffer.open(QBuffer.ReadWrite)
    try:
        qimg.save(buffer, 'jpg')
        return bytes(buffer.data())
    finally:
        buffer.close()


def upload_image_api(bimg: bytes, *, s: requests.Session = requests.session()) -> requests.Response:
    return s.post(f'http://{API_HOST}/upload', files={'file': bimg})


def upload_image_save_record(qimg: QImage) -> RecordType:
    bimg = qimage_to_bytes(qimg)
    r = upload_image_api(bimg)

    timestamp = datetime.now().strftime(DATETIME_FORMAT)
    photo = PHOTOS_DIR / f'{timestamp}.jpg'
    with photo.open('wb') as f:
        f.write(bimg)

    success = r.status_code == requests.codes.ok
    record = RecordsDriver.create(timestamp, success, False, 0.0)
    if success:
        j = r.json()
        record['human'] = j['human']
        record['ihunch'] = j['pred']
    RecordsDriver.append(record)
    return record


def get_status_font() -> QFont:
    font = QFont()
    font.setFamily('나눔바른고딕')
    font.setPointSize(50)
    font.setBold(True)
    font.setWeight(50)
    return font


class RecordsDriver:
    _file = DATA_DIR / 'records.json'
    _lock = FileLock(_file.parent / f'{_file.name}.lock')

    @classmethod
    def _load(cls) -> List[RecordType]:
        try:
            records = json.load(cls._file.open('r'))
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            records = []
        return records

    @classmethod
    def _save(cls, records: List[RecordType]) -> None:
        json.dump(records, cls._file.open('w'))

    @classmethod
    def load(cls, beg: str='', end: str='') -> List[RecordType]:
        with cls._lock:
            records = cls._load()
        if not beg and not end:
            pass
        elif not beg:
            records = [x for x in records if x['timestamp'] < end]
        elif not end:
            records = [x for x in records if beg < x['timestamp']]
        else:
            records = [x for x in records if beg < x['timestamp'] < end]
        return records

    @classmethod
    def append(cls, record: RecordType) -> None:
        with cls._lock:
            records = cls._load()
            records.append(record)
            cls._save(records)

    @staticmethod
    def create(timestamp: str, success: bool, human: bool, ihunch: float) -> RecordType:
        return {'timestamp': timestamp, 'success': success, 'human': human, 'ihunch': ihunch}


class SettingsDriver:
    _file = DATA_DIR / 'settings.json'
    _lock = FileLock(_file.parent / f'{_file.name}.lock')

    @staticmethod
    def _initialized() -> SettingsType:
        return {'warn': True, 'stat': True, 'record': True, 'stat_cycle': 0, 'record_cycle': 0}

    @classmethod
    def _load(cls) -> SettingsType:
        try:
            settings = json.load(cls._file.open('r'))
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            settings = cls._initialized()
        return settings

    @classmethod
    def _save(cls, settings: SettingsType) -> None:
        json.dump(settings, cls._file.open('w'))

    @classmethod
    def load(cls) -> SettingsType:
        with cls._lock:
            return cls._load()

    @classmethod
    def save(cls, settings: SettingsType) -> None:
        with cls._lock:
            cls._save(settings)

    @classmethod
    def init(cls) -> SettingsType:
        with cls._lock:
            settings = cls._initialized()
            cls._save(settings)
            return settings


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self) -> None:
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class MyWindow(Window, Form):
    __slots__ = [
        'cameraViewfinder',
        'available_cameras',
        'camera',
        'capture',
        'timer',
        'threadpool',
        'pixmap',
        'photo_timestamp'
    ]

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # viewfinder
        self.cameraViewfinder = QCameraViewfinder(self.cameraWidget)
        self.cameraViewfinder.setGeometry(QRect(0, 73, 641, 481))
        self.cameraViewfinder.setObjectName('cameraViewfinder')
        # available_cameras, camera, capture
        self.available_cameras = QCameraInfo.availableCameras()
        self.camera = self.setup_camera(self.available_cameras, 0) if self.available_cameras else None
        self.capture = self.setup_capture(self.camera) if self.camera else None
        if self.camera is not None:
            self.camera.start()

        # timer, threadpool, pixmap
        self.timer = self.setup_timer()
        self.threadpool = QThreadPool()
        self.pixmap = QPixmap()
        self.photo_timestamp = None

        # connect cameraButton
        self.cameraButton.toggled.connect(lambda toggle: self.cameraButton.setText('정지' if toggle else '시작'))
        self.cameraButton.toggled.connect(lambda toggle: self.start_timer_with_check() if toggle else self.stop_timer())
        # connect photoLeftButton, photoRightButton
        self.tabWidget.tabBarClicked.connect(lambda index: self.load_photo_display_status(init=True) if index == 2 else None)
        self.photoLeftButton.clicked.connect(lambda: self.load_photo_display_status(left=True))
        self.photoRightButton.clicked.connect(lambda: self.load_photo_display_status(right=True))

    def setup_camera(self, cameras: list, i: int) -> QCamera:
        camera = QCamera(cameras[i])
        camera.setViewfinder(self.cameraViewfinder)
        camera.setCaptureMode(QCamera.CaptureStillImage)
        camera.error.connect(self.error_camera_or_capture)
        return camera

    def setup_capture(self, camera: QCamera) -> QCameraImageCapture:
        capture = QCameraImageCapture(camera)
        capture.setCaptureDestination(QCameraImageCapture.CaptureToBuffer)
        capture.imageCaptured.connect(self.upload_image_display_status_async)
        capture.error.connect(self.error_camera_or_capture)
        return capture

    def setup_timer(self) -> QTimer:
        timer = QTimer()
        timer.setInterval(5_000)
        timer.timeout.connect(self.capture_with_check)
        return timer

    def resetup_camera_capture(self) -> bool:
        self.available_cameras = QCameraInfo.availableCameras()
        if not self.available_cameras:
            return False
        self.camera = self.setup_camera(self.available_cameras, 0)
        self.camera.start()
        self.capture = self.setup_capture(self.camera)
        return True

    def check_and_repair_capture(self) -> bool:
        if self.camera is None and not self.resetup_camera_capture():
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
        if self.timer.isActive():
            self.timer.stop()

    def capture_with_check(self) -> None:
        if self.check_and_repair_capture():
            self.capture.capture()
        else:
            self.cameraButton.setChecked(False)

    def upload_image_display_status_async(self, id: int, qimg: QImage) -> None:
        def display_result(record: RecordType) -> None:
            if record['success']:
                self.display_status(self.cameraStatusBar, record['human'], record['ihunch'])
        worker = Worker(upload_image_save_record, qimg)
        worker.signals.result.connect(display_result)
        self.threadpool.start(worker)

    def error_camera_or_capture(self, *args) -> None:
        self.cameraButton.setChecked(False)

    def load_photo_display_status(self, *, init=False, left=False, right=False) -> None:
        if init:
            beg, end = None, None
            index = -1
        elif left:
            beg, end = None, self.photo_timestamp
            index = -1
        elif right:
            beg, end = self.photo_timestamp, None
            index = 0
        else:
            raise Exception('load_photo_display_status: init, left, right are False')
        records = RecordsDriver.load(beg, end)
        if not records:
            return
        record = records[index]
        self.photo_timestamp = record['timestamp']
        self.pixmap.load(str(PHOTOS_DIR / f'{self.photo_timestamp}.jpg'))
        self.photoImage.setPixmap(self.pixmap)
        self.display_status(self.photoStatusBar, record['human'], record['ihunch'])

    # def load_stat_async(self, index) -> None:
    #     def fn(r) -> None:
    #         pass
    #     worker = Worker(upload_image_save_record, index)
    #     worker.signals.result.connect(fn)
    #     self.threadpool.start(worker)

    def init_setting(self):
        self.settingWarnButton.setChecked(True)
        self.settingStatButton.setChecked(True)
        self.settingStatCycle.setCurrentIndex(0)
        self.settingRecordButton.setChecked(True)
        self.settingRecordCycle.setCurrentIndex(0)

    @staticmethod
    def display_status(statusbar: QLabel, human: bool, ihunch: float):
        if human:
            if ihunch > 0.5:
                text, color = '거북목', 'FF0000'
            else:
                text, color = '정상', '23F200'
            text += f' ({ihunch:.4f})'
        else:
            text, color = '자리비움', 'FF971E'
        statusbar.setFont(get_status_font())
        statusbar.setText(text)
        statusbar.setAlignment(Qt.AlignCenter)
        statusbar.setStyleSheet(f'color: #{color}; border-style: solid;')


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
