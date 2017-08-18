from PyQt5 import QtWidgets
import sys

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.dial = QtWidgets.QDial()
        self.dial.setNotchesVisible(True)

        self.spinbox = QtWidgets.QSpinBox()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)

app = QtWidgets.QApplication(sys.argv)
form = Form()
form.show()
app.exec_()