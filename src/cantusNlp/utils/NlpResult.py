
from typing import List
from typing import Dict
from src.cantusNlp.utils.nlpPhenomena.Lemma import Lemma


class NlpResult:

    _lemma_list: List[Lemma]
    _words_not_known: List[str]
    _deleted_tokens: List[str]

    def __init__(self, list_of_lemma: List[Lemma] = None, words_not_known: List[str] = None, deleted_tokens: List[str] = None):
        self._lemma_list: List[Lemma] = list_of_lemma
        self._words_not_known: List[str] = words_not_known
        self._deleted_tokens: List[str] = deleted_tokens
        self._assign_empty_list_if_no_param()

    def add_lemma(self, lemma: Lemma):
        self._lemma_list.append(lemma)

    def add_word_not_known(self, word_not_known: str):
        self._words_not_known.append(word_not_known)

    def add_deleted_token(self, deleted_token: str):
        self._deleted_tokens.append(deleted_token)

    def add_cltk_lemma_list(self, lemma_source_slashed: List[str]) -> List[Lemma]:

        if len(self._lemma_list) > 1:
            raise ValueError("There already is a filled lemma list inside the NlpResult. The list is: " + str(self._lemma_list))

        for lemma_source_pair in lemma_source_slashed:
            split_str = lemma_source_pair.split("/")
            lemma = Lemma(split_str[1], split_str[0])
            self.add_lemma(lemma)

        return self._lemma_list

    def return_array_of_lemmas_dicts(self) -> List[Dict[str, Dict[str, str or int or None]]]:
        if len(self._lemma_list) is 0:
            raise ValueError("Can't transform a List of length 0! The Lemmalist is: " + str(self._lemma_list))

        dict_arr: List[Dict[str, Dict[str, str or int or None]]] = []

        for lemma in self._lemma_list:
            lemma_dict, lemma_key = lemma.return_as_dictionary()
            new_dict = {
                lemma_key: lemma_dict
            }
            dict_arr.append(new_dict)

        return dict_arr

    def get_list_of_lemma(self) -> List[Lemma]:
        return self._lemma_list

    def get_words_not_known(self) -> List[str]:
        return  self._words_not_known

    def get_deleted_tokens(self) -> List[str]:
        return self._deleted_tokens

    def _assign_empty_list_if_no_param(self):
        if self._lemma_list is None:
            self._lemma_list = []

        if self._words_not_known is None:
            self._words_not_known = []

        if self._deleted_tokens is None:
            self._deleted_tokens = []