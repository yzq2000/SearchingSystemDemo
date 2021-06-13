import sys
import nltk
from PyQt5.QtWidgets import *
from SearchingSystemWidget import SearchingSystemWidget
from InfoExtractWidget import InfoExtractWidget
from MainWidget import MainWidget

def init():
    # 下载需要的依赖文件
    nltk.download("wordnet")
    nltk.download("averaged_perceptron_tagger")
    nltk.download("punkt")
    nltk.download("maxnet_treebank_pos_tagger")


if __name__ == '__main__':
    init()
    app = QApplication(sys.argv)
    mainWidget = MainWidget()
    searchWidget = SearchingSystemWidget()
    extractWidget = InfoExtractWidget()
    mainWidget.show()
    mainWidget.searchBtn.clicked.connect(searchWidget.show)
    mainWidget.extractBtn.clicked.connect(extractWidget.show)
    sys.exit(app.exec_())