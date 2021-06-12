import json
import os
from collections import Counter

projectpath = os.getcwd() + "/"
reuterspath = projectpath + "data/"

def writeToFile(item,filename):
    # 将数据写入到文件中
    file = open(filename,'w')
    str = json.JSONEncoder().encode(item)
    file.write(str)
    file.close()

# 获取文档名中的文档的id
def getDocID(filename):
    end = filename.find('.')
    docId = filename[0:end]
    return int(docId)

def getWholeDocList():
    files = os.listdir(reuterspath)
    fileList = []
    for file in files:
        fileList.append(getDocID(file))
    return sorted(fileList)

def getWordList():
    file = open(projectpath + 'wordList.json', 'r')
    wordStr = file.read()
    wordList = json.JSONDecoder().decode(wordStr)
    # print(wordList)
    return wordList

def getWords():
    files = os.listdir(reuterspath)
    words = Counter()
    for file in files:
        lines = open(reuterspath + file, "r").readlines()
        for line in lines:
            wordList = line.split()
            newWords = Counter(wordList)
            words += newWords
    # print(words)
    return words

def mergeTwoList(list1, list2):
    rlist = []
    len1 = len(list1)
    len2 = len(list2)
    n1 = 0
    n2 = 0
    while n1 < len1 and n2 < len2:
        if list1[n1] < list2[n2]:
            rlist.append(list1[n1])
            n1 += 1
        elif list1[n1] > list2[n2]:
            rlist.append(list2[n2])
            n2 += 1
        else:
            rlist.append(list1[n1])
            n1 += 1
            n2 += 1

    if n1 < len1:
        rlist.extend(list1[n1: len1])
    if n2 < len2:
        rlist.extend(list2[n2: len2])
    return rlist


print("getting file list...")
wholeDocList = getWholeDocList()