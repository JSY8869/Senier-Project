import time

from PyQt5.QtWidgets import QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


class progressBar5():


    def initUI5(self):
        self.pbar5 = QProgressBar(self)
        self.pbar5.setGeometry(700, 40, 200, 25)

        self.btn5 = QPushButton('Start', self)
        self.btn5.move(700, 80)
        self.btn5.clicked.connect(self.onButtonClick5)

        self.timer5 = QBasicTimer()
        self.step5 = 0

    def onButtonClick5(self):
        count = 0
        while count < 100:
            count += 1
            time.sleep(0.1)
            self.pbar5.setValue(count)