import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from design_lobby import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_lobbyButton.clicked.connect(self.run_timer)

    def run_timer(self):
        work_min, break_min = self.min_of_work_lineEdit.text(), self.min_of_work_lineEdit.text()
        if work_min or break_min:
            pass
        else:
            print(123)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
