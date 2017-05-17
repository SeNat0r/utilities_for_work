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
        self.resize(400, 900)

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
        self.__profession = QLabel('Профессия:', self)
        self.__entry = QLabel('Дата въезда:', self)
        self.__length = QLabel('Срок пребывания до:', self)
        self.__migCard = QLabel('Миграционная карта:', self)
        self.__vakeel = QLabel('Сведения\nо законных\nпредставителях:', self)
        self.__oldAddress = QLabel('Адрес прежнего\nместа\nпребывания в РФ:', self)
        self.__newAddress = QLabel('Место пребывания:', self)
        self.__region = QLabel('Область', self)
        self.__district = QLabel('Район', self)
        self.__newcity = QLabel('Город', self)
        self.__street = QLabel('Улица', self)
        self.__house = QLabel('Дом', self)
        self.__housing = QLabel('Корпус', self)
        self.__structure = QLabel('Строение', self)
        self.__apartment = QLabel('Квартира', self)
        self.__length2 = QLabel('На срок до', self)


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
        self.__professionEdit = QLineEdit(self, maxLength=35)
        self.__entryEdit = QLineEdit(self, maxLength=10)
        self.__lengthEdit = QLineEdit(self, maxLength=10)
        self.__migCardEdit = QLineEdit(self, maxLength=11)
        self.__vakeelEdit = QLineEdit(self, maxLength=38)
        self.__oldAddressEdit = QLineEdit(self, maxLength=57)
        self.__regionEdit = QLineEdit(self, maxLength=33)
        self.__districtEdit = QLineEdit(self, maxLength=35)
        self.__newcityEdit = QLineEdit(self, maxLength=33)
        self.__streetEdit = QLineEdit(self, maxLength=35)
        self.__houseEdit = QLineEdit(self, maxLength=4)
        self.__housingEdit = QLineEdit(self, maxLength=4)
        self.__structureEdit = QLineEdit(self, maxLength=4)
        self.__apartmentEdit = QLineEdit(self, maxLength=4)
        self.__length2Edit = QLineEdit(self, maxLength=10)

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
        self.mainLayout.addWidget(self.__permitValidity, 17, 2)
        self.mainLayout.addWidget(self.__permitValidityEdit, 17, 3)
        self.mainLayout.addWidget(self.__purpose, 18, 0)
        self.mainLayout.addWidget(self.__purposeBox, 18, 1, 1, 3)
        self.mainLayout.addWidget(self.__profession, 19, 0)
        self.mainLayout.addWidget(self.__professionEdit, 19, 1, 1, 3)
        self.mainLayout.addWidget(self.__entry, 20, 0)
        self.mainLayout.addWidget(self.__entryEdit, 20, 1)
        self.mainLayout.addWidget(self.__length, 20, 2)
        self.mainLayout.addWidget(self.__lengthEdit, 20, 3)
        self.mainLayout.addWidget(self.__migCard, 21, 0)
        self.mainLayout.addWidget(self.__migCardEdit, 21, 1, 1, 3)
        self.mainLayout.addWidget(self.__vakeel, 22, 0)
        self.mainLayout.addWidget(self.__vakeelEdit, 22, 1, 1, 3)
        self.mainLayout.addWidget(self.__oldAddress, 23, 0)
        self.mainLayout.addWidget(self.__oldAddressEdit, 23, 1, 1, 3)
        self.mainLayout.addWidget(self.__newAddress, 24, 0, 1, 3)
        self.mainLayout.addWidget(self.__region, 25, 0)
        self.mainLayout.addWidget(self.__regionEdit, 25, 1, 1, 3)
        self.mainLayout.addWidget(self.__district, 26, 0)
        self.mainLayout.addWidget(self.__districtEdit, 26, 1, 1, 3)
        self.mainLayout.addWidget(self.__newcity, 27, 0)
        self.mainLayout.addWidget(self.__newcityEdit, 27, 1, 1, 3)
        self.mainLayout.addWidget(self.__street, 28, 0)
        self.mainLayout.addWidget(self.__streetEdit, 28, 1, 1, 3)
        self.mainLayout.addWidget(self.__house, 29, 0)
        self.mainLayout.addWidget(self.__houseEdit, 29, 1)
        self.mainLayout.addWidget(self.__housing, 29, 2)
        self.mainLayout.addWidget(self.__housingEdit, 29, 3)
        self.mainLayout.addWidget(self.__structure, 30, 0)
        self.mainLayout.addWidget(self.__structureEdit, 30, 1)
        self.mainLayout.addWidget(self.__apartment, 30, 2)
        self.mainLayout.addWidget(self.__apartmentEdit, 30, 3)
        self.mainLayout.addWidget(self.__length2, 31, 0)
        self.mainLayout.addWidget(self.__length2Edit, 31, 1)

        self.mainLayout.addWidget(self.__generate, 35, 0, 1, 4)

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
        profession = self.__professionEdit.text().upper()
        entry = ''
        for symb in self.__entryEdit.text():
            if symb in tempnum:
                entry += symb
        length = ''
        for symb in self.__lengthEdit.text():
            if symb in tempnum:
                length += symb
        mig_card = self.__migCardEdit.text()
        vakeel = self.__vakeelEdit.text().upper()
        old_address = self.__oldAddressEdit.text().upper()
        region = self.__regionEdit.text().upper()
        district = self.__districtEdit.text().upper()
        newcity = self.__newcityEdit.text().upper()
        street = self.__streetEdit.text().upper()
        house = self.__houseEdit.text().upper()
        housing = self.__housingEdit.text().upper()
        structure = self.__structureEdit.text().upper()
        apartament = self.__apartmentEdit.text().upper()
        length2 = ''
        for symb in self.__length2Edit.text():
            if symb in tempnum:
                length2 += symb

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

        if purpose == 0:
            self.fill_radio(c, 139.4, 476)
        elif purpose == 1:
            self.fill_radio(c, 180, 476)
        elif purpose == 2:
            self.fill_radio(c, 232.6, 476)
        elif purpose == 3:
            self.fill_radio(c, 272.5, 476)
        elif purpose == 4:
            self.fill_radio(c, 312.4, 476)
        elif purpose == 5:
            self.fill_radio(c, 352.3, 476)
        elif purpose == 6:
            self.fill_radio(c, 392.2, 476)
        elif purpose == 7:
            self.fill_radio(c, 458.7, 476)
        elif purpose == 8:
            self.fill_radio(c, 498.6, 476)

        self.fill_text(c, profession, 86, 461)

        self.fill_text(c, entry[:2], 126.4, 440)
        self.fill_text(c, entry[2:4], 179.6, 440)
        self.fill_text(c, entry[4:], 219.5, 440)

        self.fill_text(c, length[:2], 405.5, 440)
        self.fill_text(c, length[2:4], 459.7, 440)
        self.fill_text(c, length[4:], 499.6, 440)

        self.fill_text(c, mig_card[:4], 152.7, 425)
        self.fill_text(c, mig_card[4:], 219.5, 425)

        self.fill_text(c, vakeel[:19], 99.1, 400)
        self.fill_text(c, vakeel[19:], 99.1, 383)

        self.fill_text(c, old_address[:19], 99.1, 352)
        self.fill_text(c, old_address[19:38], 99.1, 336)
        self.fill_text(c, old_address[38:], 99.1, 321)

        # линия отрыва

        self.fill_text(c, last_name, 85.5, 264)
        self.fill_text(c, first_name, 85.5, 247)
        self.fill_text(c, citizenship, 99.1, 227)
        self.fill_text(c, birthday[0:2], 113.1, 205)
        self.fill_text(c, birthday[2:4], 166, 205)
        self.fill_text(c, birthday[4:], 206, 205)
        if self.__maleRadio.isChecked():
            self.fill_radio(c, 366, 205)
        else:
            self.fill_radio(c, 432.5, 205)
        self.fill_text(c, 'ПАСПОРТ', 192.8, 190)
        self.fill_text(c, passportSN, 366, 190)
        self.fill_text(c, passportN, 432.5, 190)
        self.fill_text(c, region, 113.1, 162)
        self.fill_text(c, district, 85.5, 146)
        self.fill_text(c, newcity, 112, 129)
        self.fill_text(c, street, 85.5, 113)
        self.fill_text(c, house, 72.2, 97)
        self.fill_text(c, housing, 153, 97)
        self.fill_text(c, structure, 259.4, 97)
        self.fill_text(c, apartament, 352.5, 97)
        self.fill_text(c, length2[:2], 153, 81)
        self.fill_text(c, length2[2:4], 206.2, 81)
        self.fill_text(c, length2[4:], 259.4, 81)

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
