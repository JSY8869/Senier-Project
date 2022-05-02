import time

from PyQt5 import QtCore


class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(int)

    def __init__(self, index):
        super(ThreadClass, self).__init__()
        self.index = index
        self.is_running = True

    def run(self):
        cnt = 0
        while True:
            cnt += 0.1
            if cnt == 101:
                return
            time.sleep(0.01)
            self.any_signal.emit(cnt)

    def stop(self):
        self.is_running = False
        self.terminate()
