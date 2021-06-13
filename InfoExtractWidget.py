from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import os
import tools
from InfoExtractSystem import extract

class InfoExtractWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.exitBtn = QPushButton('Exit', self)
        self.extractBtn = QPushButton('Extract', self)
        self.webView = QWebEngineView(self)
        self.comboBox = QComboBox(self)
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle('Information Extraction System')

        self.comboBox.move(50, 50)
        self.comboBox.resize(485, 30)
        self.initComboBox()

        self.extractBtn.move(560, 50)
        self.extractBtn.resize(100, 30)
        self.extractBtn.clicked.connect(self.extractBtnClicked)

        self.exitBtn.move(675, 50)
        self.exitBtn.resize(75, 30)
        self.exitBtn.clicked.connect(self.hide)

        self.webView.move(50, 120)
        self.webView.resize(700, 430)

    def initComboBox(self):
        files = os.listdir(tools.datapath)
        for file in files:
            self.comboBox.addItem(file)

    def extractBtnClicked(self):
        url = tools.datapath + self.comboBox.currentText()
        html = extract(url)
        self.webView.setHtml(html)
