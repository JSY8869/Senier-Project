import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)

TIME_LIMIT = 100


class External2(QThread):
    """
    Runs a counter thread.
    """
    countChanged2 = pyqtSignal(int)

    def run(self):
        count = 0
        while count < TIME_LIMIT:
            count += 1
            time.sleep(1)
            self.countChanged2.emit(count)


class Actions2():
    """
    Simple dialog that consists of a Progress Bar and a Button.
    Clicking on the button results in the start of a timer and
    updates the progress bar.
    """

    def initUI2(self):
        self.progress2 = QProgressBar(self)
        self.progress2.setGeometry(200, 200, 300, 25)
        self.progress2.setMaximum(100)
        self.button2 = QPushButton('Start', self)
        self.button2.move(200, 250)

        self.button2.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        self.calc2 = External2()
        self.calc2.countChanged2.connect(self.onCountChanged)
        self.calc2.start()

    def onCountChanged(self, value):
        self.progress2.setValue(value)