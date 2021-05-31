"""
QListWidget is similar to QCombobox
It is a dropdown list
It differs in the signals it provides
It offers signals such as currentItemChanged which passes QListItem
and currentTextChanged which passes the text of the current QListItem
"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("QListWidget demonstration")

        dropdown_widget = QListWidget()
        dropdown_widget.addItems(["Bir", "Ikki", "Uch"])

        dropdown_widget.currentItemChanged.connect(self.item_changed)
        dropdown_widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(dropdown_widget)

    def item_changed(self, i):  # i is a QListItem
        print(f"drop down item changed : {i.text()}")

    def text_changed(self, s):
        print(f"drop down text changed : {s}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
