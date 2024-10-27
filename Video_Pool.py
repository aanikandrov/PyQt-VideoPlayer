import sys
import cv2
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThreadPool, Qt, QRunnable, pyqtSignal, QObject
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget)


class VideoCaptureWorker(QRunnable, QObject):
    # change_pixmap_signal = pyqtSignal(QImage)

    def __init__(self, label: QLabel, mode=True, path=""):
        super().__init__()
        self.run_flag = True
        self.mode = mode
        self.path = path
        self.label = label
        self.pause = False

    def run(self):

        cap = cv2.VideoCapture(0 if self.mode else self.path)

        while self.run_flag:
            if not self.pause:
                ret, frame = cap.read()
                if ret:
                    h, w, _ = frame.shape
                    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    image = QImage(rgb_image.data, w, h, rgb_image.strides[0], QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(image).scaled(self.label.size(), Qt.KeepAspectRatio,
                                                             Qt.SmoothTransformation)
                    self.label.setPixmap(pixmap)
                    cv2.waitKey(30)  # Примерно 30 FPS
                else:
                    # Если видео закончилось
                    self.change_pixmap_signal.emit(QImage())
                    break

        cap.release()

    def start_capture(self):
        self.run_flag = True
        self.pause = False

    def stop_capture(self):
        self.run_flag = False

    def toggle_pause(self):
        self.pause = not self.pause


class VideoCaptureRunnable(QRunnable):
    def __init__(self, worker: VideoCaptureWorker):
        super().__init__()
        self.worker = worker

    def run(self):
        self.worker.run()