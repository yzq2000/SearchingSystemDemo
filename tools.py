# import json
# import os
#
# projectpath = os.getcwd() + "/"
# reuterspath = projectpath.replace("SearchSystem", "Reuters")
#
# def writeToFile(item,filename):
#     # 将数据写入到文件中
#     file = open(filename,'w')
#     str = json.JSONEncoder().encode(item)
#     file.write(str)
#     file.close()
#
# # 获取文档名中的文档的id
# def getDocID(filename):
#     end = filename.find('.')
#     docId = filename[0:end]
#     return int(docId)
#
# def getWholeDocList():
#     files = os.listdir(reuterspath)
#     fileList = []
#     for file in files:
#         fileList.append(getDocID(file))
#     return sorted(fileList)
#
# def getIndex():
#     file = open(projectpath + 'invertIndex.json', 'r')
#     indexStr = file.read()
#     index = json.JSONDecoder().decode(indexStr)
#     return index
#
# def getWordList():
#     file = open(projectpath + 'wordList.json', 'r')
#     wordStr = file.read()
#     wordList = json.JSONDecoder().decode(wordStr)
#     return wordList
#
# print("getting file list...")
# wholeDocList = getWholeDocList()