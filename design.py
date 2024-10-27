from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThreadPool, Qt

import Video_QThreadPool
import Video_QLabel
import Video_QGraphics

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 319)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.main_radioLightTheme = QtWidgets.QRadioButton(self.centralwidget)
        # self.main_radioLightTheme.setGeometry(QtCore.QRect(20, 260, 82, 17))
        # self.main_radioLightTheme.setObjectName("main_radioLightTheme")
        # self.main_radioDarkTheme = QtWidgets.QRadioButton(self.centralwidget)
        # self.main_radioDarkTheme.setGeometry(QtCore.QRect(20, 280, 82, 17))
        # self.main_radioDarkTheme.setObjectName("main_radioDarkTheme_2")

        self.main_pushFiles = QtWidgets.QPushButton(self.centralwidget)
        self.main_pushFiles.setGeometry(QtCore.QRect(320, 260, 75, 23))
        self.main_pushFiles.setStyleSheet("border-top: 1px solid rgb(0, 0, 0);\n"
                                          "border-left: 1px solid rgb(0, 0, 0);\n"
                                          "border-right: 1px solid rgb(0, 0, 0);\n"
                                          "border-bottom: 1px solid rgb(0, 0, 0);\n"
                                          "")
        self.main_pushFiles.setObjectName("main_pushFiles")
        self.tabVideo = QtWidgets.QTabWidget(self.centralwidget)
        self.tabVideo.setGeometry(QtCore.QRect(10, 10, 391, 241))
        self.tabVideo.setStyleSheet(" border: 2px solid #C4C4C3;")
        self.tabVideo.setObjectName("tabVideo")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.tab_QLabel = QtWidgets.QWidget()
        self.tab_QLabel.setObjectName("tab_3")
        self.tab_QLabel_label = QtWidgets.QLabel(self.tab_QLabel)
        self.tab_QLabel_label.setGeometry(QtCore.QRect(20, 20, 270, 170))
        self.tab_QLabel_label.setFrameShape(QtWidgets.QFrame.Box)
        self.tab_QLabel_label.setLineWidth(8)
        self.tab_QLabel_label.setText("")
        self.tab_QLabel_label.setObjectName("tab3_label")
        self.tab_QLabel_pushPlay = QtWidgets.QPushButton(self.tab_QLabel)
        self.tab_QLabel_pushPlay.setGeometry(QtCore.QRect(300, 30, 50, 25))
        self.tab_QLabel_pushPlay.setObjectName("tab3_pushPlay")
        self.tab_QLabel_pushRestart = QtWidgets.QPushButton(self.tab_QLabel)
        self.tab_QLabel_pushRestart.setGeometry(QtCore.QRect(300, 60, 50, 25))
        self.tab_QLabel_pushRestart.setObjectName("tab3_pushPause")
        self.tabVideo.addTab(self.tab_QLabel, "")


        self.tab_QGraphicsView = QtWidgets.QWidget()
        self.tab_QGraphicsView.setObjectName("tab_4")
        self.tab_QGraphicsView_graphicsView = QtWidgets.QGraphicsView(self.tab_QGraphicsView)
        self.tab_QGraphicsView_graphicsView.setGeometry(QtCore.QRect(20, 20, 270, 170))
        self.tab_QGraphicsView_graphicsView.setAutoFillBackground(False)
        self.tab_QGraphicsView_graphicsView.setObjectName("tab4_graphicsView")
        self.tab_QGraphicsView_pushPlay = QtWidgets.QPushButton(self.tab_QGraphicsView)
        self.tab_QGraphicsView_pushPlay.setGeometry(QtCore.QRect(300, 30, 50, 25))
        self.tab_QGraphicsView_pushPlay.setObjectName("tab4_pushPlay")
        self.tab_QGraphicsView_pushRestart = QtWidgets.QPushButton(self.tab_QGraphicsView)
        self.tab_QGraphicsView_pushRestart.setGeometry(QtCore.QRect(300, 60, 50, 25))
        self.tab_QGraphicsView_pushRestart.setObjectName("tab4_pushPause")
        self.tabVideo.addTab(self.tab_QGraphicsView, "")

        self.tab_ThreadPool = QtWidgets.QWidget()
        self.tab_ThreadPool.setObjectName("tab_6")
        self.tab_ThreadPool_label = QtWidgets.QLabel(self.tab_ThreadPool)
        self.tab_ThreadPool_label.setGeometry(QtCore.QRect(20, 20, 270, 170))
        self.tab_ThreadPool_label.setText("")
        self.tab_ThreadPool_label.setObjectName("tab6_label")
        self.tab_ThreadPool_pushPlay = QtWidgets.QPushButton(self.tab_ThreadPool)
        self.tab_ThreadPool_pushPlay.setGeometry(QtCore.QRect(300, 30, 50, 25))
        self.tab_ThreadPool_pushPlay.setObjectName("tab6_pushPlay")
        self.tab_ThreadPool_radioCamera = QtWidgets.QRadioButton(self.tab_ThreadPool)
        self.tab_ThreadPool_radioCamera.setGeometry(QtCore.QRect(300, 60, 70, 25))
        self.tab_ThreadPool_radioCamera.setObjectName("tab6_radioCamera")
        self.tab_ThreadPool_radioFile = QtWidgets.QRadioButton(self.tab_ThreadPool)
        self.tab_ThreadPool_radioFile.setGeometry(QtCore.QRect(300, 90, 70, 25))
        self.tab_ThreadPool_radioFile.setObjectName("tab5_radioFile")
        self.tabVideo.addTab(self.tab_ThreadPool, "")
        self.tab_ThreadPool_pushPause = QtWidgets.QPushButton(self.tab_ThreadPool)
        self.tab_ThreadPool_pushPause.setGeometry(QtCore.QRect(300, 120, 50, 25))
        self.tab_ThreadPool_pushPause.setObjectName("tab6_pushPause")


        self.tabVideo.raise_()

        self.main_pushFiles.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabVideo.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.tab_QLabel_pushPlay.setText(_translate("MainWindow", "Play"))
        self.tab_QLabel_pushRestart.setText(_translate("MainWindow", "Restart"))
        self.tabVideo.setTabText(self.tabVideo.indexOf(self.tab_QLabel), _translate("MainWindow", "QLabel"))

        self.tab_QGraphicsView_pushPlay.setText(_translate("MainWindow", "Play"))
        self.tab_QGraphicsView_pushRestart.setText(_translate("MainWindow", "Restart"))
        self.tabVideo.setTabText(self.tabVideo.indexOf(self.tab_QGraphicsView), _translate("MainWindow", "QGraphicsView"))

        self.tab_ThreadPool_pushPlay.setText(_translate("MainWindow", "Play"))
        self.tab_ThreadPool_pushPause.setText(_translate("MainWindow", "Pause"))
        self.tab_ThreadPool_radioCamera.setText(_translate("MainWindow", "Camera"))
        self.tab_ThreadPool_radioFile.setText(_translate("MainWindow", "File"))
        self.tabVideo.setTabText(self.tabVideo.indexOf(self.tab_ThreadPool), _translate("MainWindow", "ThreadPool"))

    # --- --- --- --- --- --- --- --- --- --- --- ---
    # QLabel

    def video_tab_QLabel(self, MainWindow):
        self.path = "D:/Рабочий стол/Метрол ML/vid4.mp4"
        self.video_label = Video_QLabel.Class_Video_QLabel(self.path, self.tab_QLabel_label)
        self.tab_QLabel_pushPlay.clicked.connect(self.video_label.play)
        self.tab_QLabel_pushRestart.clicked.connect(self.video_label.restart)


    # --- --- --- --- --- --- --- --- --- --- --- ---
    # QGraphicsView

    def video_tab_QGraphicsView(self, MainWindow):
        self.path = "D:/Рабочий стол/Метрол ML/vid4.mp4"
        self.tab_QGraphicsView_graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tab_QGraphicsView_graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.video_player = Video_QGraphics.Class_Video_QGraphics(self.path, self.tab_QGraphicsView_graphicsView)
        self.tab_QGraphicsView_pushPlay.clicked.connect(self.video_player.play)
        self.tab_QGraphicsView_pushRestart.clicked.connect(self.video_player.restart)

    # --- --- --- --- --- --- --- --- --- --- --- ---
    # QThreadPool

    def video_tab_ThreadPool(self, MainWindow):

        self.tab_ThreadPool_pushPause.clicked.connect(self.pause_video)
        self.tab_ThreadPool_radioCamera.clicked.connect(self.tab6_changeMode)
        self.tab_ThreadPool_radioFile.clicked.connect(self.tab6_changeMode)

        self.path = "D:/Рабочий стол/Метрол ML/vid4.mp4"
        self.thread_pool = QThreadPool()

        self.webcam_runnable = Video_QThreadPool.VideoCaptureWorker(self.tab_ThreadPool_label,
                                                                    mode=True,
                                                                    path=0)
        self.file_runnable = Video_QThreadPool.VideoCaptureWorker(self.tab_ThreadPool_label,
                                                                   path=self.path,
                                                                   mode=False)




    def start_webcam(self):

        self.stop_file_video()
        self.stop_webcam()
        self.webcam_runnable = Video_QThreadPool.VideoCaptureWorker(self.tab_ThreadPool_label,
                                                                    mode=True,
                                                                    path=0)
        self.thread_pool.start(self.webcam_runnable)



    def stop_webcam(self):
        if self.webcam_runnable is not None:
            self.webcam_runnable.stop_capture()
        self.tab_ThreadPool_label.clear()

    def start_file_video(self):
        self.stop_file_video()
        self.stop_webcam()
        self.file_runnable = Video_QThreadPool.VideoCaptureWorker(self.tab_ThreadPool_label,
                                                           path=self.path, mode=False)
        self.thread_pool.start(self.file_runnable)

    def stop_file_video(self):
        if self.file_runnable is not None:
            self.file_runnable.stop_capture()
        self.tab_ThreadPool_label.clear()

    def pause_video(self):
        if self.webcam_runnable is not None:
            self.webcam_runnable.pause()
        if self.file_runnable is not None:
            self.file_runnable.pause()

    def tab6_changeMode(self):
        if self.tab_ThreadPool_radioCamera.isChecked():
            self.tab_ThreadPool_pushPlay.clicked.connect(self.start_webcam)
        elif self.tab_ThreadPool_radioFile.isChecked():
            self.tab_ThreadPool_pushPlay.clicked.connect(self.start_file_video)

    # --- --- --- --- --- --- --- --- --- --- --- ---

