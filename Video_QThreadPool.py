import cv2

from PyQt5.QtCore import Qt, QRunnable, QObject
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel

class VideoCaptureWorker(QRunnable, QObject):
    def __init__(self, label: QLabel, mode=True, path=""):
        super().__init__()
        self.run_flag = True
        self.mode = mode
        self.path = path
        self.label = label
        self.is_pause = False

    def run(self):
        #cap = cv2.VideoCapture(0 if self.mode else self.path)
        cap = cv2.VideoCapture(0 if self.path == "" else self.path)

        while self.run_flag:
            if not self.is_pause:
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
                    self.is_pause = True
                    break
            else:
                cv2.waitKey(100)

        cap.release()

    def stop_capture(self):
        self.run_flag = False

    def pause(self):
        self.is_pause = not self.is_pause
