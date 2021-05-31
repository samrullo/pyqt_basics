from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("QCheckBox demo")

        checkbox = QCheckBox()
        checkbox.setCheckState(Qt.Checked)
        checkbox.stateChanged.connect(self.on_state_changed)

        self.setCentralWidget(checkbox)

    def on_state_changed(self, s):
        print(f"is state checked : {s == Qt.Checked}")
        print(f"checked state numerical value : {s}")


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
