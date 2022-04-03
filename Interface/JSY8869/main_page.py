from PyQt5 import QtCore, QtWidgets
import sys
import time

from PyQt5.QtGui import QPalette, QBrush, QImage
from PyQt5.QtWidgets import *
from PyQt5 import uic

import weather

thread_ui = uic.loadUiType("ui/threads.ui")[0]
class PyShine_THREADS_APP(QMainWindow,QWidget, thread_ui):
    def __init__(self):
        self.thread = {}
        super(PyShine_THREADS_APP,self).__init__()
        self.initUi1()
        self.show()



    def initUi1(self):
        self.setupUi(self)
        # 진행도 시작점 0으로 초기화
        self.progressBar.setValue(0)
        self.progressBar_2.setValue(0)

        self.textEdit.setReadOnly(True)

        # 배경 이미지 설정
        palette = QPalette()
        palette.setBrush(10,QBrush(QImage('./image/background.jpg')))
        self.setPalette(palette)

        # button 이미지 설정
        self.pushButton.setStyleSheet('border-image:url(./image/start_button.png);border:0px;')
        self.pushButton_2.setStyleSheet('border-image:url(./image/stop_button.png);border:0px;')
        self.pushButton_3.setStyleSheet('border-image:url(./image/start_button.png);border:0px;')
        self.pushButton_4.setStyleSheet('border-image:url(./image/stop_button.png);border:0px;')

        # 이벤트 설정
        self.pushButton.clicked.connect(self.start_worker_1)
        self.pushButton_2.clicked.connect(self.stop_worker_1)
        self.pushButton_3.clicked.connect(self.start_worker_2)
        self.pushButton_4.clicked.connect(self.stop_worker_2)
        self.weather_button.clicked.connect(self.weather_load)

    def start_worker_1(self):
        self.thread[1] = ThreadClass(parent=None, index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.my_function)
        self.pushButton.setEnabled(False)

    def start_worker_2(self):
        self.thread[2] = ThreadClass(parent=None, index=2)
        self.thread[2].start()
        self.thread[2].any_signal.connect(self.my_function)
        self.pushButton_3.setEnabled(False)

    def stop_worker_1(self):
        try:
            self.thread[1].stop()
            self.pushButton.setEnabled(True)
        except:
            pass

    def stop_worker_2(self):
        try:
            self.thread[2].stop()
            self.pushButton_3.setEnabled(True)
        except:
            pass

    def weather_load(self):
        try:
            self.textEdit.setStyleSheet('font-size:35px;')
            text, weather_data = weather.how_weather()
            self.textEdit.setText(text)
            self.textEdit.setReadOnly(True)
            if weather_data == 0:
                self.weather_button.setStyleSheet('border-image:url(image/rain.png);border:0px;')
            elif weather_data == 1:
                self.weather_button.setStyleSheet('border-image:url(image/rainsnow.png);border:0px;')
            elif weather_data == 2:
                self.weather_button.setStyleSheet('border-image:url(image/snow.png);border:0px;')
            elif weather_data == 3:
                self.weather_button.setStyleSheet('border-image:url(image/shower.png);border:0px;')
            elif weather_data == 4:
                self.weather_button.setStyleSheet('border-image:url(image/sunny.jpg);border:0px;')
        except:
            self.textEdit.setText("날씨 조회 실패 (인터넷 상태나 주소 설정을 확인해주세요.)")

    def my_function(self, counter):

        cnt = counter
        index = self.sender().index
        if index == 1:
            self.progressBar.setValue(cnt)
            if cnt == 100:
                self.pushButton.setEnabled(True)
        if index == 2:
            self.progressBar_2.setValue(cnt)
            if cnt == 100:
                self.pushButton_2.setEnabled(True)



class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.index = index
        self.is_running = True

    def run(self):
        cnt = 0
        while (True):
            cnt += 1
            if cnt == 101:
                return
            time.sleep(0.01)
            self.any_signal.emit(cnt)
    def stop(self):
        self.any_signal.emit(0)
        self.is_running = False
        self.terminate()

app = QtWidgets.QApplication(sys.argv)
mainWindow = PyShine_THREADS_APP()
mainWindow.show()
sys.exit(app.exec_())
