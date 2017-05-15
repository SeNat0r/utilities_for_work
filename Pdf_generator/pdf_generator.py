import sys

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QGridLayout, QLabel, QLineEdit, QPushButton,
    QComboBox, QSpacerItem, QSizePolicy, QRadioButton, QCheckBox
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

        self.__lastName = QLabel('Фамилия:', self)
        self.__firstName = QLabel('Имя:', self)
        self.__citizenship = QLabel('Гражданство:', self)
        self.__birthday = QLabel('Дата рождения:\n(ДДММГГГГ)\n', self)
        self.__sex = QLabel('Пол:', self)
        self.__pob = QLabel('Место рождения:', self)
        self.__state = QLabel('Государство:', self)
        self.__city = QLabel('Город:', self)
        self.__passport = QLabel('Паспорт:', self)
        self.__passSN = QLabel('Серия:', self)

        self.__lastNameEdit = QLineEdit(self, maxLength=35)
        self.__firstNameEdit = QLineEdit(self, maxLength=35)
        self.__citizenshipEdit = QLineEdit(self, maxLength=34)
        # self.__citizenshipSelect = QComboBox(self)
        # citizenships = ['Беларусь']
        # self.__citizenshipSelect.addItems(citizenships)
        self.__birthdayEdit = QLineEdit(self, maxLength=10)
        self.__maleRadio = QRadioButton('Мужской', self)
        self.__femaleRadio = QRadioButton('Женский', self)
        self.__stateCheck = QCheckBox('Совпадает с гражданством', self)
        self.__stateEdit = QLineEdit(self, maxLength=33)
        self.__cityEdit = QLineEdit(self, maxLength=33)
        self.__passportEdit = QLineEdit(self, maxLength=4)


        self.__generate = QPushButton('Генерировать', self)

    def initLayouts(self):
        w = QWidget(self)

        self.spacer_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.spacer_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # self.mainLayout = QVBoxLayout(w)
        self.mainLayout = QGridLayout(w)
        self.mainLayout.setSpacing(10)
        # self.inputLayout = QFormLayout(w)
        # self.inputLayout2 = QFormLayout(w)
        # self.inputLayout3 = QFormLayout(w)

        # self.mainLayout.addLayout(self.inputLayout)
        self.mainLayout.addWidget(self.__lastName, 1, 0)
        self.mainLayout.addWidget(self.__lastNameEdit, 1, 1, 1, 5)
        # self.inputLayout.addRow(self.__lastName, self.__lastNameEdit)
        self.mainLayout.addWidget(self.__firstName, 2, 0)
        self.mainLayout.addWidget(self.__firstNameEdit, 2, 1, 1, 5)
        # self.inputLayout.addRow(self.__firstName, self.__firstNameEdit)
        # self.inputLayout.addRow(self.__citizenship, self.__citizenshipSelect)
        # self.inputLayout.addRow(self.__citizenship, self.__citizenshipEdit)
        self.mainLayout.addWidget(self.__citizenship, 3, 0)
        self.mainLayout.addWidget(self.__citizenshipEdit, 3, 1, 1, 5)
        self.mainLayout.addWidget(self.__birthday, 4, 0)
        self.mainLayout.addWidget(self.__birthdayEdit, 4, 1)
        # self.inputLayout.addRow(self.__birthday, self.__birthdayEdit)
        self.mainLayout.addWidget(self.__sex, 5, 0)
        # self.mainLayout.addLayout(self.inputLayout2)
        # self.inputLayout2.addRow(self.__maleRadio, self.__femaleRadio)
        self.mainLayout.addWidget(self.__maleRadio, 5, 1)
        self.mainLayout.addWidget(self.__femaleRadio, 6, 1)
        self.mainLayout.addWidget(self.__pob, 7, 0)
        self.mainLayout.addWidget(self.__stateCheck, 8, 1)
        # self.mainLayout.addLayout(self.inputLayout3)
        # self.inputLayout3.addRow(self.__state, self.__stateEdit)
        self.mainLayout.addWidget(self.__state, 9, 0)
        self.mainLayout.addWidget(self.__stateEdit, 9, 1, 1, 5)
        # self.inputLayout3.addRow(self.__city, self.__cityEdit)
        self.mainLayout.addWidget(self.__city, 10, 0)
        self.mainLayout.addWidget(self.__stateEdit, 10, 1, 1, 5)
        # self.inputLayout3.addRow(self.__passport, self.__passportEdit)
        self.mainLayout.addWidget(self.__passport, 11, 0)
        self.mainLayout.addWidget(self.__passSN, 12, 0)
        self.mainLayout.addWidget(self.__passportEdit, 12, 1)
        self.mainLayout.addItem(self.spacer_2)
        self.mainLayout.addWidget(self.__generate, 13, 0, 1, 5)

        self.setCentralWidget(w)

    def generatePDF(self):
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf', 'UTF-8'))
        c = canvas.Canvas('123.pdf', pagesize=A4)
        c.setFont('Arial', 7.5)
        c.drawImage('blank.png', 0, 0, 594, 845)

        last_name = self.__lastNameEdit.text().upper()
        first_name = self.__firstNameEdit.text().upper()
        # citizenship = self.__citizenshipSelect.currentText().upper()
        citizenship = self.__citizenshipEdit.text().upper()
        birthday = ''
        tempnum = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for symb in self.__birthdayEdit.text():
            if symb in tempnum:
                birthday += symb
        if self.__stateCheck.isChecked():
            state = citizenship
        else:
            state = self.__stateEdit.text().upper()
        city = self.__cityEdit.text().upper()

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
        for s in birthday[2:4]:
            text = c.beginText(x, y)
            text.textLine(s)
            c.drawText(text)
            x += 13.3
        x = 206
        for s in birthday[4:]:
            text = c.beginText(x, y)
            text.textLine(s)
            c.drawText(text)
            x += 13.3

        if self.__maleRadio.isChecked():
            text = c.beginText(351.8, y)
            text.textLine('V')
            c.drawText(text)
        else:
            text = c.beginText(418.3, y)
            text.textLine('V')
            c.drawText(text)

        x = 112.5
        y = 615
        for s in state:
            text = c.beginText(x, y)
            text.textLine(s)
            c.drawText(text)
            x += 13.3

        x = 113
        y = 593
        for s in city:
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
