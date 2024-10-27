
import cv2
from PyQt5.QtWidgets import (QGraphicsScene)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem

class Class_Video_QGraphics:
    def __init__(self, path, graphics_view):
        self.path = path
        self.graphicsView = graphics_view

        self.capture = cv2.VideoCapture(self.path)

        self.is_end = False
        self.is_paused = True

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        self.pixmap_item = QGraphicsPixmapItem()
        scene = self.graphicsView.scene() or QGraphicsScene()
        scene.addItem(self.pixmap_item)
        self.graphicsView.setScene(scene)

    def play(self):
        if self.is_end:
            self.restart()
        elif not self.timer.isActive():
            self.is_paused = False
            self.timer.start(30)
        else:
            self.is_paused = True
            self.timer.stop()

    def update_frame(self):
        if not self.is_paused and self.capture is not None:
            ret, frame = self.capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                height, width, channel = frame.shape
                image = QImage(frame.data, width, height,
                               width * channel, QImage.Format_RGB888)

                pixmap = QPixmap.fromImage(image).scaled(self.graphicsView.size(),
                                                           Qt.KeepAspectRatio,
                                                           Qt.SmoothTransformation)
                scaled_pixmap = pixmap.scaled(self.graphicsView.size(),
                                                Qt.KeepAspectRatio,
                                                Qt.SmoothTransformation)
                self.pixmap_item.setPixmap(scaled_pixmap)
            else:
                self.capture.release()
                self.capture = None
                self.timer.stop()
                self.is_paused = True
                self.is_end = True

    def restart(self):
        if self.capture is not None:
            self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Сбросить на начало
            if not self.timer.isActive():
                self.play()
