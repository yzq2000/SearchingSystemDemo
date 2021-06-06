from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from SearchingSystem import search


class SearchingSystemWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Search', self)
        self.lineEdit = QLineEdit(self)
        self.table = QTableWidget(self)
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle('SearchingSystem')

        self.lineEdit.move(50, 50)
        self.lineEdit.resize(550, 30)

        self.btn.move(650, 50)
        self.btn.resize(100, 30)
        self.btn.clicked.connect(self.searchBtnClicked)

        self.table.move(50, 120)
        self.table.resize(700, 430)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['相关度', '题目', '主要匹配内容', 'URL', '日期', '准确率'])
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 200)
        self.table.setColumnWidth(4, 60)
        self.table.setColumnWidth(5, 50)
        self.table.hide()

        self.show()

    def searchBtnClicked(self):
        if self.lineEdit.text() == "":
            self.table.hide()
            msg = QMessageBox()
            msg.warning(self, "", "do not search null", QMessageBox.Yes)
        else:
            statement = self.lineEdit.text()
            results = search(statement)
            self.showTable(results)

    def showTable(self, results):
        for row in range(len(results)):
            item = results[row]
            self.table.insertRow(row)
            for col in range(len(item)):
                item = QTableWidgetItem(str(results[row][col]))
                self.table.setItem(row, col, item)
        self.table.show()


