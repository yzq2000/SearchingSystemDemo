from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
import tools

# stemming

deleteSignal = [',', '.', ';', '&', ':', '>', "'", '`', '(', ')', '+', '!', '*', '"', '?']
deleteSignalForInput = [',', '.', ';', '&', ':', '>', "'", '`', '+', '!', '*', '"', '?']

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def getWord(word):
    if word.istitle():
        word = word.lower()
        word = WordNetLemmatizer().lemmatize(word, pos='n')
    else:
        word = WordNetLemmatizer().lemmatize(word, pos='n')
    return word

def lemmatize_sentence(sentence, forinput):
    res = []
    result = []
    lemmatizer = WordNetLemmatizer()
    for word, pos in pos_tag(word_tokenize(sentence)):
        wordnet_pos = get_wordnet_pos(pos) or wordnet.NOUN
        res.append(lemmatizer.lemmatize(word, pos=wordnet_pos))
    for word in res:
        # 如果是 's什么的，直接排除
        if word[0] == '\'':
            continue
        # 去除标点符号
        if not forinput:
            for c in deleteSignal:
                word = word.replace(c, '')
        else:
            for c in deleteSignalForInput:
                word = word.replace(c, '')
        # 排除空的字符串
        if len(word) == 0 or word[0] == '-':
            continue
        # 如果分解的单词中有/,则将其中的每个单词添加到结果中
        if word.find('/') > 0:
            rs = word.split('/')
            for w in rs:
                w = getWord(w)
                result.append(w)
        else:
            word = getWord(word)
            result.append(word)
    return result


# spell

WORDS = tools.getWords()

# The subset of `words` that appear in the dictionary of WORDS.
def known(words):
    return set(w for w in words if w in WORDS)

# All edits that are one edit away from `word`.
def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

# All edits that are two edits away from `word`.
def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

# Generate possible spelling corrections for word.
def candidates(word):
    return known([word]) or known(edits1(word)) or known(edits2(word)) or [word]

# Probability of `word`.
def P(word, N=sum(WORDS.values())):
    return WORDS[word] / N

# Most probable spelling correction for word.
def correction(word):
    return max(candidates(word), key=P)

def correctSentence(wordList):
    res = []
    for word in wordList:
        if word == '(' or word == ')':
            res.append(word)
        else:
            res.append(correction(word))
    return res
