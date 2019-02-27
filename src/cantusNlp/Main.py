
from src.cantusNlp.NlpProcessor import NlpProcessor
from src.cantusNlp.utils.FileReader import FileReader
from src.cantusNlp.utils.Lemma import LEMMATA
from src.cantusNlp.utils.CltkOperator import CltkOperator

fr = FileReader()
projDirectory = fr.calcPath(__file__).parent.parent.parent
dataDir = str(projDirectory) + "/resources/txtData/"

# start nlp
nlp = NlpProcessor(dataDir)
nlp.loadCorpus("note")
# nlp.lemmatizeCorpus()

map = nlp.getTextMap()
cltk = CltkOperator()


for key in map:
    text = map[key]
    text = nlp._strRefiner.refineElemTxt(text)
    text, removed = cltk.wtokenizeLatin(text, True)
    # text = cltk.lemmatizeLat(text)
    # text = cltk.removeLatStopWords(text)
    map[key] = text

print(removed)
#cltk.displayCltkLemmaDeviation(map["txt.txt"])

aggregStr = nlp.aggregateWordlist(map["txt.txt"])
print(aggregStr)