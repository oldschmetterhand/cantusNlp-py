import xml.etree.ElementTree as ElementTree


class XReader:
    etree = ElementTree.ElementTree()

    def __init__class(self):
        print("instantiating class")

    def readXml(self, path: str):
        """"
        Reads in given xml via using the etree library.

        :param path: String of the path to the specific XML document.
        :returns: ElementTree representation of the read in XML.
        """
        return ElementTree.parse(path)

    def getRootTag(self, xTree: object):
        """
        Reads given xml (see param), accesses the root element
        and calcs the it's tagname.
        :param xTree: ElementTree instance of the XML. (from etree library)
        :return: string value of the root-tag
        """

        rootTag: str = xTree.getroot().tag
        return rootTag

    def getTeiBodyText(self, xTree: object):
        root: object = xTree.getroot()
        teiBody = root.findall(".//{http://www.tei-c.org/ns/1.0}body//*")

        concatStr: str = ''
        for elem in teiBody:
            if elem.text is not None:
                concatStr += elem.text

        concatStr = self._stripElemTxt(concatStr)
        return concatStr

    def _stripElemTxt(self, txt: str):
        txt = txt.replace("\n", "")
        txt = txt.replace("\t", "")
        txt = txt.strip()
        txt = txt.replace("  ", "")  # remove duplicated space
        txt = self._delEditorMarks(txt)
        return txt

    def _delEditorMarks(self, txt: str):
        txt = txt.replace("[", "")
        txt = txt.replace("]", "")  # quite specific for my current project(maybe not good here)
        return txt


# # TestCalls from here
# reader = XReader()
# xml = reader.readXml("fragment_1a.xml")
# print(xml)
#
# #getRoot elem and print one childElemsText
# root = reader.getRoot(xml)
# print(root[0][1].text)



# looping through tags
#allNodes = root.iter()

#tree = ElementTree.parse('test01.xml')
#print(ElementTree.tostring(tree, encoding='utf-8', method='text'))


