from PyQt5 import QtWidgets
from urllib import request
import sys

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        date = self.get_data()
        rates = sorted(self.rates.keys())

        dateLabel = QtWidgets.QLabel(date)

        self.fromComboBox = QtWidgets.QComboBox()
        self.toComboBox = QtWidgets.QComboBox()

        self.fromComboBox.addItems(rates)
        self.toComboBox.addItems(rates)

        self.fromSpinBox = QtWidgets.QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 1000)
        self.fromSpinBox.setValue(1.00)

        self.toLabel = QtWidgets.QLabel("1.00")

        layout = QtWidgets.QGridLayout()
        layout.addWidget(dateLabel, 0, 0)
        layout.addWidget(self.fromComboBox, 1, 0)
        layout.addWidget(self.toComboBox, 2, 0)
        layout.addWidget(self.fromSpinBox, 1, 1)
        layout.addWidget(self.toLabel, 2, 1)
        self.setLayout(layout)

        self.fromComboBox.currentIndexChanged.connect(self.update_ui)
        self.toComboBox.currentIndexChanged.connect(self.update_ui)
        self.fromSpinBox.valueChanged.connect(self.update_ui)

    def get_data(self):
        self.rates = {}

        try:
            date = "Unknown"

            fh = request.urlopen("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")

            for line in fh:
                line = line.rstrip()
                if not line or line.startswith(("#", "Closing")):
                    continue

                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]

                else:
                    try:
                        value = float(fields[-1])
                        self.rates[fields[0]] = value
                    except ValueError:
                        pass

            return "Exchange rates date: " + date

        except Exception as e:
            return "Failed to download: \n%s" % e

    def update_ui(self):
        from_ = self.fromComboBox.currentText()
        to_ = self.toComboBox.currentText()

        result = (self.rates[from_] / self.rates[to_]) * self.fromSpinBox.value()

        self.toLabel.setText("%0.2f" % result)

app = QtWidgets.QApplication(sys.argv)
form = Form()
form.show()
app.exec_()