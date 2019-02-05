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

    def test_canFilterSpecificElem_valOfSuppliedTag_notInSampleData(self):
        # ignore textVal of given tag.
        nlp.loadCorpus("supplied")
        map = nlp.getTextMap()
        txt = map.get("fragment_08.xml")

        testStr: str = "iungitur"  # expected in <supplied> here (but filtered before)
        isInside: bool = testStr in txt

        self.assertFalse(isInside)


    def test_alsoSupports_txtFiles(self):

        txt_data_dir = str(projectDir) + "/resources/txtData/"
        processor = NlpProcessor(txt_data_dir)
        processor.loadCorpus()
        txt = processor.getText("txt.txt")
        is_inside = "In primo nocturno In omnem terram" in txt
        self.assertTrue(is_inside)



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
