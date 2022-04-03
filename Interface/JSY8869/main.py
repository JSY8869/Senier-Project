import sys

from PyQt5 import QtWidgets

import main_page

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = main_page.PyShine_THREADS_APP()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()