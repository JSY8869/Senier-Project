from PyQt5.QtGui import QPalette, QBrush, QImage, QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore

import weather, serial
from ThreadClass import ThreadClass

thread_ui = uic.loadUiType("ui/usan.ui")[0]

progress_bar_design = ("QProgressBar{\n"
                                       "    background-color: rgb(98, 114, 164);\n"
                                       "    color:rgb(200,200,200);\n"
                                       "    border-style: none;\n"
                                       "    border-bottom-right-radius: 10px;\n"
                                       "    border-bottom-left-radius: 10px;\n"
                                       "    border-top-right-radius: 10px;\n"
                                       "    border-top-left-radius: 10px;\n"
                                       "    text-align: center;\n"
                                       "    font-size:25px;\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "    border-bottom-right-radius: 10px;\n"
                                       "    border-bottom-left-radius: 10px;\n"
                                       "    border-top-right-radius: 10px;\n"
                                       "    border-top-left-radius: 10px;\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
                                       "}\n"
                                       "\n"
                                       "")
class usan_main(QMainWindow, QWidget, thread_ui):
    def __init__(self):
        super(usan_main, self).__init__()
        self.thread = {}
        self.setupUi(self)


        self.usan_fan = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.usan_fan2 = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
        self.shoe_fan = serial.Serial('/dev/ttyACM2', 9600, timeout=1)
        self.motor = serial.Serial('/dev/ttyACM3', 9600, timeout=1)
        self.usan_fan.flush()
        self.usan_fan2.flush()
        self.shoe_fan.flush()
        self.motor.flush()

        self.setWindowTitle("U.S.A.N")
        self.setWindowIcon(QIcon("./image/main.png"))


        # 진행도 시작점 0으로 초기화
        self.progressBar.setValue(0)
        self.progressBar_2.setValue(0)
        self.progressBar.setStyleSheet(progress_bar_design)
        self.progressBar_2.setStyleSheet(progress_bar_design)

        # 배경 이미지 설정
        palette = QPalette()
        palette.setBrush(10,QBrush(QImage('./image/background.jpg')))
        self.setPalette(palette)

        # button 이미지 설정
        self.pushButton.setStyleSheet('border-image:url(./image/start_button.png);border:0px;')
        self.pushButton_2.setStyleSheet('border-image:url(./image/stop_button.png);border:0px;')
        self.pushButton_3.setStyleSheet('border-image:url(./image/start_button.png);border:0px;')
        self.pushButton_4.setStyleSheet('border-image:url(./image/stop_button.png);border:0px;')
        self.weather_button.setStyleSheet('border-image:url(./image/weather.png);border:0px;')

        # 이벤트 설정
        self.pushButton.clicked.connect(self.start_worker_1)
        self.pushButton_2.clicked.connect(self.stop_worker_1)
        self.pushButton_3.clicked.connect(self.start_worker_2)
        self.pushButton_4.clicked.connect(self.stop_worker_2)
        self.weather_button.clicked.connect(self.weather_load)


        self.textEdit.setStyleSheet('font-size:35px;'
                                    'color:#ffffff;'
                                    'background-color: rgb(68, 84, 107);'
                                    'border-color: rgb(68, 84, 107);')
        self.textEdit.setReadOnly(True)

    def start_worker_1(self):
        self.thread[1] = ThreadClass(index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.progress_bar_count)
        self.pushButton.setEnabled(False)

    def start_worker_2(self):
        self.thread[2] = ThreadClass(index=2)
        self.thread[2].start()
        self.thread[2].any_signal.connect(self.progress_bar_count)
        self.pushButton_3.setEnabled(False)

    def stop_worker_1(self):
        self.thread[1].stop()
        self.pushButton.setEnabled(True)

    def stop_worker_2(self):
        self.thread[2].stop()
        self.pushButton_3.setEnabled(True)

    def weather_load(self):
        try:
            text, weather_data = weather.how_weather()
            self.textEdit.setText(text)
            if weather_data == 0:
                self.weather_button.setStyleSheet('border-image:url(image/rain.png);border:0px;')
            elif weather_data == 1:
                self.weather_button.setStyleSheet('border-image:url(image/rainsnow.png);border:0px;')
            elif weather_data == 2:
                self.weather_button.setStyleSheet('border-image:url(image/snow.png);border:0px;')
            elif weather_data == 3:
                self.weather_button.setStyleSheet('border-image:url(image/shower.png);border:0px;')
            elif weather_data == 4:
                self.weather_button.setStyleSheet('border-image:url(image/sunny.png);border:0px;')
        except:
            self.textEdit.setText("날씨 조회 실패 (인터넷 상태나 주소 설정을 확인해주세요.)")

    def progress_bar_count(self, counter):
        cnt = counter
        index = self.sender().index
        if index == 1:
            self.usan_fan.write('1'.encode())
            self.usan_fan_2.write('1'.encode())
            self.motor.write('1'.encode())
            self.progressBar.setValue(cnt)
            if cnt == 100:
                self.pushButton.setEnabled(True)
                self.thread[1].is_running = False
        if index == 2:
            self.shoe_fan.write('1'.encode())
            self.progressBar_2.setValue(cnt)
            if cnt == 100:
                self.pushButton_3.setEnabled(True)
                self.thread[2].is_running = False
