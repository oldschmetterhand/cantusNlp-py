
from src.cantusNlp.NlpProcessor import NlpProcessor
from src.cantusNlp.utils.FileReader import FileReader

# first setting up data and result path for the analysis
fr = FileReader()
projDirectory = fr.calcPath(__file__).parent.parent.parent
dataDir = str(projDirectory) + "/resources/txtData"
resultDir = str(projDirectory) + "/resources/analyzis"

# then start nlp process
nlp = NlpProcessor(dataDir, resultDir)
nlp.loadCorpus("note")
nlp.lemmatizeCorpus(True)
# nlp.lemmatizeCorpus()