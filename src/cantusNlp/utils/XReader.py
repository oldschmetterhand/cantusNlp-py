import xml.etree.ElementTree as ElementTree

class XReader:

    def __init__class(self):
        print("")

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
        """
        Uses Element.itertext() on the body element of given TEI file. Then retrieves
        the text and concatinates it to one string WITHOUT string refining. (=whitespaces
        etc. will be included if in given file.)
        :param xTree: The xml-file parsed as ElementTree (etree library)
        :return: concatStr: The concatenated text WITHOUT normalization / stripping etc.
        = As it is in the file.
        """
        root: ElementTree.Element = xTree.getroot()
        body: ElementTree.Element = root.find(".//{http://www.tei-c.org/ns/1.0}body")

        # needs to be done that way ...> if accessing mulitple
        # elems via xpath and then looping through elem's and their
        # texts ...> problem at elems with text AND other elems nested
        # inside. Going around that bug via .itertext().
        concatStr = ""
        for txt in body.itertext():
            concatStr += txt

        return concatStr

    def _filterElem(self):
        print("implement!")
