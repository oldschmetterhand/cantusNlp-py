
import xml.etree.ElementTree as ElementTree



class XReader:
    etree = ElementTree.ElementTree()

    def __init__class(self):
        print("instantiating class")

    def readXml(self, path):
        return ElementTree.parse(path)

    def getRoot(self, xml):
        return xml.getroot()


# TestCalls from here
reader = XReader()
xml = reader.readXml("test01.xml")
print(xml)

root = reader.getRoot(xml)
print(root[0][1].text)

# looping through tags
allNodes = root.iter()

tree = ElementTree.parse('test01.xml')
print(ElementTree.tostring(tree, encoding='utf-8', method='text'))
