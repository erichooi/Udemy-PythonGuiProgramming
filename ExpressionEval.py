import sys
from PyQt5.QtWidgets import QDialog, QApplication


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)




app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()