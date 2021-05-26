from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome Main Window")

        label = QLabel("AWESOME LABEL")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)


app = QApplication(sys.argv)
window = MyMainWindow()
window.show()
app.exec_()
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome Main Window")

        label = QLabel("AWESOME LABEL")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My Toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("Your button", self)
        button_action.setStatusTip("Your button status tip")
        button_action.triggered.connect(self.onToolButtonTriggered)
        toolbar.addAction(button_action)

    def onToolButtonTriggered(self, s):
        print(f"toolbar button was triggered : {s}")

    def onTitleChanged(self, window_title):
        print(f"window title changed to {window_title}")


app = QApplication(sys.argv)
window = MyMainWindow()
window.show()
app.exec_()
