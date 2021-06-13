from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.searchBtn = QPushButton('search', self)
        self.extractBtn = QPushButton('extract', self)
        self.titleLabel = QLabel(self)
        self.toothableLabel = QLabel(self)
        self.vibrantLabel = QLabel(self)
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle('Searching & Information Extraction System')

        self.titleLabel.move(50, 100)
        self.titleLabel.resize(700, 150)
        self.titleLabel.setText("信息知识与获取")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(QFont("Arial", 48))

        self.toothableLabel.move(50, 300)
        self.toothableLabel.resize(700, 50)
        self.toothableLabel.setText("2018211305班    2018211296    王淇森")
        self.toothableLabel.setAlignment(Qt.AlignCenter)
        self.toothableLabel.setFont(QFont("Arial", 18))

        self.vibrantLabel.move(50, 350)
        self.vibrantLabel.resize(700, 50)
        self.vibrantLabel.setText("2018211301班    2018211540    杨竹芩")
        self.vibrantLabel.setAlignment(Qt.AlignCenter)
        self.vibrantLabel.setFont(QFont("Arial", 18))

        self.searchBtn.move(100, 500)
        self.searchBtn.resize(200, 50)

        self.extractBtn.move(500, 500)
        self.extractBtn.resize(200, 50)
