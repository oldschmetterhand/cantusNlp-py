
import src.prototyping.FileReader as FileReader
import src.prototyping.XReader as Xreader
from cltk.corpus.utils.importer import CorpusImporter


class NlpProcessor:

    dirPath: str
    textMap: dict

    _xreader: object
    _fileReader: object

    def __init__(self, dirPath: str):
        self.dirPath = dirPath
        self._xreader = Xreader.XReader()
        self._fileReader = FileReader.FileReader(self.dirPath)
        self.textMap = {}  # initialize here

    def addToMap(self, key: str, content: str):
        self.textMap[key] = content

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
            path = self.dirPath + fileName
            # print(path)
            xTree = self._xreader.readXml(path)
            bodyTxt = self._xreader.getTeiBodyText(xTree)
            #print(bodyTxt)
            self.textMap[fileName] = bodyTxt

    def getCorpus(self, fileName: str):
        """
        Accesses the intern dictionary in which the read in corpora are saved under their
        filename as key-value. Value calls dictionary[key] ...> to access the data.
        :param fileName: The Name of the file read in is stored as key in the intern dictionary. With
        the filename the read in corpus is accessible.
        :return: the internally saved corpus
        """
        corpus: str = self.textMap[fileName]
        return corpus

    def retrieveLatinModels(self):
        """
        Loads the required Latin data models (for the cltk processing) from the internet.
        Uses the CorpusImporter('latin') to access the resources.
        The data will be stored in the local project ...> from then the cltk
        """
        latinDownloader = CorpusImporter('latin')
        latinDownloader.import_corpus('latin_text_latin_library')
        latinDownloader.import_corpus('latin_models_cltk')


