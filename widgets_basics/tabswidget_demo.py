from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from layouts.custom_color_widget import ColorWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QStackedLayout demo")

        tabs_widget = QTabWidget()
        tabs_widget.setDocumentMode(False)
        tabs_widget.setTabPosition(QTabWidget.West)

        colors = ['red', 'blue', 'green', 'yellow', 'purple', 'brown']

        for idx, color in enumerate(colors):
            tabs_widget.addTab(ColorWidget(color), color)

        self.setCentralWidget(tabs_widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
