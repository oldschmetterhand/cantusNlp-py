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

#getRoot elem and print one childElemsText
root = reader.getRoot(xml)
print(root[0][1].text)

#get complete text via loop and concatination
allElems = root.findall(".//")
print(allElems)
concat = ''
for elem in allElems:
    print(elem.text)
    if elem.text is not None:
        concat += elem.text


print(concat)


# looping through tags
#allNodes = root.iter()

#tree = ElementTree.parse('test01.xml')
#print(ElementTree.tostring(tree, encoding='utf-8', method='text'))


