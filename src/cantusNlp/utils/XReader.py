import xml.etree.ElementTree as ElementTree


class XReader:

    def __init__class(self):
        print("instantiating class")

    def readXml(self, path: str):
        """"
        Reads in given xml via using the etree library.
        :param path: String of the path to the specific XML document.
        :returns: ElementTree representation of the read in XML.
        """

        if ".xml" not in path:
            raise ValueError("No '.xml' found in given parameter: " + path + ". This methods only applies to xml")

        return ElementTree.parse(path)

    def getRootTag(self, xTree: ElementTree):
        """
        Reads given xml (see param), accesses the root element
        and calcs the it's tagname.
        :param xTree: ElementTree instance of the XML. (from etree library)
        :return: string value of the root-tag
        """

        rootTag: str = xTree.getroot().tag
        return rootTag

    def getTeiBodyText(self, xTree: ElementTree):
        root: object = xTree.getroot()
        teiBody = root.findall(".//{http://www.tei-c.org/ns/1.0}body//*")

        concatStr: str = ''
        for elem in teiBody:
            if elem.text is not None:
                concatStr += elem.text

        return concatStr
