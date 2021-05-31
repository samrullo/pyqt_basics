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
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon(os.path.relpath('../icons/bug.png')), 'My Action', self)
        button_action.setStatusTip('My Action status tip')
        button_action.triggered.connect(self.onActionTriggered)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        button_action2 = QAction(QIcon('../icons/cookie-bite.png'), 'My Action 2', self)
        button_action2.setStatusTip('This is status tip for My Action 2')
        button_action2.triggered.connect(self.onActionTriggered)
        toolbar.addAction(button_action2)
        self.setStatusBar(QStatusBar(self))

        # add a menubar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

    def onTitleChanged(self, s):
        print(f"window title changed : {s}")

    def onActionTriggered(self, s):
        print(f"my action was triggered : {s}")


app = QApplication(sys.argv)
window = MyMainWindow()
window.show()
app.exec_()
