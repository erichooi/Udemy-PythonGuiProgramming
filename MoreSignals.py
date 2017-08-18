# Custom make signal
from PyQt5 import QtWidgets, QtCore
import sys

class ZeroSpinBox(QtWidgets.QSpinBox):

    zeros = 0
    atZero = QtCore.pyqtSignal(int, int)

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)

        self.valueChanged.connect(self.check_zero)

    def check_zero(self, value):
        if value == 0:
            self.zeros += 1
            self.constant = 5
            self.atZero.emit(self.zeros, self.constant)

class Form(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.dial = QtWidgets.QDial()
        self.dial.setNotchesVisible(True)

        self.spinbox = ZeroSpinBox()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)

        self.spinbox.atZero.connect(self.printValue)

    def printValue(self, zeros, constant):
        print("The Spinbox has been at zero {0} times".format(zeros))
        print("The constant is {0}".format(constant))

app = QtWidgets.QApplication(sys.argv)
form = Form()
form.show()
app.exec_()