from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys

import showGui

class MainDialog(QtWidgets.QDialog, showGui.Ui_mainDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.showButton.clicked.connect(self.showMessageBox)

    def showMessageBox(self):
        QtWidgets.QMessageBox.information(self, "Hello!", "Hello there, " + self.nameEdit.text())


app = QtWidgets.QApplication(sys.argv)
form = MainDialog()
form.show()
form.exec_()