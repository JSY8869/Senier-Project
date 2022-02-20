from PyQt5 import QtCore, QtWidgets
import sys
import time

from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
from PyQt5 import uic
from gtts import gTTS
from playsound import playsound

import weather
import wifi

thread_ui = uic.loadUiType("threads.ui")[0]
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
        self.progressBar_3.setValue(0)

        # 배경 이미지 설정
        palette = QPalette()
        palette.setBrush(10,QBrush(QImage('./image/background.jpg')))
        self.setPalette(palette)

        # button 이미지 설정
        self.pushButton.setStyleSheet('border-image:url(./image/start_button.png);border:0px;')
        self.pushButton_4.setStyleSheet('border-image:url(./image/stop_button.png);border:0px;')
        self.pushButton_2.setStyleSheet('border-image:url(./image/start_button.png);border:0px;')
        self.pushButton_5.setStyleSheet('border-image:url(./image/stop_button.png);border:0px;')
        self.pushButton_3.setStyleSheet('border-image:url(./image/start_button.png);border:0px;')
        self.pushButton_6.setStyleSheet('border-image:url(./image/stop_button.png);border:0px;')

        # 날씨 버튼 이미지 설정
        self.weather_button.setStyleSheet('border-image:url(./image/cute_dog.jpg);border:0px;')
        # 와이파이 버튼 이미지 설정
        self.wifi_button.setStyleSheet('border-image:url(./image/wifi_image.png);border:0px;')

        # 이벤트 설정
        self.pushButton.clicked.connect(self.start_worker_1)
        self.pushButton_2.clicked.connect(self.start_worker_2)
        self.pushButton_3.clicked.connect(self.start_worker_3)
        self.pushButton_4.clicked.connect(self.stop_worker_1)
        self.pushButton_5.clicked.connect(self.stop_worker_2)
        self.pushButton_6.clicked.connect(self.stop_worker_3)
        self.weather_button.clicked.connect(self.weather_load)
        self.wifi_button.clicked.connect(self.wifi_set)

    def start_worker_1(self):
        self.thread[1] = ThreadClass(parent=None, index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.my_function)
        self.pushButton.setEnabled(False)

    def start_worker_2(self):
        self.thread[2] = ThreadClass(parent=None, index=2)
        self.thread[2].start()
        self.thread[2].any_signal.connect(self.my_function)
        self.pushButton_2.setEnabled(False)

    def start_worker_3(self):
        self.thread[3] = ThreadClass(parent=None, index=3)
        self.thread[3].start()
        self.thread[3].any_signal.connect(self.my_function)
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
            self.pushButton_2.setEnabled(True)
        except:
            pass
    def stop_worker_3(self):
        try:
            self.thread[3].stop()
            self.pushButton_3.setEnabled(True)
        except:
            pass
    def weather_load(self):
        self.textEdit.setStyleSheet('font-size:35px;')
        text = weather.how_weather(62,120)
        self.textEdit.setText(text)

        self.speak(text)

    def speak(self, text):
        tts = gTTS(text=text, lang='ko')
        filename = 'voice.mp3'
        tts.save(filename)
        playsound(filename)

    def wifi_set(self):
        self.hide()
        self.second = wifi.set_wifi()
        self.second.exec()
        self.show()


    def my_function(self, counter):

        cnt = counter
        index = self.sender().index
        if index == 1:
            self.progressBar.setValue(cnt)
        if index == 2:
            self.progressBar_2.setValue(cnt)
        if index == 3:
            self.progressBar_3.setValue(cnt)



class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.index = index
        self.is_running = True

    def run(self):
        print('Starting thread...', self.index)
        cnt = 0
        while (True):
            cnt += 1
            if cnt == 101:
                break
            time.sleep(0.01)
            self.any_signal.emit(cnt)
    def stop(self):
        self.any_signal.emit(0)
        self.is_running = False
        print('Stopping thread...', self.index)
        self.terminate()

app = QtWidgets.QApplication(sys.argv)
mainWindow = PyShine_THREADS_APP()
mainWindow.show()
sys.exit(app.exec_())
