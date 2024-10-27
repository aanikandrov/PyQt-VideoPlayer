
import cv2
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap

class Class_Video_QLabel(QLabel):
    def __init__(self, path, label, parent=None):
        super(Class_Video_QLabel, self).__init__(parent)
        self.path = path
        self.label = label

        self.capture = cv2.VideoCapture(self.path)

        self.is_end = False
        self.is_paused = True

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

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

                pixmap = QPixmap.fromImage(image).scaled(self.label.size(),
                                                         Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation)
                self.label.setPixmap(pixmap)
            else:
                self.timer.stop()
                self.is_paused = True
                self.is_end = True
                self.capture.release()


    def restart(self):
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Сбросить на начало
        if not self.timer.isActive():
            self.play()

