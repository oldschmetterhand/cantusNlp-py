
from src.prototyping.NlpProcessor import NlpProcessor

#from cltk.tokenize.sentence import TokenizeSentence

# test run ...> everything goes as expected
dir = "C:/Users/stoffse/PycharmProjects/CantusNlp/resources/sampledata/"
processor = NlpProcessor(dir)
processor.loadLocalXml()

# test if everything is inside
for x in processor.textMap:
    print(x)
    print(processor.textMap[x])



##########NLP TRIES#####

#tokenizer = TokenizeSentence("latin")

#myTokens = tokenizer.tokenize_sentences(processor.textMap["fragment_1a.xml"])

#print(myTokens)
