import unittest
from src.cantusNlp.utils.FileReader import FileReader
from src.cantusNlp.NlpProcessor import NlpProcessor

fr = FileReader()
projectDir = str(fr.calcPath(__file__).parent.parent.parent)
xmlDir = projectDir + "/resources/sampledata/"
nlp = NlpProcessor(xmlDir)


class Test_loadCorpus(unittest.TestCase):

    def test_assertExpectedFilenames_InMap(self):
        listOfFiles = fr.listFiles(xmlDir)  # using FileReader to get name of files
        nlp.loadCorpus()
        map = nlp.getTextMap()
        for key in map:
            assert key in listOfFiles

