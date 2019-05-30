import unittest
from src.cantusNlp.utils.FileReader import FileReader
from src.cantusNlp.NlpProcessor import NlpProcessor


nlp = NlpProcessor('','')
fr = FileReader()
projectDir = str(fr.calcPath(__file__).parent.parent.parent)


class Test_readXMl(unittest.TestCase):

    def test_returnsExpectedXml_withExpectedRootTag(self):
        lemma_list: list = ['peter', 'peter', 'peter', 'haus', 'thomas', 'haus', 'frida', 'sigurd']

        result = nlp.analyze_lemma(lemma_list)
        first_entry_count = result[0]['value']
        expected_count = 3

        self.assertEqual(first_entry_count, expected_count)

if __name__ == '__main__':
    unittest.main()
