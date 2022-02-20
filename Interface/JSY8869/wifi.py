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
        try:
            File = open("test.txt", "r")
            Wifi = File.readlines()
            self.wifi_name.setPlainText(Wifi[0].strip())
            self.wifi_password.setPlainText(Wifi[1])
        except:
            pass
        self.save_button.clicked.connect(self.save_wifi)
        self.home_button.clicked.connect(self.Home)

    def Home(self):
        self.close()

    def save_wifi(self):
        self.wifi_id = self.wifi_name.toPlainText()
        self.wifi_pass = self.wifi_password.toPlainText()
        File = open("test.txt", "w")
        File.write(self.wifi_id +"\n"+ self.wifi_pass)
        self.close()
