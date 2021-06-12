import sys
import nltk

from PyQt5.QtWidgets import *
from Widget import SearchingSystemWidget

def init():
    # 下载需要的依赖文件
    nltk.download("wordnet")
    nltk.download("averaged_perceptron_tagger")
    nltk.download("punkt")
    nltk.download("maxnet_treebank_pos_tagger")


if __name__ == '__main__':
    init()
    app = QApplication(sys.argv)
    ex = SearchingSystemWidget()
    sys.exit(app.exec_())
