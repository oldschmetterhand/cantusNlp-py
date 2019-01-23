import unittest
from src.cantusNlp.utils.FileReader import FileReader

fr = FileReader()
projectDir = str(fr.calcPath(__file__).parent.parent.parent)


class Test_retrieveLatinModels(unittest.TestCase):

    def checkIfModels_areStored_inLb(self):
        print("implement!")
        self.assertTrue(False)


