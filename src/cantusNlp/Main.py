
from src.cantusNlp.NlpProcessor import NlpProcessor
from src.cantusNlp.utils.FileReader import FileReader
from src.cantusNlp.utils.Lemma import LEMMATA
from src.cantusNlp.utils.CltkOperator import CltkOperator

fr = FileReader()
projDirectory = fr.calcPath(__file__).parent.parent.parent
dataDir = str(projDirectory) + "/resources/cantus/"

# start nlp
nlp = NlpProcessor(dataDir)
nlp.loadCorpus("note")
# nlp.lemmatizeCorpus()

map = nlp.getTextMap()
cltk = CltkOperator()


for key in map:
    text = map[key]
    text = nlp._strRefiner.refineElemTxt(text)
    text = cltk.wtokenizeLatin(text)
    # text = cltk.lemmatizeLat(text)
    text = cltk.removeLatStopWords(text)
    map[key] = text


array = []



for key in LEMMATA:
    key = str.lower(key)
    array.append(key)
    # print(key)


# print(array)

for word in map["TEI_SOURCE.xml"]:

    if word not in array:
        print(word)



# print(map)


# print(nlp.getText("fragment_07.xml"))

# TODO move following code inside NlpPRocessor ...> should not have to loop by hand.

# testprints
# map = nlp.getTextMap()
# print(map)

# aggr = " "
#
# for key in map:
#     curentry = map[key]
#
#     for word in curentry:
#         aggr += word + " "
#
#
#
# print(aggr)