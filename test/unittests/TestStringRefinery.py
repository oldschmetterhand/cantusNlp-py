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

    def test_pollutedStringWith_numbers_escapes_whitespace(self):
        sample = "  I'm my neighbour 1233 high     312       rabbit      []          \n\n \t            bambus \n           934917394123        "
        exp = "I'm my neighbour high rabbit bambus"
        act = strRefiner.refineElemTxt(sample)
        self.assertEqual(exp, act)

    def test_cleansPollutedString_withNumbersPunctuation_whitespaceParenthesis(self):
        sample = "  I'm my neighbour 1233 high     312       rabbit      []          \n\n \t   bambus \n           934917394123       :;:::;;,.,.,;"
        exp= "I'm my neighbour high rabbit bambus"
        act = strRefiner.refineElemTxt(sample)
        self.assertEqual(exp, act)

class Test_replaceNumbs(unittest.TestCase):

    def test_replacesNumberInGivenString_throughOneWhitespace(self):
        sample = "eel 8987 codfish"
        exp = "eel   codfish"
        act = strRefiner.replNumbers(sample)
        self.assertEqual(exp, act)

    def test_resplacesNumberWithWhitespace_inStringWithManyNumbers(self):
        sample = "eel8987codfish902138123parrot11111231244214124124141244124"
        exp = "eel codfish parrot "
        act = strRefiner.replNumbers(sample)
        self.assertEqual(exp, act)


class Test_replEditorMarks(unittest.TestCase):

    def test_correctRemovalOfParenthesis(self):
        sample = "[]banana[]"
        exp = "  banana  "  # no whitespace removal in the method
        act = strRefiner.replEditorMarks(sample)
        self.assertEqual(exp, act)


class Test_replPunctuation(unittest.TestCase):

    def test_punctuationReplaced_throughWhitespace(self):
        sample = ".,banana:;"
        exp = "  banana  "  # no whitespace removal in the method
        act = strRefiner.replPunctuation(sample)
        self.assertEqual(exp, act)

    def test_replacePunctuation_inHeavyPollutedString(self):
        sample="...perch:;."
        exp = "   perch   "
        act = strRefiner.replPunctuation(sample)
        self.assertEqual(exp, act)