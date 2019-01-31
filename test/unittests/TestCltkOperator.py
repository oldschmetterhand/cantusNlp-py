import unittest
from src.cantusNlp.utils.FileReader import FileReader
import pathlib
from src.cantusNlp.utils.CltkOperator import CltkOperator


curDir = pathlib.Path(__file__).parent
curDir = str(curDir)
fr = FileReader(curDir)


class TestDisplaySuspiciousWords(unittest.TestCase):

    def tests_blaa(self):
        cltk = CltkOperator()
        cltk.displaySuspiciousWords()