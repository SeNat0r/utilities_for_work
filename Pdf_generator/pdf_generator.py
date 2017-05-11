import sys

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton,
    QComboBox
)


class pdf_generator(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUi()
        self.initSignals()
        self.initLayouts()

    def initUi(self):
        self.setWindowTitle('Генератор бланков')
        self.resize(400, 300)

        self.__lastName = QLabel('Фамилия', self)
        self.__firstName = QLabel('Имя', self)
        self.__citizenship = QLabel('Гражданство', self)
        self.__birthday = QLabel('Дата рождения\nЗаполнять в формате:\nДД-ММ-ГГГГ', self)

        self.__lastNameEdit = QLineEdit(self, maxLength=35)
        self.__firstNameEdit = QLineEdit(self, maxLength=35)

        self.__citizenshipSelect = QComboBox(self)
        citizenships = ['Беларусь']
        self.__citizenshipSelect.addItems(citizenships)

        self.__birthdayEdit = QLineEdit(self, maxLength=10)


        self.__generate = QPushButton('Генерировать', self)

    def initLayouts(self):
        w = QWidget(self)

        self.mainLayout = QVBoxLayout(w)
        self.inputLayout = QFormLayout(w)

        self.mainLayout.addLayout(self.inputLayout)
        self.inputLayout.addRow(self.__lastName, self.__lastNameEdit)
        self.inputLayout.addRow(self.__firstName, self.__firstNameEdit)
        self.inputLayout.addRow(self.__citizenship, self.__citizenshipSelect)
        self.inputLayout.addRow(self.__birthday, self.__birthdayEdit)
        self.mainLayout.addWidget(self.__generate)

        self.setCentralWidget(w)

    def generatePDF(self):
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf', 'UTF-8'))
        c = canvas.Canvas('123.pdf', pagesize=A4)
        c.setFont('Arial', 7.5)
        c.drawImage('blank.png', 0, 0, 594, 845)

        last_name = self.__lastNameEdit.text().upper()
        first_name = self.__firstNameEdit.text().upper()
        citizenship = self.__citizenshipSelect.currentText().upper()
        birthday = self.__birthdayEdit.text()

        x = 85.5
        y = 697
        for s in last_name:
            text = c.beginText(x, y)
            text.textLine(s)
            c.drawText(text)
            x += 13.3

        x = 85.5
        y = 677
        for s in first_name:
            text = c.beginText(x, y)
            text.textLine(s)
            c.drawText(text)
            x += 13.3

        x = 98.8
        y = 656
        for s in citizenship:
            text = c.beginText(x, y)
            text.textLine(s)
            c.drawText(text)
            x += 13.3

        x = 113.1
        y = 635
        for s in birthday[:2]:
            text = c.beginText(x, y)
            text.textLine(s)
            c.drawText(text)
            x += 13.3
        x = 166
        for s in birthday[3:5]:
            text = c.beginText(x, y)
            text.textLine(s)
            c.drawText(text)
            x += 13.3
        x = 206
        for s in birthday[6:]:
            text = c.beginText(x, y)
            text.textLine(s)
            c.drawText(text)
            x += 13.3

        c.save()

    def initSignals(self):
        self.__generate.clicked.connect(self.generatePDF)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    lb = pdf_generator()
    lb.show()

    sys.exit(app.exec_())
