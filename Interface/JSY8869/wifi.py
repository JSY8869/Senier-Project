from PyQt5.QtWidgets import QPushButton, QInputDialog, QLineEdit


class set_wifi():
    def __init__(self):
        self.le = QLineEdit(self)
        self.le2 = QLineEdit(self)

    def initwifiName(self):
        self.btn1 = QPushButton('wifi name 입력', self)
        self.btn1.move(10, 600)

        self.le.move(10, 570)
        self.btn1.clicked.connect(self.showDialogName())


    def showDialogName(self):
        text, ok = QInputDialog.getText(self, '와이파이 이름', 'Enter your wifi name: ')

        if ok:
            self.le.setText(str(text))
            print(text)


    def initwifiPassword(self):
        self.btn2 = QPushButton('wifi password 입력', self)
        self.btn2.move(50, 600)

        self.le2.move(50, 570)
        self.btn2.clicked.connect(self.showDialogPassword())


    def showDialogPassword(self):
        text, ok = QInputDialog.getText(self, '와이파이 비밀번호', 'Enter your wifi password: ')

        if ok:
            self.le2.set