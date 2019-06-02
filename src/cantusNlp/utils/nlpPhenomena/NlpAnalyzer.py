
from typing import Dict
from typing import List
from src.cantusNlp.utils.NlpResultMap import NlpResultMap


class NlpAnalyser:

    _nlp_result_map: NlpResultMap

    def __init__(self, nlp_result_map: NlpResultMap):
        self._nlp_result_map = nlp_result_map

    def calc_lemma_occurence(self, min_lemma_occurence: int) -> Dict[str, List[Dict[str, str or int]]]:
        """
        Counts the occurence of each individual lemmas and returns the result as dictionary.
        :param min_lemma_occurence: Only lemmas higher equal occurence are returned.
        :return: Dictionary with key for each read in file with file extension e.g. "xy.txt".
        Dictionarie's value is a List of Dictionaries. Each dictionary is a lemma -> with properties
        name, value, and source.
        """

        corpus_occurent_lemma: Dict[str, List[Dict[str, str or int]]] = {}

        keys: list = self._nlp_result_map._result_map.keys()
        all_lemma: List[str] = []

        for key in keys:
            cur_nlp_result = self._nlp_result_map.get_result(key)
            lemma_dicts = cur_nlp_result.return_array_of_lemmas_dicts()

            for lemma in lemma_dicts:
                all_lemma.append(lemma.get("lemma"))

            uniques: set = set(all_lemma)
            lemma_uniques: list = []

            for unique in uniques:
                if unique in all_lemma:
                    lemma_count = all_lemma.count(unique)

                    if lemma_count >= min_lemma_occurence:
                        lemma_uniques.append({
                            'name': str(unique),
                            'value': lemma_count
                        })


            corpus_occurent_lemma[key] = lemma_uniques

        print(corpus_occurent_lemma)
        return corpus_occurent_lemma

