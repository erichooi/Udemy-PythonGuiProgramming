from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys

__appname__ = "StandardDialog"

class Program(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        self.btn = QtWidgets.QPushButton("Open Dialog")
        self.mainSpinBox = QtWidgets.QSpinBox()
        self.mainCheckBox = QtWidgets.QCheckBox("Main Checkbox Value")

        self.btn.clicked.connect(self.dialogOpen)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.mainSpinBox)
        layout.addWidget(self.mainCheckBox)
        self.setLayout(layout)


    def dialogOpen(self):
        initValues = {"mainSpinBox": self.mainSpinBox.value(), "mainCheckBox": self.mainCheckBox.isChecked()}
        dialog = Dialog(initValues)
        if dialog.exec_():
            self.mainSpinBox.setValue(dialog.spinBox.value())
            self.mainCheckBox.setChecked(dialog.checkBox.isChecked())

class Dialog(QtWidgets.QDialog):
    def __init__(self, initValues, parent=None):
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

        self.spinBox.setValue(initValues["mainSpinBox"])
        self.checkBox.setChecked(initValues["mainCheckBox"])

        self.buttonOk.clicked.connect(self.accept)
        self.buttonCancel.clicked.connect(self.reject)

    def accept(self):

        class GreaterThanFive(Exception): pass
        class IsZero(Exception): pass

        try:
            if self.spinBox.value() > 5:
                raise GreaterThanFive("The SpinBox value cannot be greater than 5")
            elif self.spinBox.value() == 0:
                raise IsZero("The SpinBox value cannot be equal to 0")
            else:
                QtWidgets.QDialog.accept(self)
        except GreaterThanFive as e:
            QtWidgets.QMessageBox.warning(self, __appname__, str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return
        except IsZero as e:
            QtWidgets.QMessageBox.warning(self, __appname__, str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return

app = QtWidgets.QApplication(sys.argv)
form = Program()
form.show()
form.exec_()