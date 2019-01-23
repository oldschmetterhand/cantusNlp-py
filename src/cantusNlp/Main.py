
from src.cantusNlp.NlpProcessor import NlpProcessor
from src.cantusNlp.utils.FileReader import FileReader

fr = FileReader()
projDirectory = fr.calcPath(__file__).parent.parent.parent
dataDir = str(projDirectory) + "/resources/sampledata/"

# start nlp
nlp = NlpProcessor(dataDir)
nlp.loadCorpus()
nlp.lemmatizeCorpus()






# testprints
map = nlp.getTextMap()
print(map)


aggr = ""

for key in map:
    curentry = map[key]

    for word in curentry:
        aggr += word + " "



print(aggr)