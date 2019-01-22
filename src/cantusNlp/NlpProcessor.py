
import src.cantusNlp.utils.FileReader as FileReader
import src.cantusNlp.utils.XReader as Xreader
import src.cantusNlp.utils.StringRefinery as StringRefinery
import src.cantusNlp.utils.CltkOperator as CltkOperator


class NlpProcessor:

    _dirPath: str
    _textMap: dict

    _xreader: Xreader
    _fileReader: FileReader
    _cltk: CltkOperator
    _strRefiner: StringRefinery

    def __init__(self, dirPath: str):
        self._dirPath = dirPath
        self._xreader = Xreader.XReader()
        self._fileReader = FileReader.FileReader(self._dirPath)
        self._textMap = {}  # initialize here

    def _addToMap(self, key: str, content: str):
        self._textMap[key] = content

    def loadCorpus(self):
        """
        Uses the intern dirPath variable given at instantiation to locate the diretory
        of the xml files. Build the access to the individual files via concatinating dirpath
        and name of the xml-files. Uses the XReader class to retrieve the TEI-body as text.
        Stores retrieved corpus in the dictionary ...> filename.xml as key-value.
        :return: nothing
        """
        fileNameList = self._fileReader.listFiles()
        for fileName in fileNameList:
            # trying getting all the body texts.
            path = self._dirPath + fileName
            # print(path)
            xTree = self._xreader.readXml(path)
            bodyTxt = self._xreader.getTeiBodyText(xTree)
            #print(bodyTxt)
            self._textMap[fileName] = bodyTxt

    def getText(self, fileName: str):
        """
        Accesses the intern dictionary in which the read in corpora are saved under their
        filename as key-value. Value calls dictionary[key] ...> to access the data.
        :param fileName: The Name of the file read in is stored as key in the intern dictionary. With
        the filename the read in corpus is accessible.
        :return: the internally saved corpus
        """
        corpus: str = self._textMap[fileName]
        return corpus

    def getTextMap(self):
        return self._textMap

    def _removePunctuation(self, text: list):
        noPuncts: list = [token for token in text if token not in ['.', ',', ':', ';']]
        return noPuncts