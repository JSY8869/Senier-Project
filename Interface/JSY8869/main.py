import sys

from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QDialog,
                             QProgressBar, QPushButton)


from action.progressBar1 import Actions, External
from action.progressBar2 import Actions2, External2


class MyApp(QWidget, Actions, External, Actions2, External2):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.initUI1()
        self.initUI2()

        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('image/main_image.png'))
        self.setGeometry(300, 300, 1000, 600)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
