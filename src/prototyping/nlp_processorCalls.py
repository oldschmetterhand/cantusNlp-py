
from src.prototyping.NlpProcessor import NlpProcessor

from cltk.tokenize.sentence import TokenizeSentence
from cltk.corpus.utils.importer import CorpusImporter
from cltk.tokenize.word import nltk_tokenize_words

# test run ...> everything goes as expected
dir = "C:/Users/Sebi/PycharmProjects/cantusNlp-py.git/resources/sampleData/"
processor = NlpProcessor(dir)
processor.loadLocalXml()

# test if everything is inside
# for x in processor.textMap:
#     print(x)
#     print(processor.textMap[x])



############################
##########NLP Procedure#####
############################

# first git needs to be installed on the local machine!
# i need to import the datamodels first! ...> run this first (don't need to repeat!)
#my_latin_downloader = CorpusImporter('latin')
#my_latin_downloader.import_corpus('latin_text_latin_library')
#my_latin_downloader.import_corpus('latin_models_cltk')

txt = processor.textMap["fragment_1a.xml"]

sentenceTokenizer = TokenizeSentence('latin')
sentences = sentenceTokenizer.tokenize_sentences(txt)
print(sentences)

wordTokens = nltk_tokenize_words(txt)
print(wordTokens)