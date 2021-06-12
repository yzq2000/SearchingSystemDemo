import os
import tools

# Vibrant说以下的注释是copy的
# 创建倒排索引
# 在向量空间模型当中，每一个位置的权重值依赖于文档频率df和文档中词项的频率tf
# 我们要在倒排索引表中记录某一词在某一文档中出现的频率tf
# 最初的思路是把倒排表中的每一项设置为一个二元的tuple
# 然而在python中tuple是immutable的
# 于是我打算把倒排表由list变成一个dictionary，key值为docID，属性值为该term在docID文档中出现的频率tf
def create_index():
    files = os.listdir(tools.reuterspath)
    inverted_index = {}
    for file in files:
        lines = open(tools.reuterspath + file, "r").readlines()
        for line in lines:
            wordList = line.split()
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


