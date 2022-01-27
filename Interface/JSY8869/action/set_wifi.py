import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog)


class set_wifi():

    def initwifi(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(200, 200)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(160, 170)

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))
            print(text)