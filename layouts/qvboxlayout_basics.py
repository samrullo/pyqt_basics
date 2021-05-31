from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from layouts.custom_color_widget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("QVBoxLayout demo")

        layout = QVBoxLayout()
        red_widget = ColorWidget('red')
        layout.addWidget(red_widget)

        green_widget=ColorWidget('green')
        layout.addWidget(green_widget)

        yellow_widget=ColorWidget('yellow')
        layout.addWidget(yellow_widget)

        main_widget = QWidget()
        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
