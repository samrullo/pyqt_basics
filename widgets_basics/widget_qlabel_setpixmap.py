from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MyMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome Main Window")

        label = QLabel("AWESOME LABEL")
        # label.setScaledContents(False)
        label.setPixmap(QPixmap('/Users/samrullo/Downloads/samira_photo.JPG'))

        self.setCentralWidget(label)


app = QApplication(sys.argv)
window = MyMainWindow()
window.show()
app.exec_()
