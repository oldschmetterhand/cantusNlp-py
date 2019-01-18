
import src.prototyping.FileReader as FileReader
import src.prototyping.XReader as Xreader



class NlpProcessor:

    dirPath: str
    textMap: dict

    _xreader: object
    _fileReader: object

    def __init__(self, dirPath: str):
        self.dirPath = dirPath
        self._xreader = Xreader.XReader()
        self._fileReader = FileReader.FileReader(self.dirPath)


    def addToMap(self, key: str, content: str):
        self.textMap[key] = content


    def loadLocalXml(self):
        fileNameList = self._fileReader.listFiles()
        for fileName in fileNameList:
            # print(fileName)
            # trying getting all the body texts.
            path = self.dirPath + fileName
            # print(path)
            xTree = self._xreader.readXml(path)
            bodyTxt = self._xreader.getTeiBodyText(xTree)
            #print(bodyTxt)
            self.textMap[fileName] = bodyTxt

    def getCorpus(self, fileName: str):
        return self.textMap[fileName]


# test run ...> everything goes as expected
dir = "C:/Users/stoffse/PycharmProjects/CantusNlp/resources/sampledata/"
processor = NlpProcessor(dir)
processor.loadLocalXml()

for x in processor.textMap:
    print(x)
    print(processor.textMap[x])
