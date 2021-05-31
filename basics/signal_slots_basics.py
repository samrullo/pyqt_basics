from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.windowTitleChanged.connect(self.onTitleChanged)

        self.setWindowTitle("My Awesome Main Window")

        label = QLabel("AWESOME LABEL")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

    def onTitleChanged(self, s):
        print(f"window title changed : {s}")


app = QApplication(sys.argv)
window = MyMainWindow()
window.show()
app.exec_()
