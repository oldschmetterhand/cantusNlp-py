
import src.cantusNlp.utils.FileReader as FileReader
import src.cantusNlp.utils.XReader as Xreader
import src.cantusNlp.utils.StringRefinery as StringRefinery
import src.cantusNlp.utils.CltkOperator as CltkOperator
from typing import List
from typing import Dict
from src.cantusNlp.utils.NlpResultMap import NlpResultMap
from src.cantusNlp.utils.NlpOutputter import NlpOutputter
from src.cantusNlp.utils.nlpPhenomena.NlpAnalyzer import NlpAnalyser
import os
import json


class NlpProcessor:

    _dataPath: str
    _textMap: dict

    _xreader: Xreader
    _fileReader: FileReader
    _cltk: CltkOperator
    _strRefiner: StringRefinery
    _nlpResultMap: NlpResultMap
    _nlp_outputter: NlpOutputter
    _nlp_analyzer: NlpAnalyser

    def __init__(self, dataPath: str, resultDir: str):
        self._dataPath = dataPath
        self._resultDir = resultDir

        self._xreader = Xreader.XReader()
        self._fileReader = FileReader.FileReader(self._dataPath)
        self._cltk = CltkOperator.CltkOperator()
        self._strRefiner = StringRefinery.StringRefinery()
        self._nlpResultMap = NlpResultMap()
        self._nlp_outputter = NlpOutputter(resultDir, self._nlpResultMap)
        self._nlp_analyser = NlpAnalyser(self._nlpResultMap)

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
            path = self._dataPath + "/" + fileName

            # creating output folders
            dir_name = fileName.replace(".", "_")
            os.makedirs(self._resultDir + "/" + dir_name)

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

        cltk = self._cltk
        map: dict[str] = self.getTextMap()

        for key in map:
            text = map[key]
            text = self._strRefiner.refineElemTxt(text)
            text, deleted_tokens = cltk.wtokenizeLatin(text, True)
            text = cltk.removeLatStopWords(text)
            lemmas_plain, lemmas_with_source = cltk.lemmatizeLat(text, True)
            map[key] = lemmas_plain

            self._nlpResultMap.build_entry_from_cltk(key, text, deleted_tokens, lemmas_with_source)

            if output_statistics:
                self._output_cltk_lemma_deviation(key.replace(".", "_"), text)

        return self.getTextMap()

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

    def _output_cltk_lemma_deviation(self, folder_to_create: str, refined_word_list: list) -> dict:
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

        self._nlp_outputter.write_dict_to_json(analDict, folder_to_create + "/lemmatizationAnalysis.json")
        return analDict

    def output_lemmatization_result(self):
        self._nlp_outputter.write_lemmatization_result()

    def analyse_lemma_occurence(self, min_lemma_occurence: int, write_to_file: bool = False) -> Dict[str, List[Dict[str, str or int]]]:
        """

        :param min_lemma_occurence:
        :param write_to_file:
        :return:
        """
        corp_lemma_occ: Dict[str, List[Dict[str, str or int]]] = self._nlp_analyser.calc_lemma_occurence(min_lemma_occurence)

        if write_to_file:
            for key in corp_lemma_occ.keys():
                self._nlp_outputter.write_list_to_json(corp_lemma_occ.get(key), str.replace(key, ".", "_")
                                                       + "/lemmataOccurences.json")

        return corp_lemma_occ

    def create_voyant_output(self) -> Dict[str, str]:
        return self._nlp_outputter.output_for_voyant()
