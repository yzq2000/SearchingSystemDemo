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
        self.fileComboBox = QComboBox(self)
        self.nlpComboBox = QComboBox(self)
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle('Information Extraction System')

        self.fileComboBox.move(50, 50)
        self.fileComboBox.resize(300, 30)
        self.initFileComboBox()

        self.nlpComboBox.move(385, 50)
        self.nlpComboBox.resize(150, 30)
        self.initNlpComboBox()

        self.extractBtn.move(560, 50)
        self.extractBtn.resize(100, 30)
        self.extractBtn.clicked.connect(self.extractBtnClicked)

        self.exitBtn.move(675, 50)
        self.exitBtn.resize(75, 30)
        self.exitBtn.clicked.connect(self.hide)

        self.webView.move(50, 120)
        self.webView.resize(700, 430)

    def initFileComboBox(self):
        files = os.listdir(tools.datapath)
        for file in files:
            self.fileComboBox.addItem(file)

    def initNlpComboBox(self):
        self.nlpComboBox.addItem("small model")
        self.nlpComboBox.addItem("middle model")
        self.nlpComboBox.addItem("large model")

    def extractBtnClicked(self):
        url = tools.datapath + self.fileComboBox.currentText()
        model = self.nlpComboBox.currentText()
        html = extract(url, model)
        self.webView.setHtml(html)
