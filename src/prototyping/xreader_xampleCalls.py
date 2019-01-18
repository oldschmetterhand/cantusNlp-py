import src.prototyping.XReader as XReader

xreader = XReader.XReader()




# xTree = xreader.readXml("fragment_1a.xml")
# rootElem = xreader.getRootTag(xTree)
# print(rootElem)


# get the bodyTxt
xTree = xreader.readXml("C:/Users\stoffse\PycharmProjects\CantusNlp\\resources\sampledata\\fragment_1a.xml")
bodyTxt = xreader.getTeiBodyText(xTree)
print(bodyTxt)





