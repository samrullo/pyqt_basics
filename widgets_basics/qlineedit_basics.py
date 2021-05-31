"""
QLineEdit is heavily used in forms.
It allows to enter text like username, address etc...
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        line = QLineEdit()
        line.setMaxLength(50)
        line.setPlaceholderText("Enter what you want...")

        # signal that notifies we pressed Enter on QLineEdit widget
        line.returnPressed.connect(self.return_pressed)

        # signal that's triggered whenever we select some part of the text
        line.selectionChanged.connect(self.selection_changed)

        # signal triggered whenever the text of the QLineEdit widget changes
        line.textChanged.connect(self.text_changed)

        # signal triggered whenever the text of the QLineEdit widget is edited
        line.textEdited.connect(self.text_edited)

        self.setCentralWidget(line)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed!")
        print(f"Selected text : {self.centralWidget().selectedText()}")

    def text_changed(self, s):
        print("Text changed...")
        print(f"Changed text : {s}")

    def text_edited(self, s):
        print("Text edited...")
        print(f"Edited text : {s}")


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
