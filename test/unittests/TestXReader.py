import unittest
import xml.etree.ElementTree as ElementTree
from src.cantusNlp.utils.XReader import XReader
from src.cantusNlp.utils.FileReader import FileReader

xreader = XReader()
fr = FileReader()
projectDir = str(fr.calcPath(__file__).parent.parent.parent)


class Test_readXMl(unittest.TestCase):

    def test_returnsExpectedXml_withExpectedRootTag(self):
        path = xreader.readXml(projectDir + "/resources/sampledata/fragment_1b.xml")
        # namespace needs to be given
        exp = "{http://www.tei-c.org/ns/1.0}TEI"
        act = str(path.getroot().tag)
        self.assertEqual(exp, act)

    def test_throwsValueError_IfPathString_notContainsXmlFileName(self):
        wrongFile = "XYZ.json"
        self.assertRaises(ValueError, xreader.readXml, wrongFile)


    def test_throwsValueError_justDirGiven_asPath(self):
        wrongDir = "../unittests/"
        self.assertRaises(ValueError, xreader.readXml, wrongDir)


class Test_getRootTag(unittest.TestCase):

    def test_returnsExpectedRoot_ofGivenXml(self):
        testXml = ElementTree.parse(projectDir + "/resources/sampledata/fragment_1b.xml")
        exp = "{http://www.tei-c.org/ns/1.0}TEI"
        act = str(xreader.getRootTag(testXml))
        self.assertEqual(exp, act)



if __name__ == '__main__':
    unittest.main()