from PyQt5.QtWidgets import *
from PyQt5 import uic

form_set_wifi = uic.loadUiType("wifi_ui.ui")[0]
class set_wifi(QDialog,QWidget,form_set_wifi):
    def __init__(self):
        super(set_wifi,self).__init__()
        self.initUi2()
        self.show()
    def initUi2(self):
        self.setupUi(self)
        self.save_button.clicked.connect(self.save_wifi)
        self.home_button.clicked.connect(self.Home)
    def Home(self):
        self.close()
    def save_wifi(self):
        self.wifi_id = self.wifi_name.toPlainText()
        self.wifi_pass = self.wifi_password.toPlainText()
        print(self.wifi_id, self.wifi_pass)

if __name__ == '__main__':
    a = set_wifi()