import unittest
from src.cantusNlp.utils.FileReader import FileReader
from src.cantusNlp.utils.NlpResult import NlpResult
from src.cantusNlp.utils.nlpPhenomena.Lemma import Lemma

fr = FileReader()
projectDir = str(fr.calcPath(__file__).parent.parent.parent)

mock_lemma01 = Lemma("Pferd", "Pferde", 21)
mock_lemma02 = Lemma("Haus", "Häuser", 22)
mock_lemma_list = [mock_lemma01, mock_lemma02]

mock_cltk_lemma_list = ["Pferd/Pferde", "Haus/Häuser", "Flamingo/Flamingos"]

class Test_instantiation(unittest.TestCase):

    def test_smoke_instantiation(self):
        res = NlpResult(mock_lemma_list)



class Test_return_array_of_lemma_dicts(unittest.TestCase):

    def test_returned_array_has_length_of_2(self):
        res = NlpResult(mock_lemma_list)
        act_length = len(res.return_array_of_lemmas_dicts())
        exp_length = 2
        self.assertEquals(exp_length, act_length)

    def test_throws_when_list_empty(self):
        res = NlpResult()
        self.assertRaises(ValueError, res.return_array_of_lemmas_dicts)


class Test_add_cltk_lemma_list(unittest.TestCase):

    def test_lemma_list_has_expected_length(self):
        res = NlpResult()
        res.add_cltk_lemma_list(mock_cltk_lemma_list)

        act_length = len(res.get_list_of_lemma())
        exp_length = 3

        self.assertEquals(act_length, exp_length)