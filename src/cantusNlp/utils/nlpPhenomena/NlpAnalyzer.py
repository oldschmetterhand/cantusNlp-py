
from typing import Dict
from typing import List
from src.cantusNlp.utils.NlpResultMap import NlpResultMap


class NlpAnalyser:

    _nlp_result_map: NlpResultMap

    def __init__(self, nlp_result_map: NlpResultMap):
        self._nlp_result_map = nlp_result_map

    def calculate_most_occurence_lemmata(self, min_lemma_occurence: int) -> List[Dict[str, str or int]]:
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

        print(str(lemma_uniques))
        return lemma_uniques

            # self.write_dict_to_json(dict_to_write, str.replace(key, ".", "_") + "/lemmatizationResult.json")

