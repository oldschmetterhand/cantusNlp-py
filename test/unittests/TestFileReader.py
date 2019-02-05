import unittest
from src.cantusNlp.utils.FileReader import FileReader
import pathlib

curDir = pathlib.Path(__file__).parent
curDir = str(curDir)
fr = FileReader(curDir)


class TestPathGetter(unittest.TestCase):

    def test_returnValue(self):
        act = fr.getPath()
        print(act)
        self.assertEqual(curDir, act)


class TestListFiles(unittest.TestCase):

    def test_currentScript_inCurDir(self):
        fileList = fr.listFiles()
        expFileName = pathlib.Path(__file__).name
        # expecting only one file
        actFileName = fileList[1]
        self.assertEqual(expFileName, actFileName)

    def test_overwriteDefaultValue_withNonsense(self):
        # no list type will be returned because of error.
        self.assertRaises(TypeError, fr.listFiles(), "/bla/bla")


class Test_calcMyPath(unittest.TestCase):

    def test_fromReturn_rightFileName_detectable(self):
        act = fr.calcPath(__file__).name
        exp = "TestFileReader.py"
        self.assertEqual(exp, act)


class Test_readTxt(unittest.TestCase):

    def test_expectedStringIn_readInTxt(self):
        reader = FileReader()
        filePath = pathlib.Path(__file__).parent.parent.parent
        filePath = str(filePath) + "/resources/txtData/txt.txt"
        txt = reader.readTxt(filePath)
        expInside = "iuxta quod et sanctus Gregorius in sacramentario et in graduali libro aliquotiens"
        isInside = expInside in txt
        self.assertTrue(isInside)

if __name__ == '__main__':
    unittest.main()
