import sys
from PyQt5 import QtWidgets
import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        # функционал
        self.video_tab_QLabel(self)
        self.video_tab_QGraphicsView(self)
        self.video_tab_ThreadPool(self)

    def closeEvent(self, event):
        self.video_label.clear()
        self.stop_webcam()
        self.stop_file()
        event.accept()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()