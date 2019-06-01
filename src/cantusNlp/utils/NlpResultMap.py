
from typing import Dict
from typing import List
from src.cantusNlp.utils.NlpResult import NlpResult


class NlpResultMap:

    _result_map: Dict[str, NlpResult]
    _refactored_source_corpus: str

    def __init__(self):
        self._result_map = {}
        self.set_refactored_source_corpus = None

    def add_nlp_result(self, result: NlpResult, key_name: str):
        self._result_map[key_name] = result

    def build_entry_from_cltk(self, key: str, rem_stops_text: str, deleted_tokens: List[str], cltk_lemmas_with_source: List[str]):
        nlp_res = NlpResult()
        nlp_res.add_cltk_lemma_list(cltk_lemmas_with_source)

        for word in deleted_tokens:
            nlp_res.add_deleted_token(word)

        self.set_refactored_source_corpus = rem_stops_text
        self._result_map[key] = nlp_res

    def get_result(self, key: str) -> NlpResult:
        return self._result_map.get(key)

    def set_refactored_source_corpus(self, ref_corpus: str):
        self._refactored_source_corpus = ref_corpus