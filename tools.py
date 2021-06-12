import os
from collections import Counter
import time

projectpath = os.getcwd() + "/"
reuterspath = projectpath + "data/"

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

def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)
