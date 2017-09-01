from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys

import iconDisplay

class MainDialog(QtWidgets.QDialog, iconDisplay.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
form = MainDialog()
form.show()
form.exec_()