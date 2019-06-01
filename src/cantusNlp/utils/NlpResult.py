
from typing import List
import src.cantusNlp.utils.nlpPhenomena.Lemma as Lemma


class NlpResult:

    def __init__(self,
                 list_of_lemma: List[Lemma] = None,
                 words_not_known: List[str] = None,
                 deleted_tokens: List[str] = None
                ):

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