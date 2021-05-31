from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ColorWidget(QWidget):
    def __init__(self, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    widget = ColorWidget('red')
    window.setCentralWidget(widget)
    window.show()
    app.exec_()
