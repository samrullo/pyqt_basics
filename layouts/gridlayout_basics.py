from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from layouts.custom_color_widget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QGridLayout demo")

        layout = QGridLayout()
        layout.addWidget(ColorWidget('red'), 0, 0)
        layout.addWidget(ColorWidget('blue'), 0, 1)
        layout.addWidget(ColorWidget('green'), 1, 0)
        layout.addWidget(ColorWidget('yellow'), 1, 1)
        layout.addWidget(ColorWidget('purple'),2,1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
