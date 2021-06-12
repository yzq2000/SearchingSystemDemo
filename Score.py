import cmath

def get_wfidf_Score(index, fileNum, doc, wordset):
    score = 0
    mainWords = []
    for word in wordset:
        if word not in index or doc not in index[word]:
            continue
        tf = index[word][doc]
        df = len(index[word])
        wf = 1 + cmath.log10(tf).real
        idf = cmath.log10(fileNum / df).real
        score += wf * idf
        mainWords.append((wf * idf, word))
    mainWords.sort()
    return round(score, 4), mainWords
