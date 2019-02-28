
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
nlp.doTheMagic()
# nlp.lemmatizeCorpus()

# map = nlp.getTextMap()
# cltk = CltkOperator()
#
# lemmas = []
# lemmas_with_source = []
# text = []
# for key in map:
#     text = map[key]
#     text = nlp._strRefiner.refineElemTxt(text)
#     text, removed = cltk.wtokenizeLatin(text, True)
#     text = cltk.removeLatStopWords(text)
#     text, lemmas_with_source = cltk.lemmatizeLat(text, True)
#     map[key] = text

# print(removed)
# not_matched, percentage_not_matched = cltk.analyzeCltkLemmaDeviation(map["txt.txt"]) # called on plain tokenized words

# print(str(percentage_not_matched) + "%")
# print(not_matched)
# print(map["txt.txt"])

# aggregStr = nlp.aggregateWordlist(map["txt.txt"])
# print(aggregStr)

# print(map["txt.txt"])
# print(lemmas_with_source)

# size = []
# for lemma in lemmas_with_source:
#     if ("1" or "2" or "3") in lemma:
#         size.append(lemma)
#         # print(lemma)
#
# print(len(size))
#
# size = set(size)
#
# print(len(size))
# print(size)