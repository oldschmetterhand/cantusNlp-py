import unittest
from src.cantusNlp.utils.FileReader import FileReader
from src.cantusNlp.utils.NlpResult import NlpResult
from src.cantusNlp.utils.nlpPhenomena.Lemma import Lemma

fr = FileReader()
projectDir = str(fr.calcPath(__file__).parent.parent.parent)

mock_lemma01 = Lemma("Pferd", "Pferde", 21)
mock_lemma02 = Lemma("Haus", "Häuser", 22)

mock_lemma_list = [mock_lemma01, mock_lemma02]


class Test_instantiation(unittest.TestCase):

    def test_smoke_instantiation(self):
        res = NlpResult(mock_lemma_list)



class Test_return_array_of_lemma_dicts(unittest.TestCase):

    def test_returned_array_has_length_of_2(self):
        res = res = NlpResult(mock_lemma_list)
        act_length = len(res.return_array_of_lemmas_dicts())
        exp_length = 2
        self.assertEquals(exp_length, act_length)

        print(res.return_array_of_lemmas_dicts())