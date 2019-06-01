
from typing import Dict
from src.cantusNlp.utils.NlpResult import NlpResult


class NlpResultMap:

    _result_map: Dict[str, NlpResult]

    def __init__(self):
        self._result_map = {}

    def add_nlp_result(self, result: NlpResult, key_name: str):
        self._result_map[key_name] = result

    def get_result(self, key: str) -> NlpResult:
        return self._result_map.get(key)