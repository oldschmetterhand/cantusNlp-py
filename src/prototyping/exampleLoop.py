from src.prototyping.NlpProcessor import NlpProcessor

dir = "C:/Users/stoffse/PycharmProjects/CantusNlp/resources/sampledata/"
processor = NlpProcessor(dir)
processor.loadCorpus()
processor.retrieveLatinModels() # ...> loads the dataModels from the internet

map = processor.getTextMap()


aggregated_str = ""

for key in map:
    print("loop")

    cur_txt = processor.getText(key)
    tokenized_txt = processor.wtokenizeLatin(cur_txt)
    try:
        lemmatized_txt = processor.lemmatizeLat(tokenized_txt)
        lemmatized_noStops = processor.removeLatStopWords(tokenized_txt)
        for word in lemmatized_noStops:
            aggregated_str += word + " "

    except:
        print("err in: " + key)









print(aggregated_str)