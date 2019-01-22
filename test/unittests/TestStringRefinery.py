import unittest
from src.cantusNlp.utils.FileReader import FileReader
from src.cantusNlp.utils.StringRefinery import StringRefinery
import pathlib

curDir = pathlib.Path(__file__).parent
curDir = str(curDir)
fr = FileReader(curDir)
strRefiner = StringRefinery()

class Test_refineElemText(unittest.TestCase):

    def test_removesWhitespace_fromSampleInput(self):
        sample = "            rabbit         perch             "
        exp = "rabbit perch"
        act = strRefiner.refineElemTxt(sample)
        self.assertEqual(act, exp)

