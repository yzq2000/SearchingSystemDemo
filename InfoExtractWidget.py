from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


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

        self.extractBtn.move(560, 50)
        self.extractBtn.resize(100, 30)

        self.exitBtn.move(675, 50)
        self.exitBtn.resize(75, 30)
        self.exitBtn.clicked.connect(self.hide)

        self.webView.move(50, 120)
        self.webView.resize(700, 430)

        self.webView.setHtml('''hiii''')

        self.comboBox.addItem("1")
        self.comboBox.addItem("1")
        self.comboBox.addItem("1")
        self.comboBox.addItem("1")
