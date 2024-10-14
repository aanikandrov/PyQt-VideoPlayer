import cv2
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QLabel

class Class_VideoCaptureThread(QThread):
    change_pixmap_signal = pyqtSignal(QImage)

    def __init__(self, label: QLabel, mode=True, path=""):
        super().__init__()
        self.run_flag = False
        self.mode = mode
        self.path = path
        self.label = label
        self.pause = False

    def run(self):
        if (self.mode or self.path == ""):
            cap = cv2.VideoCapture(0)
        else:
            cap = cv2.VideoCapture(self.path)

        while self.run_flag:
            if not self.pause:
                ret, frame = cap.read()
                if ret:
                    h, w, _ = frame.shape
                    width = self.label.width()
                    height = self.label.height()

                    frame_resized = cv2.resize(frame, (width, height))

                    rgb_image = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgb_image.shape
                    bytes_per_line = ch * w
                    convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                    self.change_pixmap_signal.emit(convert_to_Qt_format)
                    cv2.waitKey(30)
                else:
                    self.change_pixmap_signal.emit(QImage())
                    break
        cap.release()

    def start_capture(self):
        self.run_flag = True
        self.pause = False
        self.start()

    def stop_capture(self):
        self.run_flag = False
        self.quit()
        self.wait()

    def toggle_capture(self):
        if not self.run_flag:
            self.run_flag = True
            self.pause = False
            self.start()
        else:
            self.pause = not self.pause

    def pause_capture(self):
        if self.pause:
            self.pause = False
        else:
            self.pause = True

