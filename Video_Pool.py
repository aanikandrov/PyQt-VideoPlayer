
import cv2
from PyQt5.QtCore import QRunnable
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

class VideoCaptureRunnable(QRunnable):
    def __init__(self, label: QLabel, source: str):
        super().__init__()
        self.label = label
        self.source = source
        self.is_running = True
        self.is_paused = False

    def run(self):
        cap = cv2.VideoCapture(self.source)

        while self.is_running:
            if not self.is_paused:
                ret, frame = cap.read()
                if ret:
                    # Преобразование BGR в RGB
                    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgb_image.shape
                    bytes_per_line = ch * w
                    image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

                    # Обновление QLabel с новым изображением
                    pixmap = QPixmap.fromImage(image).scaled(self.label.size(), Qt.KeepAspectRatio,
                                                             Qt.SmoothTransformation)
                    self.label.setPixmap(pixmap)
                    cv2.waitKey(30)
            else:
                cv2.waitKey(100)

        cap.release()

    def stop(self):
        self.is_running = False
    def pause(self):
        self.is_paused = not self.is_paused


