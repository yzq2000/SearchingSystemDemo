import cmath

# def get_tfidf(index, fileNum , docID, word) :
#     docID = str(docID)
#     if docID not in index[word]:
#         return "0"
#     tf = len(index[word][docID])
#     df = len(index[word])
#     idf = cmath.log10(fileNum / df).real
#     return tf * idf
#
# def get_wfidf(index, fileNum, docID, word):
#     docID = str(docID)
#     if docID not in index[word]:
#         return "0"
#     tf = len(index[word][docID])
#     df = len(index[word])
#     wf = 1 + cmath.log10(tf).real
#     idf = cmath.log10(fileNum / df).real
#     return wf * idf

def get_wfidf_Score(index, fileNum, doc, wordset):
    score = 0
    mainWords = []
    for word in wordset:
        if word not in index or doc not in index[word]:
            continue
        tf = index[word][doc]
        df = len(index[word])
        # df = 0
        # for val in dict(index[word]).values():
        #     df += val
        wf = 1 + cmath.log10(tf).real
        idf = cmath.log10(fileNum / df).real
        score += wf * idf
        mainWords.append((wf * idf, word))
    mainWords.sort()
    return round(score, 4), mainWords
#
# def get_tfidf_Score(index,fileNum,docID,wordList):
#     score = 0
#     docID = str(docID)
#
#     for word in wordList:
#
#         if word not in index or docID not in index[word]:
#             continue
#         tf = len(index[word][docID])
#         df = len(index[word])
#         idf = cmath.log10(fileNum / df).real
#         # print("filenum / df",fileNum / df, "df: ",df, " idf: ", idf )
#         score += tf * idf
#     return score
