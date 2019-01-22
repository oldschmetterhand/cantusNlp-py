
from cltk.corpus.utils.importer import CorpusImporter
from cltk.tokenize.word import nltk_tokenize_words
from cltk.tokenize.word import WordTokenizer
from collections import Counter
from cltk.stop.latin import STOPS_LIST
from cltk.stem.lemma import LemmaReplacer


class CltkOperator:

    def __init__(self):
        print("bla")

    def retrieveLatinModels(self):
        """
        Loads the required Latin data models (for the cltk processing) from the internet.
        Uses the CorpusImporter('latin') to access the resources.
        The data will be stored in the local project ...> from then the cltk
        """
        latinDownloader = CorpusImporter('latin')
        latinDownloader.import_corpus('latin_text_latin_library')
        latinDownloader.import_corpus('latin_models_cltk')

    def wtokenizeLatin(self, text: str):
        """
        Uses the latin word tokenizer from cltk to tokenize the words for given text.
        Removes punctuation internally.
        :param text: Text to tokenize.
        :return: List comprehension of tokenized words.
        """
        text = text.lower()
        #print(text)
        wordTokenizer = WordTokenizer("latin")
        tokens = wordTokenizer.tokenize(text)
        tokens: list = self._removePunctuation(tokens)
        return tokens

    def countWords(self, text: list):
        wordsDict: dict = Counter(text)
        return wordsDict

    def removeLatStopWords(self, tokenized_text: list):
        removedStops: list[str] = [w for w in tokenized_text if not w in STOPS_LIST]
        return removedStops

    def lemmatizeLat(self, tokenized_words: list):
        lemmatizer = LemmaReplacer('latin')
        lemmata: list = lemmatizer.lemmatize(tokenized_words)
        return lemmata