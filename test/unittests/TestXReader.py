import unittest
import xml.etree.ElementTree as ElementTree
from src.cantusNlp.utils.XReader import XReader
from src.cantusNlp.utils.FileReader import FileReader

xreader = XReader()
fr = FileReader()
projectDir = str(fr.calcPath(__file__).parent.parent.parent)


class Test_readXMl(unittest.TestCase):

    def test_returnsExpectedXml_withExpectedRootTag(self):
        path = xreader.readXml(projectDir + "/resources/sampledata/fragment_01b.xml")
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
        testXml = ElementTree.parse(projectDir + "/resources/sampledata/fragment_01b.xml")
        exp = "{http://www.tei-c.org/ns/1.0}TEI"
        act = str(xreader.getRootTag(testXml))
        self.assertEqual(exp, act)


class Test_getTeiBodyTag(unittest.TestCase):

    def test_returnsExpectedText_textOfFirstPTaginside_withoutFiltering(self):
        testXml = ElementTree.parse(projectDir + "/resources/sampledata/fragment_01b.xml")
        act = xreader.getTeiBodyText(testXml)
        exp = "[Et tu Domine Deus] virtutum, Deus Israel. Intende ad visitandas omnes gentes," \
              + " non miserearis omnibus qui operantur iniquitatem."
        self.assertTrue(exp in act)

    def test_textOfLastPinside_withoutFiltering(self):
        testXml = ElementTree.parse(projectDir + "/resources/sampledata/fragment_01b.xml")
        act = xreader.getTeiBodyText(testXml)
        exp = "in consumatione, in ira consumationis et non erunt. Et scient quia Deus dominabitur [Iacob]"
        self.assertTrue(exp in act)

    def test_contentFromSuppliedElem_notInside_whenFilterParamGiven(self):
        testXml = ElementTree.parse(projectDir + "/resources/sampledata/fragment_01b.xml")
        str = xreader.getTeiBodyText(testXml, "supplied")
        isInside = "[Et tu Domine Deus]" in str
        self.assertFalse(isInside)

    def test_anotherContentFrom_suppliedTag_notInside_whenFilterParamGiven(self):
        testXml = ElementTree.parse(projectDir + "/resources/sampledata/fragment_08.xml")
        str = xreader.getTeiBodyText(testXml, "supplied")
        isInside = "[iungitur, reus]" in str
        self.assertFalse(isInside)


class Test_emptyElem(unittest.TestCase):

    def test_filteredElem_notInside(self):

        testXml = ElementTree.parse(projectDir + "/resources/sampledata/fragment_08.xml")
        root: ElementTree = testXml.getroot()
        body: ElementTree.Element = root.find(".//{http://www.tei-c.org/ns/1.0}body")

        # remove <supplied> element
        body = xreader._emptyElem(body, "supplied")

        # aggregate string.
        aggrStr = ""
        for txt in body.itertext():
            aggrStr += txt

        testStr = "iungitur"  # should not be in aggrStr
        isInside: bool = testStr in aggrStr

        self.assertFalse(isInside)

    def test_ifMethod_notCalled_valOfSuppliedTag_isStillInside(self):

        testXml = ElementTree.parse(projectDir + "/resources/sampledata/fragment_08.xml")
        root: ElementTree = testXml.getroot()
        body: ElementTree.Element = root.find(".//{http://www.tei-c.org/ns/1.0}body")

        # aggregate string.
        aggrStr = ""
        for txt in body.itertext():
            aggrStr += txt

        testStr = "iungitur"  # should be in aggrStr (only once in sample data)
        isInside: bool = testStr in aggrStr

        self.assertTrue(isInside)

if __name__ == '__main__':
    unittest.main()
