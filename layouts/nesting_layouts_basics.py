from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from layouts.custom_color_widget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Nesting layouts demo")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3=QVBoxLayout()

        layout2.addWidget(ColorWidget('red'))
        layout2.addWidget(ColorWidget('blue'))
        layout2.addWidget(ColorWidget('yellow'))

        layout1.addLayout(layout2)

        layout1.addWidget(ColorWidget('green'))

        layout3.addWidget(ColorWidget('purple'))
        layout3.addWidget(ColorWidget('gold'))
        layout1.addLayout(layout3)


        main_widget = QWidget()
        main_widget.setLayout(layout1)

        self.setCentralWidget(main_widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
