
import re


class StringRefinery:

    _text: str

    def __init__(self):
        print("")

    def refineElemTxt(self, txt: str):
        txt = self.delEditorMarks(txt)
        txt = self.replNumbers(txt)
        txt = txt.replace("\n", " ")
        txt = txt.replace("\t", " ")

        # at last whitespace operations
        txt = txt.strip()
        txt = re.sub(" +", " ", txt)  # remove via regex
        return txt

    def delEditorMarks(self, txt: str):
        txt = txt.replace("[", " ")
        txt = txt.replace("]", " ")  # quite specific for my current project(maybe not good here)
        return txt

    def replNumbers(self, txt: str):
        remNumbs: str = re.sub("[\d]+", " ", txt)
        return remNumbs


    def getText(self):
        return self._text
