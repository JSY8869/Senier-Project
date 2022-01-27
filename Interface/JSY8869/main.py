import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

from action.progressBar import progressBar
from action.set_wifi import set_wifi


class MyApp(QWidget, progressBar, set_wifi):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initd()
        self.initwifi()
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