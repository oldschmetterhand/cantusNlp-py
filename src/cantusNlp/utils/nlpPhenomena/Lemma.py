

from typing import Dict
from typing import Tuple

class Lemma:

    _lemma: str
    _source: str
    _word_position: int

    def __init__(self, lemma: str, source: str = None, word_position: int = None):
        self._lemma: str = lemma
        self._source: str or None = source
        self._word_position: int or None = word_position

    def get_lemma(self) -> str:
        return self._lemma

    def get_source(self) -> str:
        if not self._source:
            raise ValueError("No source word was defined at instantiation for the demanded lemma: " + self._lemma)
        return self._source

    def get_word_position(self) -> int:
        if not self._word_position:
            raise ValueError("No word position was defined at instantiation for the lemma: " + self._lemma)
        return self._word_position

    def return_as_dictionary(self) -> Tuple[Dict[str, str or int], str]:

        lemma_as_dict = {
            "lemma": self._lemma,
            "source": self._source,
            "word_position": self._word_position
        }

        return lemma_as_dict, self._lemma

    def __str__(self) -> str:
        string_repr: str =  "<LemmaClass> _lemma: {}, _source:{}, _word_position:{}"\
            .format(self._lemma, self._source, self._word_position)

        return string_repr
