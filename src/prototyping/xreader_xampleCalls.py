import prototyping.XReader as XReader

xreader = XReader.XReader()




# xTree = xreader.readXml("fragment_1a.xml")
# rootElem = xreader.getRootTag(xTree)
# print(rootElem)


# get the bodyTxt
xTree = xreader.readXml("fragment_1a.xml")
bodyTxt = xreader.getTeiBodyText(xTree)
print(bodyTxt)

# "repairing string etc."
# bodyTxt = bodyTxt.replace("\n", "")
# bodyTxt = bodyTxt.replace("\t", "")
# bodyTxt = bodyTxt.strip()
# bodyTxt = bodyTxt.replace("  ", "")         # remove duplicated space
# print(bodyTxt)


