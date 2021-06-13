from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from SearchingSystem import search

class SearchingSystemWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.searchBtn = QPushButton('Search', self)
        self.exitBtn = QPushButton('Exit', self)
        self.lineEdit = QLineEdit(self)
        self.table = QTableWidget(self)
        self.label = QLabel(self)
        self.browser = QWebEngineView()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle('Searching System')

        self.lineEdit.move(50, 50)
        self.lineEdit.resize(485, 30)

        self.searchBtn.move(560, 50)
        self.searchBtn.resize(100, 30)
        self.searchBtn.clicked.connect(self.searchBtnClicked)

        self.exitBtn.move(675, 50)
        self.exitBtn.resize(75, 30)
        self.exitBtn.clicked.connect(self.hide)

        self.label.move(50, 100)
        self.label.resize(700, 30)

        self.table.move(50, 150)
        self.table.resize(700, 400)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['相关度', '题目', '主要匹配内容', 'URL', '日期'])
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 200)
        self.table.setColumnWidth(4, 110)
        self.table.hide()

    def searchBtnClicked(self):
        if self.lineEdit.text() == "":
            self.table.hide()
            msg = QMessageBox()
            msg.warning(self, "", "do not search null", QMessageBox.Yes)
        else:
            statement = self.lineEdit.text()
            spellingCorrectStr, results = search(statement)
            self.label.setText(spellingCorrectStr)
            self.showTable(results)

    def showTable(self, results):
        # 清空上次搜索结果
        rows = self.table.rowCount()
        for row in reversed(range(rows)):
            self.table.removeRow(row)
        for row in range(len(results)):
            item = results[row]
            self.table.insertRow(row)
            for col in range(len(item)):
                item = QTableWidgetItem(str(results[row][col]))
                self.table.setItem(row, col, item)
        self.table.show()
