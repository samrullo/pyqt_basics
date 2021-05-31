from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from layouts.custom_color_widget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("QHBoxLayout demo")

        layout = QHBoxLayout()

        layout.addWidget(ColorWidget('red'))
        layout.addWidget(ColorWidget('blue'))
        layout.addWidget(ColorWidget('green'))
        layout.addWidget(ColorWidget('brown'))

        main_widget = QWidget()
        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
