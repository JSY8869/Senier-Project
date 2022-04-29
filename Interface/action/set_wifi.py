import sys
from PyQt5.QtWidgets import (QPushButton, QLineEdit, QInputDialog)


class set_wifi_name():

    def wifi_name(self):
        self.btn = QPushButton('입력하기', self)
        self.btn.move(200, 200)
        self.btn.clicked.connect(self.showDialog_name)

        self.le = QLineEdit(self)
        self.le.move(160, 170)

    def showDialog_name(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your wifi-name:')

        if ok:
            self.le.setText(str(text))

class set_wifi_password():
    def showDialog_password(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your wifi-password:')

        if ok:
            self.le2.setText(str(text))

    def wifi_password(self):
        self.btn2 = QPushButton('입력하기', self)
        self.btn2.move(400, 200)
        self.btn2.clicked.connect(self.showDialog_password)

        self.le2 = QLineEdit(self)
        self.le2.move(360, 170)