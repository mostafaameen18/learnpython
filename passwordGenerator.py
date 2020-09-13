from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QCheckBox, QRadioButton, QLabel, QGroupBox, QGridLayout, QVBoxLayout
import sys
import string
from random import randint, choice
import pyperclip

class calculator(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Password Generator"
        self.left = 600
        self.top = 100
        self.width = 300
        self.height = 300
        self.text = ""
        self.windowoptions()

    def windowoptions(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.components()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupbox)


        self.setLayout(self.vbox)

        self.show()

    def components(self):
        self.groupbox = QGroupBox("Detect your password options")
        self.gridbox = QGridLayout()

        self.charchoice = QCheckBox('Include Characters [a-z,A-Z]',self)
        self.gridbox.addWidget(self.charchoice,0,0)

        self.numbers = QCheckBox('Include numbers [0-9]', self)
        self.gridbox.addWidget(self.numbers, 1,0)

        self.label = QLabel("Choose length of password")
        self.label.setStyleSheet("color: dodgerblue; text-align: cener;")
        self.gridbox.addWidget(self.label, 2,0)

        self.five = QRadioButton("5")
        self.five.clicked.connect(self.radiochecker)
        self.gridbox.addWidget(self.five, 3, 0)

        self.ten = QRadioButton("10")
        self.ten.clicked.connect(self.radiochecker)
        self.gridbox.addWidget(self.ten, 4, 0)

        self.fifteen = QRadioButton("15")
        self.fifteen.clicked.connect(self.radiochecker)
        self.gridbox.addWidget(self.fifteen, 5, 0)

        self.twenty = QRadioButton("20")
        self.twenty.clicked.connect(self.radiochecker)
        self.gridbox.addWidget(self.twenty, 6, 0)

        self.generatebtn = QPushButton("Generate")
        self.generatebtn.clicked.connect(self.generate)
        self.gridbox.addWidget(self.generatebtn, 7,0)

        self.label = QLabel(self)
        self.label.setStyleSheet("border: 2px solid grey; background:whitesmoke; color: black; height: 50; font-weight: bold;")
        self.gridbox.addWidget(self.label, 8,0)

        self.copybtn = QPushButton("Copy to Clipboard")
        self.copybtn.clicked.connect(self.copyToClipboard)
        self.gridbox.addWidget(self.copybtn, 9, 0)

        self.groupbox.setLayout(self.gridbox)

    def radiochecker(self):
        self.checkedradio = self.sender()

        if self.checkedradio.isChecked():
            self.choosenLength = int(self.checkedradio.text())

    def generate(self):
        try:
            self.letters = string.ascii_letters
            self.digits = string.digits
            self.chars = []
            if self.charchoice.isChecked():
                self.chars += self.letters

            if self.numbers.isChecked():
                self.chars += self.digits

            self.length = self.choosenLength
            self.code = "".join(choice(self.chars) for x in range(randint(self.length, self.length)))
            self.label.setStyleSheet("border: 2px solid grey; background:whitesmoke; color: black; padding: 5px;")
            self.label.setText(self.code)
        except:
            self.label.setStyleSheet("background: #d9534f; color: white; padding: 5px;")
            self.label.setText("Wrong enteries!!")

    def copyToClipboard(self):
        if self.label.text() == "Wrong enteries!!":
            pass
        else:
            try:
                pyperclip.copy(self.code)
                self.label.setStyleSheet("background: #5cb85c; color: white; padding: 5px;")
                self.label.setText("Copied To Clipboard")
            except:
                pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = calculator()
    sys.exit(app.exec())

