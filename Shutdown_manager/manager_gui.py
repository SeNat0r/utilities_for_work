import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QHBoxLayout, QGroupBox, QAbstractItemView, QFormLayout
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

        self.refreshBtn = QPushButton('Обновить', self)
        self.editVM = QPushButton('Изменить ВМ', self)
        self.shutdownVM = QPushButton('Выключить ВМ', self)
        self.info = QLabel('Инфо', self)
        self.infoLabel1 = QLabel('Имя машины:', self)
        self.infoLabel2 = QLabel('ВМ:', self)
        self.infoData1 = QLabel('10-1-001', self)
        self.infoData2 = QLabel('ThinVm001', self)

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

        self.infoLayout.addRow(self.infoLabel1, self.infoData1)
        self.infoLayout.addRow(self.infoLabel2, self.infoData2)

        self.setLayout(self.mainLayout)

        self.setCentralWidget(w)

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Токий клиент", "ВМ", "В сети"])
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def tableData(self):
        conn = storage.connect('base.db')
        storage.initialize(conn)
        all_data = storage.all_data(conn)
        rowcount = 0
        for data in all_data:
            rowcount += 1
            self.tableWidget.setRowCount(rowcount)
            self.tableWidget.setItem(rowcount - 1, 0, QTableWidgetItem(data['host_name']))

    def initSignals(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sm = Manager()
    # sm.projectView.show()
    sm.show()

    sys.exit(app.exec_())
