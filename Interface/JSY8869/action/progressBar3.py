import time

from PyQt5.QtWidgets import QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


class progressBar3():
    def __init__(self):
        self.pbar1 = QProgressBar()
        self.btn1 = QPushButton('Start')
        self.timer1 = QBasicTimer()
        self.step1 = 0

    def initUI3(self):
        self.pbar1.setGeometry(400, 40, 200, 25)
        self.btn1.move(400, 80)
        self.btn1.clicked.connect(self.onButtonClick3)

    def onButtonClick3(self):
        count = 0
        while count < 100:
            count += 1
            time.sleep(0.1)
            self.pbar3.setValue(count)