import sys
import time

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from design_lobby import Ui_DesignLobby
from design_timer import Ui_DesignTimer

minutes_of_work = 10
minutes_of_break = 10


class mMainClass(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked)
        self.window_lobby = LobbyWindow(self)
        self.window_timer = TimerWindow(self)
        self.stacked.addWidget(self.window_lobby)
        self.stacked.addWidget(self.window_timer)

        self.stacked.setCurrentIndex(0)

    def go_lobby(self):
        self.stacked.setCurrentIndex(0)

    def go_timer(self):
        self.stacked.setCurrentIndex(1)


class TimerWindow(QtWidgets.QMainWindow, Ui_DesignTimer):
    def __init__(self, parent=None):
        global minutes_of_work
        super(TimerWindow, self).__init__(parent)
        self.setupUi(self)
        self.work_is = True
        self.startButton.clicked.connect(self.play_timer)
        self.minute_label.setText(str(minutes_of_work))

    def play_timer(self):
        time_of_timer = None
        if self.work_is:
            time_of_timer = minutes_of_work * 60
            while time_of_timer > -1:
                self.minute_label.setText(str(time_of_timer // 60))
                self.second_label.setText(str(time_of_timer % 60))
                time.sleep(1)
                time_of_timer -= 1


class LobbyWindow(QtWidgets.QMainWindow, Ui_DesignLobby):
    def __init__(self, parent=None):
        super(LobbyWindow, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.start_lobbyButton.clicked.connect(self.run_timer)

    def run_timer(self):
        global minutes_of_work, minutes_of_break
        work_min, break_min = self.min_of_work_lineEdit.text(), self.min_of_break_lineEdit.text()
        if work_min and break_min:
            minutes_of_work, minutes_of_break = int(work_min), int(break_min)
            self.parent.go_timer()
        else:
            print(123)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = mMainClass()
    ex.resize(758, 600)
    ex.show()
    sys.exit(app.exec_())
