import queue
import tools
import os
import LanguageAnalysis
import Score
import Index

def getScoreDocList(index, fileNum, words, docList):
    scoreDocList = []
    for doc in docList:
        score, mainWords = Score.get_wfidf_Score(index, fileNum, doc, words)
        cnt = 0
        mainWordsString = ""
        for (s, word) in mainWords:
            mainWordsString += word + " "
            cnt += 1
            if cnt == 10:
                break
        url = "data/" + doc
        scoreDocList.append([score, doc, mainWordsString, url, tools.TimeStampToTime(os.path.getctime(url))])
    return scoreDocList

# 从大到小得到sortedDocList
def sortScoreDocList(index, fileNum, words, docList):
    scoreDocList = getScoreDocList(index, fileNum, words, docList)
    return sorted(scoreDocList, reverse=True)

def searchOneWord(index, word):
    if word not in index:
        return []
    else:
        docList = [key for key in index[word].keys()]
        # 将文档的id排序
        docList.sort()
        return docList

# 将所有word的结果取并，即所有包含这些word的文档
def searchWords(index, words):
    if len(words) == 0:
        return []
    docQueue = queue.Queue()
    for word in words:
        docQueue.put(searchOneWord(index, word))

    while docQueue.qsize() > 1:
        list1 = docQueue.get()
        list2 = docQueue.get()
        docQueue.put(tools.mergeTwoList(list1, list2))

    docList = docQueue.get()
    return docList


def search(statement):
    # stemming
    inputWords = LanguageAnalysis.lemmatize_sentence(statement, True)
    # correct spelling
    inputWords = LanguageAnalysis.correctSentence(inputWords)
    wordSet = set(inputWords)

    # 数据集改变后需要删除index.txt重新生成
    index = Index.get_index()
    files = os.listdir(tools.datapath)
    fileNum = len(files)

    docList = searchWords(index, wordSet)
    sortedDocList = sortScoreDocList(index, fileNum, wordSet, docList)
    for doc in sortedDocList:
        print("doc ID: ", doc[1], " score: ", "%.4f" % doc[0])

    spellingCorrectStr = "猜您想搜：" + " ".join(inputWords)
    return spellingCorrectStr, sortedDocList
