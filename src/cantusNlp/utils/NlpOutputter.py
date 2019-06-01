
import json
from typing import Dict
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
        f = open(path, "w")
        json.dump(dict_to_write, f)
        f.close()


    def write_lemmatization_result(self):

        keys: list = self._nlp_result_map._result_map.keys()

        for key in keys:
            print(key)
            lemma_dicts = self._nlp_result_map.get_result(key).return_array_of_lemmas_dicts()
            print(lemma_dicts)

            print(self._nlp_result_map.get_result(key).get_deleted_tokens())
            print(self._nlp_result_map.get_result(key).get_words_not_known())