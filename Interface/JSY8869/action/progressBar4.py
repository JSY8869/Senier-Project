import time

from PyQt5.QtWidgets import QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


class progressBar4():


    def initUI4(self):
        self.pbar4 = QProgressBar(self)
        self.pbar4.setGeometry(550, 40, 200, 25)

        self.btn4 = QPushButton('Start', self)
        self.btn4.move(550, 80)
        self.btn4.clicked.connect(self.onButtonClick4)

        self.timer4 = QBasicTimer()
        self.step4 = 0

    def onButtonClick4(self):
        count = 0
        while count < 100:
            count += 1
            time.sleep(0.1)
            self.pbar4.setValue(count)