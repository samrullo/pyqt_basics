from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("QComboBox demonstration")

        dropdown_widget = QComboBox()
        dropdown_widget.addItems(["Bir", "Ikki", "Uch"])

        # combo boxes can be made editable allowing users to enter values
        # editing the current value causes a new value to be added to the dropdown list
        dropdown_widget.setEditable(True)

        # we can set Insert policy, such as whether values should be inserted at the top
        # or at the bottom
        dropdown_widget.setInsertPolicy(QComboBox.InsertAtTop)

        # you can also set maximum number of items in the combobox
        dropdown_widget.setMaxCount(10)

        dropdown_widget.currentIndexChanged.connect(self.index_changed)
        dropdown_widget.currentIndexChanged[str].connect(self.text_changed)



        self.setCentralWidget(dropdown_widget)

    def index_changed(self, i):
        print(f"drop down index changed : {i}")

    def text_changed(self, s):
        print(f"drop down text changed : {s}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
