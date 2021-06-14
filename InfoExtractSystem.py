from spacy import displacy
import re
import en_core_web_sm
import en_core_web_md
import en_core_web_lg
from bs4 import BeautifulSoup

smallNLP = en_core_web_sm.load()
middleNLP = en_core_web_md.load()
largeNLP = en_core_web_lg.load()

def extract(url, model):
    file = open(url).read()
    soup = BeautifulSoup(file, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    ny_bb = " ".join(re.split(r'[\n\t]+', soup.get_text()))
    if model == "small model":
        smallArticle = smallNLP(ny_bb)
        return displacy.render(smallArticle, jupyter=False, style='ent')
    elif model == "middle model":
        middleArticle = middleNLP(ny_bb)
        return displacy.render(middleArticle, jupyter=False, style='ent')
    else:
        largeArticle = largeNLP(ny_bb)
        return displacy.render(largeArticle, jupyter=False, style='ent')
