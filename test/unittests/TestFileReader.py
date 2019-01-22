import unittest
from src.cantusNlp.utils.FileReader import FileReader
import pathlib

curDir = pathlib.Path(__file__).parent
fr = FileReader(curDir)


class TestPathGetter(unittest.TestCase):

    def test_returnValue(self):
        act = fr.getPath()
        self.assertEqual(act, curDir)


class TestListFiles(unittest.TestCase):

    def test_currentScript_inCurDir(self):
        fileList = fr.listFiles()
        expFileName = pathlib.Path(__file__).name
        # expecting only one file
        actFileName = fileList[0]
        self.assertEqual(expFileName, actFileName)

    def test_overwriteDefaultValue_withNonsense(self):
        # no list type will be returned because of error.
        self.assertRaises(TypeError, fr.listFiles(), "/bla/bla")


class Test_calcMyPath(unittest.TestCase):

    def test_fromReturn_rightFileName_detectable(self):
        act = fr.calcPath(__file__).name
        exp = "TestFileReader.py"
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()
