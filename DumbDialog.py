from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys

__appname__ = "DumbDialog"

class Program(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        self.btn = QtWidgets.QPushButton("Open Dialog")
        self.label1 = QtWidgets.QLabel("Label 1 Result")
        self.label2 = QtWidgets.QLabel("Label 2 Result")

        self.btn.clicked.connect(self.dialogOpen)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)

    def dialogOpen(self):
        dialog = Dialog()
        if dialog.exec_():
            self.label1.setText("Spinbox value is " + str(dialog.spinBox.value()))
            self.label2.setText("Checkbox is " + str(dialog.checkBox.isChecked()))

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        self.checkBox = QtWidgets.QCheckBox()
        self.spinBox = QtWidgets.QSpinBox()
        self.buttonOk = QtWidgets.QPushButton("OK")
        self.buttonCancel = QtWidgets.QPushButton("Cancel")

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.spinBox, 0, 0)
        layout.addWidget(self.checkBox, 0, 1)
        layout.addWidget(self.buttonCancel)
        layout.addWidget(self.buttonOk)
        self.setLayout(layout)

        self.buttonOk.clicked.connect(self.accept)
        self.buttonCancel.clicked.connect(self.reject)

app = QtWidgets.QApplication(sys.argv)
form = Program()
form.show()
form.exec_()