import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QHBoxLayout, QAbstractItemView, QFormLayout, QTableView
)

from manager import storage


class Manager(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUi()
        self.initSignals()
        self.initLayouts()

    def initUi(self):
        self.setWindowTitle('Shutdown manager')
        self.createTable()
        self.tableData()
        self.infoUI()

        self.refreshBtn = QPushButton('Обновить', self)
        self.editVM = QPushButton('Изменить ВМ', self)
        self.shutdownVM = QPushButton('Выключить ВМ', self)


    def infoUI(self):
        self.infoLabelTCName = QLabel('Имя машины:', self)
        self.infoLabelIP = QLabel('IP', self)
        self.infoLabelVM = QLabel('Виртуальная машина:', self)
        self.infoLabelVMIP = QLabel('ВМ IP:', self)
        self.infoTCName = QLabel('Не выбрано', self)
        self.infoIP = QLabel('Не выбрано', self)
        self.infoVM = QLabel('Не выбрано', self)
        self.infoVMIP = QLabel('Не выбрано', self)


    def initLayouts(self):
        w = QWidget(self)

        self.mainLayout = QHBoxLayout(w)
        self.rightLayout = QVBoxLayout(w)
        self.leftLayout = QVBoxLayout(w)
        self.infoLayout = QFormLayout(w)

        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.rightLayout)

        self.leftLayout.addWidget(self.tableWidget)
        self.leftLayout.addWidget(self.refreshBtn)

        self.rightLayout.addLayout(self.infoLayout)

        self.rightLayout.addStretch()
        self.rightLayout.addWidget(self.editVM)
        self.rightLayout.addWidget(self.shutdownVM)

        self.infoLayout.addRow(self.infoLabelTCName, self.infoTCName)
        self.infoLayout.addRow(self.infoLabelIP, self.infoIP)
        self.infoLayout.addRow(self.infoLabelVM, self.infoVM)
        self.infoLayout.addRow(self.infoLabelVMIP, self.infoVMIP)

        self.setLayout(self.mainLayout)

        self.setCentralWidget(w)

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setSelectionBehavior(QTableView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Токий клиент", "ВМ", "В сети"])
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def tableData(self):
        self.conn = storage.connect('base.db')
        storage.initialize(self.conn)
        all_data = storage.all_data(self.conn)
        rowcount = 0
        for data in all_data:
            rowcount += 1
            self.tableWidget.setRowCount(rowcount)
            self.tableWidget.setItem(rowcount - 1, 0, QTableWidgetItem(data['host_name']))

    def getRow(self, row, b):
        row = self.tableWidget.currentRow()
        self.dataToInfo(row)

    def dataToInfo(self, a):
        b = self.tableWidget.item(a, 0)
        d = storage.find_by_name(self.conn, b.text())
        self.infoTCName.setText(d['host_name'])
        self.infoIP.setText(d['tc_ip'])
        self.infoVM.setText(d['vm_name'])
        self.infoVMIP.setText(d['vm_ip'])

    def initSignals(self):
        self.tableWidget.cellClicked.connect(self.getRow)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sm = Manager()
    sm.show()

    sys.exit(app.exec_())
