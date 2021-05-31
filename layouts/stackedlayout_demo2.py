from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from layouts.custom_color_widget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QStackedLayout demo")

        main_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()
        stacked_layout = QStackedLayout()

        colors = ['red', 'blue', 'green', 'yellow', 'purple', 'brown']

        for idx, color in enumerate(colors):
            stacked_layout.addWidget(ColorWidget(color))
            btn = QPushButton(color)
            btn.pressed.connect(lambda idx=idx: stacked_layout.setCurrentIndex(idx))
            buttons_layout.addWidget(btn)

        main_layout.addLayout(buttons_layout)
        main_layout.addLayout(stacked_layout)
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
