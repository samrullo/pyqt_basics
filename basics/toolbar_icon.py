from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os


class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.windowTitleChanged.connect(self.onTitleChanged)

        self.setWindowTitle("My Awesome Main Window")

        label = QLabel("AWESOME LABEL")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My toolbar')
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon(os.path.relpath('../icons/bug.png')),'My Action', self)
        button_action.setStatusTip('My Action status tip')
        button_action.triggered.connect(self.onActionTriggered)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onTitleChanged(self, s):
        print(f"window title changed : {s}")

    def onActionTriggered(self, s):
        print(f"my action was triggered : {s}")


app = QApplication(sys.argv)
window = MyMainWindow()
window.show()
app.exec_()
