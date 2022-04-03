import time

from PyQt5 import QtCore


class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.index = index
        self.is_running = True

    def run(self):
        cnt = 0
        while (True):
            cnt += 1
            if cnt == 101:
                return
            time.sleep(0.01)
            self.any_signal.emit(cnt)

    def stop(self):
        self.any_signal.emit(0)
        self.is_running = False
        self.terminate()