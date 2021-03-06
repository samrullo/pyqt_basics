from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome Main Window")

        checkbox = QCheckBox()
        checkbox.setCheckState(Qt.Checked)
        checkbox.stateChanged.connect(self.show_state)

        self.setCentralWidget(checkbox)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)


app = QApplication(sys.argv)
window = MyMainWindow()
window.show()
app.exec_()
