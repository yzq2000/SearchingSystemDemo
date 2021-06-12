import os
import tools
import LanguageAnalysis

# 创建倒排索引
def create_index():
    files = os.listdir(tools.datapath)
    inverted_index = {}
    for file in files:
        lines = open(tools.datapath + file, "r").readlines()
        for line in lines:
            # wordList = line.split()
            wordList = LanguageAnalysis.lemmatize_sentence(line, True)
            for word in wordList:
                if word not in inverted_index:
                    inverted_index[word] = {file: 1}
                elif file not in inverted_index[word]:
                    inverted_index[word][file] = 1
                else:
                    inverted_index[word][file] += 1
    # print(inverted_index)
    return inverted_index

def get_index():
    # 若已经有倒排索引表了 读取倒排索引表
    if os.path.isfile("index.txt"):
        indexFile = open("index.txt", 'r')
        inverted_index = eval(indexFile.read())
        indexFile.close()
    # 否则创建新的倒排索引表
    else:
        inverted_index = create_index()
        indexFile = open("index.txt", 'w')
        indexFile.write(str(inverted_index))
        indexFile.close()
    return inverted_index


