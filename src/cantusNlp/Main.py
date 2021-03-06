
from src.cantusNlp.NlpProcessor import NlpProcessor
from src.cantusNlp.utils.FileReader import FileReader

# first setting up data and result path for the analysis
fr = FileReader()
projDirectory = fr.calcPath(__file__).parent.parent.parent
dataDir = str(projDirectory) + "/resources/try_01"
resultDir = str(projDirectory) + "/resources/analyzis"

# then start nlp process
nlp = NlpProcessor(dataDir, resultDir)
nlp.loadCorpus()
nlp.lemmatizeCorpus(True)

nlp.create_voyant_output()
nlp.output_lemmatization_result()
nlp.analyse_lemma_occurence(100, True)
