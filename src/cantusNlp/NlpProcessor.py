
import src.cantusNlp.utils.FileReader as FileReader
import src.cantusNlp.utils.XReader as Xreader
import src.cantusNlp.utils.StringRefinery as StringRefinery
import src.cantusNlp.utils.CltkOperator as CltkOperator
import os
import json


class NlpProcessor:

    _dataPath: str
    _textMap: dict

    _xreader: Xreader
    _fileReader: FileReader
    _cltk: CltkOperator
    _strRefiner: StringRefinery

    def __init__(self, dataPath: str, resultDir: str):
        self._dataPath = dataPath
        self._resultDir = resultDir

        self._xreader = Xreader.XReader()
        self._fileReader = FileReader.FileReader(self._dataPath)
        self._cltk = CltkOperator.CltkOperator()
        self._strRefiner = StringRefinery.StringRefinery()

        self._textMap = {}  # initialize here

    def _addToMap(self, key: str, content: str):
        self._textMap[key] = content

    def loadCorpus(self, elemToIgnore: str = None):
        """
        Uses the intern dirPath variable given at instantiation to locate the diretory
        of the xml files. Build the access to the individual files via concatinating dirpath
        and name of the xml-files. Uses the XReader class to retrieve the TEI-body as text.
        Stores retrieved corpus in the dictionary ...> filename.xml as key-value.
        :param elemToIgnore: Can optionally define a tag to be ignored for the read in of
        the tei-body.
        :return: nothing
        """
        fileNameList = self._fileReader.listFiles()
        for fileName in fileNameList:
            # trying getting all the body texts.
            path = self._dataPath + fileName

            # .txt or .xml
            if fileName.endswith(".xml"):
                xTree = self._xreader.readXml(path)
                bodyTxt = self._xreader.getTeiBodyText(xTree, elemToIgnore)
            elif fileName.endswith(".txt"):
                bodyTxt = self._fileReader.readTxt(path)
            else:
                raise TypeError("LoadCorpus only supports .txt and .xml files. Given file was: " + path)

            self._textMap[fileName] = bodyTxt

    def lemmatizeCorpus(self, output_statistics: bool = False) -> dict:
        """

        :param output_statistics: Boolean decides if analysis files should be generated or not.
        If true creates folders for each read in file in given result folder at instantiation.
        :return: The lemmatized internal map.
        """

        if output_statistics:
            self._lemmatizeWithAnalysis()
        else:
            cltk = self._cltk
            map: dict[str] = self.getTextMap()

            for key in map:
                text = map[key]
                text = self._strRefiner.refineElemTxt(text)
                text = cltk.wtokenizeLatin(text)
                text = cltk.removeLatStopWords(text)
                text = cltk.lemmatizeLat(text)
                map[key] = text

        return self.getTextMap()

    def _lemmatizeWithAnalysis(self):
        """

        :return:
        """

        # TODO finish method + split into reusable AND testable methods

        cltk = self._cltk
        map: dict[str] = self.getTextMap()

        for key in map:
            text = map[key]
            text = self._strRefiner.refineElemTxt(text)
            text, deleted_tokens = cltk.wtokenizeLatin(text, True)
            text = cltk.removeLatStopWords(text)
            lemmas_plain, lemmas_with_source = cltk.lemmatizeLat(text, True)

            base_path = self._resultDir
            dir_name = key.replace(".", "_")
            os.makedirs(base_path + "/" + dir_name)

            self.outputToTxt(deleted_tokens, base_path + "/" + dir_name + "/deleted_tokens.txt")
            self.outputToTxt(lemmas_with_source, base_path + "./" + dir_name + "/lemmas_with_source.txt")
            self.outputToTxt(lemmas_plain, base_path + "./" + dir_name + "/lemmas_plain.txt")

            # voyant writing
            f = open(base_path + "./" + dir_name + "/voyant_ready.txt", "w")
            aggr_str = ""
            for word in lemmas_plain:
                aggr_str += (word + " ")

            self.outputToTxt(aggr_str, base_path + "./" + dir_name + "/voyant_ready.txt")

            # from here method to analyze analytical deviation from cltk perseus corpus.
            self._createAnalysisJSON(dir_name, text)

    def getText(self, fileName: str) -> str:
        """
        Accesses the intern dictionary in which the read in corpora are saved under their
        filename as key-value. Value calls dictionary[key] ...> to access the data.
        :param fileName: The Name of the file read in is stored as key in the intern dictionary. With
        the filename the read in corpus is accessible.
        :return: the internally saved corpus
        """
        corpus: str = self._textMap[fileName]
        return corpus

    def getTextMap(self) -> dict:
        return self._textMap

    def aggregateWordlist(self, wordList: list) -> str:
        """
        Takes a list of words and returns a giant string, with all individual words separated through
        a single whitespace.
        :param wordList:
        :return: one big string of words separated by whitespace.
        """
        aggr: str = ""
        for word in wordList:
            aggr += word + " "

        return aggr

    def _createAnalysisJSON(self, folder_to_create: str, refined_word_list: list) -> dict:
        """
        Calls the analyzeCltkLemmaDeviation method from the CltkOperator.py and writes result to
        a json file with values for words not known to the cltk lemmatizer.
        :param refined_word_list: Tokenized wordlist with removed latin stopwords.
        :param folder_to_create: Folder where the json should be placed (created if necessary)
        :return: Dictionary created (that is written to JSON)
        """

        analDict: dict = {}

        words_not_found, no_match_percentage = self._cltk.analyzeCltkLemmaDeviation(refined_word_list)
        analDict['wordsNotKnownToLemmatizer'] = str(words_not_found)
        analDict['percentageOfWordsNotKnownToLemmatizer'] = str(no_match_percentage)

        self.write_dict_to_json(analDict, self._resultDir + "./" + folder_to_create + "/analysisJson.json")
        return analDict

    def write_dict_to_json(self, dict_to_write: dict, path_with_name:str):
        """
        Writes given dictionary to specified path (+ filename) as json object. (no json array)
        :param dict_to_write: Dictionary to write to json file
        :param path_with_name:  Path where to write the json with filename
        e.g. 'folderXY/names/surnames/startingWithS.json'
        :return:
        """
        f = open(path_with_name, "w")
        json.dump(dict_to_write, f)
        f.close()

    def outputToTxt(self, text: str, path_with_name:str):
        """
        Writes given file to given path (+filename).
        :param text: String to ouput to text file
        :param path_with_name: Path where to write the .txt with filename
        :return:
        """
        f = open(path_with_name, "w")
        f.write(str(text))
        f.close()


