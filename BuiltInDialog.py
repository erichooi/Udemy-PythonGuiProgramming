from PyQt5 import QtWidgets
import sys

__appname__ = "BuiltInDialog"

class Program(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        openButton = QtWidgets.QPushButton("Open")
        saveButton = QtWidgets.QPushButton("Save")
        dirButton = QtWidgets.QPushButton("Other")
        closeButton = QtWidgets.QPushButton("Close...")

        openButton.clicked.connect(self.open)
        saveButton.clicked.connect(self.save)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(saveButton)
        layout.addWidget(dirButton)
        layout.addWidget(closeButton)
        self.setLayout(layout)

    def open(self):
        dir = "."
        fileObj = QtWidgets.QFileDialog.getOpenFileName(self, "{0} Open File Dialog".format(__appname__), dir, "Text files (*.txt)")
        print(fileObj)
        print(type(fileObj))

        filename = fileObj[0]

        file = open(filename, "r")
        read = file.read()
        file.close()
        print(read)

    def save(self):
        dir = "."

        fileObj = QtWidgets.QFileDialog.getSaveFileName(self, __appname__, dir, 'Text files (*.txt)')
        print(fileObj)
        print(type(fileObj))

        contents = "Hello world"
        filename = fileObj[0]
        open(filename, "w").write(contents)



app = QtWidgets.QApplication(sys.argv)
form = Program()
form.show()
form.exec_()