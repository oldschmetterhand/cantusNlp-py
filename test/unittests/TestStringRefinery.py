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


    def test_cleansPollutedString_withoutNumbers(self):
        sample = "              rabbit      []          \n\n \t             bambus \n                   "
        exp = "rabbit bambus"
        act = strRefiner.refineElemTxt(sample)
        self.assertEqual(exp, act)

    def test_removesArabicNumbers(self):
        sample = "          parrot99999dog91812338luce  "
        exp = "parrot dog luce"
        act = strRefiner.refineElemTxt(sample)
        self.assertEqual(exp, act)

    def test_cleansHighlyPollutedString_withNumbers(self):
        sample = "  2     312       rabbit      []          \n\n \t            bambus \n           934917394123        "
        exp = "rabbit bambus"
        act = strRefiner.refineElemTxt(sample)
        self.assertEqual(exp, act)
