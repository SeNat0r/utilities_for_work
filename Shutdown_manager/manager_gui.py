import sys

from PyQt5.QtWidgets import (
QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableView, QTableWidgetItem,
QHBoxLayout
)
from  PyQt5.QtSql import QSqlQueryModel, QSqlDatabase, QSqlQuery


class Manager(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUi()
        self.initSignals()
        self.initLayouts()

    def initUi(self):
        # self.db()
        self.setWindowTitle('Shutdown manager')
        self.createTable()

        self.convertBtn = QPushButton('Обновить', self)

    # def db(self):
    #     self.db = QSqlDatabase.addDatabase('QSQLITE')
    #     self.db.setDatabaseName('base.db')
    #     self.db.open()
    #
    #     self.projectModel = QSqlQueryModel()
    #     self.projectModel.setQuery('SELECT * FROM manager', self.db)
    #
    #     self.projectView = QTableView()
    #     self.projectView.setModel(self.projectModel)
    def initSignals(self):
        pass

    def initLayouts(self):
        w = QWidget(self)

        self.mainLayout = QHBoxLayout(w)
        self.mainLayout.addWidget(self.tableWidget)
        self.mainLayout.addWidget(self.convertBtn)
        # self.setLayout(self.mainLayout)

        self.setCentralWidget(w)

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.move(0, 0)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    sm = Manager()
    # sm.projectView.show()
    sm.show()

    sys.exit(app.exec_())