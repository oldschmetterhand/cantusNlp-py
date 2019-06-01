import unittest
from src.cantusNlp.utils.FileReader import FileReader
from src.cantusNlp.utils.nlpPhenomena.Lemma import Lemma

fr = FileReader()
projectDir = str(fr.calcPath(__file__).parent.parent.parent.parent)

test_data = {
    "lemma": "Pferd",
    "source": "Pferde",
    "word_position": 21
}


class Test_instantiation(unittest.TestCase):

    def test_instantiation_raises_no_error(self):
        lemma = Lemma(test_data["lemma"], test_data["source"], test_data["word_position"])

    def test_get_source_without_val_raises_error(self):
        lemma = Lemma(test_data["lemma"])
        self.assertRaises(ValueError, lemma.get_source)

    def test_get_word_pos_without_val_raises_error(self):
        lemma = Lemma(test_data["lemma"])
        self.assertRaises(ValueError, lemma.get_word_position)


class Test_return_as_dictionary(unittest.TestCase):

    def test_dictionary_equal_to_read_in_dict(self):
        lemma = Lemma(test_data["lemma"], test_data["source"], test_data["word_position"])
        lemma_dict, key = lemma.return_as_dictionary()
        self.assertDictEqual(test_data, lemma_dict)

    def test_unique_key_is_lemma(self):
        lemma = Lemma(test_data["lemma"], test_data["source"], test_data["word_position"])
        lemma_dict, key = lemma.return_as_dictionary()
        self.assertEquals(test_data["lemma"], lemma_dict["lemma"])


if __name__ == '__main__':
    unittest.main()