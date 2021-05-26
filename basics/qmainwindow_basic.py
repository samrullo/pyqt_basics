from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# for access to command line arguments
import sys

app=QApplication(sys.argv)
window=QMainWindow()
window.show() # by default QMainWindow is invisible

# start the event loop
app.exec_()