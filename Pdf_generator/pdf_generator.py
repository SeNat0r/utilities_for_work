import sys, os.path

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton,
    QComboBox, QSpacerItem, QSizePolicy, QRadioButton, QCheckBox
)
from PyQt5.QtCore import Qt


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
        self.__state = QLabel('Государство', self)
        self.__state.setAlignment(Qt.AlignRight)
        self.__city = QLabel('Город', self)
        self.__city.setAlignment(Qt.AlignRight)
        self.__passport = QLabel('Паспорт:', self)
        self.__passSN = QLabel('Серия', self)
        self.__passSN.setAlignment(Qt.AlignRight)
        self.__passNum = QLabel('№', self)
        self.__passNum.setAlignment(Qt.AlignRight)
        self.__dateOfIssue = QLabel('Дата выдачи', self)
        self.__dateOfIssue.setAlignment(Qt.AlignRight)
        self.__validity = QLabel('Срок', self)
        self.__validity.setAlignment(Qt.AlignRight)
        self.__permit = QLabel('Документ на право\nпребывания:', self)
        self.__permitS = QLabel('Серия', self)
        self.__permitS.setAlignment(Qt.AlignRight)
        self.__permitN = QLabel('№', self)
        self.__permitN.setAlignment(Qt.AlignRight)
        self.__permitDate = QLabel('Дата выдачи', self)
        self.__permitDate.setAlignment(Qt.AlignRight)
        self.__permitValidity = QLabel('Срок', self)
        self.__permitValidity.setAlignment(Qt.AlignRight)
        self.__purpose = QLabel('Цель въезда:', self)

        self.__lastNameEdit = QLineEdit(self, maxLength=35)
        self.__firstNameEdit = QLineEdit(self, maxLength=35)
        self.__citizenshipEdit = QLineEdit(self, maxLength=34)
        self.__birthdayEdit = QLineEdit(self, maxLength=10)
        self.__maleRadio = QRadioButton('Мужской', self)
        self.__femaleRadio = QRadioButton('Женский', self)
        self.__stateCheck = QCheckBox('Совпадает с гражданством', self)
        self.__stateEdit = QLineEdit(self, maxLength=33)
        self.__cityEdit = QLineEdit(self, maxLength=33)
        self.__passportEdit = QLineEdit(self, maxLength=4)
        self.__passportNumEdit = QLineEdit(self, maxLength=9)
        self.__dateOfIssueEdit = QLineEdit(self, maxLength=10)
        self.__validityEdit = QLineEdit(self, maxLength=10)
        self.__permitBox = QComboBox(self)
        permits = ['Виза', 'Вид на жительство', 'Разрешение на временное проживание']
        self.__permitBox.addItems(permits)
        self.__permitSEdit = QLineEdit(self, maxLength=4)
        self.__permitNEdit = QLineEdit(self, maxLength=9)
        self.__permitDateEdit = QLineEdit(self, maxLength=10)
        self.__permitValidityEdit = QLineEdit(self, maxLength=10)
        self.__purposeBox = QComboBox(self)
        purposes = ['служебная', 'туризм', 'деловая', 'учеба', 'работа', 'частная', 'транзит', 'гуманитарная', 'другая']
        self.__purposeBox.addItems(purposes)



        self.__generate = QPushButton('Генерировать', self)

    def initLayouts(self):
        w = QWidget(self)

        self.spacer_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.spacer_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainLayout = QGridLayout(w)
        self.mainLayout.setSpacing(8)

        self.mainLayout.addWidget(self.__lastName, 1, 0)
        self.mainLayout.addWidget(self.__lastNameEdit, 1, 1, 1, 3)
        self.mainLayout.addWidget(self.__firstName, 2, 0)
        self.mainLayout.addWidget(self.__firstNameEdit, 2, 1, 1, 3)
        self.mainLayout.addWidget(self.__citizenship, 3, 0)
        self.mainLayout.addWidget(self.__citizenshipEdit, 3, 1, 1, 3)
        self.mainLayout.addWidget(self.__birthday, 4, 0)
        self.mainLayout.addWidget(self.__birthdayEdit, 4, 1)
        self.mainLayout.addWidget(self.__sex, 5, 0)
        self.mainLayout.addWidget(self.__maleRadio, 5, 1, 1, 3)
        self.mainLayout.addWidget(self.__femaleRadio, 6, 1, 1, 3)
        self.mainLayout.addWidget(self.__pob, 7, 0)
        self.mainLayout.addWidget(self.__state, 8, 0)
        self.mainLayout.addWidget(self.__stateEdit, 8, 1, 1, 3)
        self.mainLayout.addWidget(self.__stateCheck, 9, 1, 1, 3)
        self.mainLayout.addWidget(self.__city, 10, 0)
        self.mainLayout.addWidget(self.__cityEdit, 10, 1, 1, 3)
        self.mainLayout.addWidget(self.__passport, 11, 0)
        self.mainLayout.addWidget(self.__passSN, 12, 0)
        self.mainLayout.addWidget(self.__passportEdit, 12, 1)
        self.mainLayout.addWidget(self.__passNum, 12, 2)
        self.mainLayout.addWidget(self.__passportNumEdit, 12, 3)
        self.mainLayout.addWidget(self.__dateOfIssue, 13, 0)
        self.mainLayout.addWidget(self.__dateOfIssueEdit, 13, 1)
        self.mainLayout.addWidget(self.__validity, 13, 2)
        self.mainLayout.addWidget(self.__validityEdit, 13, 3)
        self.mainLayout.addWidget(self.__permit, 14, 0)
        self.mainLayout.addWidget(self.__permitBox, 14, 1, 1, 3)
        self.mainLayout.addWidget(self.__permitS, 15, 0)
        self.mainLayout.addWidget(self.__permitSEdit, 15, 1)
        self.mainLayout.addWidget(self.__permitN, 15, 2)
        self.mainLayout.addWidget(self.__permitNEdit, 15, 3)
        self.mainLayout.addWidget(self.__permitDate, 17, 0)
        self.mainLayout.addWidget(self.__permitDateEdit, 17, 1)
        self.mainLayout.addWidget(self.__permitValidity, 18, 0)
        self.mainLayout.addWidget(self.__permitValidityEdit, 18, 1)
        self.mainLayout.addWidget(self.__purpose, 19, 0)
        self.mainLayout.addWidget(self.__purposeBox, 19, 1, 1, 3)


        self.mainLayout.addWidget(self.__generate, 20, 0, 1, 4)

        self.setCentralWidget(w)

    def generatePDF(self):
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf', 'UTF-8'))
        c = canvas.Canvas('123.pdf', pagesize=A4)
        c.setFont('Arial', 7.5)
        c.drawImage('blank.png', 0, 0, 594, 845)

        last_name = self.__lastNameEdit.text().upper()
        first_name = self.__firstNameEdit.text().upper()
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
        passportSN = self.__passportEdit.text()
        passportN = self.__passportNumEdit.text()
        dateOfIssue = ''
        for symb in self.__dateOfIssueEdit.text():
            if symb in tempnum:
                dateOfIssue += symb
        validity = ''
        for symb in self.__validityEdit.text():
            if symb in tempnum:
                validity += symb
        permit = self.__permitBox.currentIndex()
        permits = self.__permitSEdit.text()
        permitn = self.__permitNEdit.text()
        permit_date = ''
        for symb in self.__permitDateEdit.text():
            if symb in tempnum:
                permit_date += symb
        permit_validity = ''
        for symb in self.__permitValidityEdit.text():
            if symb in tempnum:
                permit_validity += symb
        purpose = self.__purposeBox.currentIndex()

        self.fill_text(c, last_name, 85.5, 697)
        self.fill_text(c, first_name, 85.5, 677)
        self.fill_text(c, citizenship, 98.8, 656)

        self.fill_text(c, birthday[:2], 113.1, 635)
        self.fill_text(c, birthday[2:4], 166, 635)
        self.fill_text(c, birthday[4:], 206, 635)

        if self.__maleRadio.isChecked():
            self.fill_radio(c, 351.8, 635)
        else:
            self.fill_radio(c, 418.3, 635)

        self.fill_text(c, state, 112.5, 615)
        self.fill_text(c, city, 113, 593)
        self.fill_text(c, 'ПАСПОРТ', 192.8, 578)
        self.fill_text(c, passportSN, 366, 578)
        self.fill_text(c, passportN, 432.5, 578)

        self.fill_text(c, dateOfIssue[:2], 99.8, 551)
        self.fill_text(c, dateOfIssue[2:4], 152.7, 551)
        self.fill_text(c, dateOfIssue[4:], 192.7, 551)

        self.fill_text(c, validity[:2], 312.5, 551)
        self.fill_text(c, validity[2:4], 365.7, 551)
        self.fill_text(c, validity[4:], 405.6, 551)

        if permit == 0:
            self.fill_radio(c, 86, 520)
        elif permit == 1:
            self.fill_radio(c, 180, 520)
        elif permit == 2:
            self.fill_radio(c, 312, 520)

        self.fill_text(c, permits, 365.7, 520)
        self.fill_text(c, permitn, 432.1, 520)

        self.fill_text(c, permit_date[:2], 99.8, 493)
        self.fill_text(c, permit_date[2:4], 152.7, 493)
        self.fill_text(c, permit_date[4:], 192.7, 493)

        self.fill_text(c, permit_validity[:2], 312.5, 493)
        self.fill_text(c, permit_validity[2:4], 365.7, 493)
        self.fill_text(c, permit_validity[4:], 405.6, 493)

        c.save()

    def initSignals(self):
        self.__generate.clicked.connect(self.generatePDF)

    def fill_text(self, canvas, data,x, y):
        for s in data:
            text = canvas.beginText(x, y)
            text.textLine(s)
            canvas.drawText(text)
            x += 13.3

    def fill_radio(self, canvas, x, y):
        text = canvas.beginText(x, y)
        text.textLine('V')
        canvas.drawText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    lb = pdf_generator()
    lb.show()

    sys.exit(app.exec_())
