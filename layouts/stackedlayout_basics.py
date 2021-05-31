from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from layouts.custom_color_widget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout demo")

        layout = QStackedLayout()
        layout.addWidget(ColorWidget('red'))
        layout.addWidget(ColorWidget('blue'))
        layout.addWidget(ColorWidget('green'))

        layout.setCurrentIndex(1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
