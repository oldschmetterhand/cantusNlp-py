import unittest
import re
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


class test_lemmatizCorpus(unittest.TestCase):

    def test_noDoubleDigits_inLemmatizedTexts(self):
        # explanation: the cltk might include numbers from 1- 9 to differentiate
        # between lemmas
        nlp = NlpProcessor(xmlDir)
        nlp.loadCorpus()
        nlp.lemmatizeCorpus()
        mapi = nlp.getTextMap()
        for key in mapi:
            lemmaList = mapi[key]
            for lemma in lemmaList:
                withoutNumbers = re.search("\d\d+", lemma)  # returns None if no match
                self.assertEqual(None, withoutNumbers)

    def test_noPunctuation_inTexts(self):
        nlp = NlpProcessor(xmlDir)
        nlp.loadCorpus()
        nlp.lemmatizeCorpus()
        mapi = nlp.getTextMap()
        for key in mapi:
            lemmaList = mapi[key]
            for lemma in lemmaList:
                withoutNumbers = re.search("[,;.:]", lemma)  # returns None if no match
                self.assertEqual(None, withoutNumbers)
