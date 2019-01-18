import src.prototyping.XReader as XReader
import src.prototyping.FileReader as FileReader

xreader = XReader.XReader()
dir = "C:/Users/stoffse/PycharmProjects/CantusNlp/resources/sampledata/"


# get the bodyTxt
#xTree = xreader.readXml("C:/Users/stoffse/PycharmProjects/CantusNlp/resources/sampledata/fragment_1a.xml")
#bodyTxt = xreader.getTeiBodyText(xTree)
#print(bodyTxt)


# example use of the fileReader class
fileReader = FileReader.FileReader(dir)
fileNameList = fileReader.listFiles()
print(fileNameList)
for fileName in fileNameList:
    # print(fileName)
    # trying getting all the body texts.
    path = dir + fileName
    #print(path)
    xTree = xreader.readXml(path)
    bodyTxt = xreader.getTeiBodyText(xTree)
    print(bodyTxt)


