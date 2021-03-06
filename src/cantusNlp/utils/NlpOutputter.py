
import json
import os
from typing import Dict
from typing import List
from typing import Tuple
from src.cantusNlp.utils.NlpResultMap import NlpResultMap


class NlpOutputter:

    _nlp_result_map: NlpResultMap

    def __init__(self, result_dir: str, nlp_result_map: NlpResultMap):
        self._json = json
        self._result_dir = result_dir
        self._nlp_result_map = nlp_result_map

    def output_to_txt(self, text: str, folder_file_name: str):
        """
        Writes given file to given path (+filename).
        :param text: String to ouput to text file
        :param folder_file_name: Relative path where to write the .txt with filename inside the result_dir folder
        :return:
        """
        if '.' not in folder_file_name:
            raise ValueError(str(self.__class__) + ": No '.' was given as argument. "
                                                   "Please consider defining your filename")

        path = self._result_dir + "/" + folder_file_name
        f = open(path, "w")
        f.write(str(text))
        f.close()

    def write_dict_to_json(self, dict_to_write: dict, folder_file_name: str):
        """
        Writes given dictionary to specified path (+ filename) as json object. (no json array)
        :param dict_to_write: Dictionary to write to json file
        :param folder_file_name: Relative path where to write the json with filename inside the result_dir folder
        e.g. 'folderXY/names/surnames/startingWithS.json'
        :return:
        """
        if '.' not in folder_file_name:
            raise ValueError(str(self.__class__) + ": No '.' was given as argument. "
                                                   "Please consider defining your filename")

        path = self._result_dir + "/" + folder_file_name
        print(path)
        f = open(path, "w")
        json.dump(dict_to_write, f)
        f.close()

    def write_lemmatization_result(self):

        keys: list = self._nlp_result_map._result_map.keys()

        for key in keys:
            print(key)

            cur_nlp_result = self._nlp_result_map.get_result(key)

            lemma_dicts = cur_nlp_result.return_array_of_lemmas_dicts()
            deleted_tokens = cur_nlp_result.get_deleted_tokens()
            words_not_known = cur_nlp_result.get_words_not_known()

            dict_to_write = {
                "lemmata": lemma_dicts,
                "deletedTokens": deleted_tokens,
                "wordsNotKnown":words_not_known
            }

            self.write_dict_to_json(dict_to_write, str.replace(key, ".", "_") + "/lemmatizationResult.json")

    def write_list_to_json(self, list: List, folder_file_name: str):
        """

        :param list: python list to write to json array.
        :param folder_file_name:
        :return:
        """
        path = self._result_dir + "/" + folder_file_name
        f = open(path, "w")
        json.dump(list, f)
        f.close()

    def output_for_voyant(self) -> Dict[str, str]:

        corpora_keys = self._nlp_result_map.get_available_keys()

        voyant_dict: Dict[str, str] = {}

        for corpus in corpora_keys:
            lemma_list = self._nlp_result_map.get_result(corpus).get_list_of_lemma()

            aggr_lemma: str = ""
            for lemma in lemma_list:
                aggr_lemma += (lemma.get_lemma() + " ")

            self.output_to_txt(aggr_lemma, str.replace(corpus, ".", "_") + "/voyantLemma.txt")

            voyant_dict[corpus] = aggr_lemma

        return voyant_dict