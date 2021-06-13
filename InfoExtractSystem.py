from spacy import displacy
import re
import en_core_web_sm
from bs4 import BeautifulSoup

nlp = en_core_web_sm.load()

def extract(url):
    file = open(url).read()
    soup = BeautifulSoup(file, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    ny_bb = " ".join(re.split(r'[\n\t]+', soup.get_text()))
    article = nlp(ny_bb)
    return displacy.render(article, jupyter=False, style='ent')