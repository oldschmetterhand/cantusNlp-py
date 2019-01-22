

class StringRefinery:

    _text: str

    def __init__(self):
        print("")

    def refineElemTxt(self, txt: str):
        txt = txt.replace("\n", "")
        txt = txt.replace("\t", "")
        txt = txt.strip()
        txt = txt.replace("  ", "")  # remove duplicated space
        txt = self.delEditorMarks(txt)
        return txt

    def delEditorMarks(self, txt: str):
        txt = txt.replace("[", "")
        txt = txt.replace("]", "")  # quite specific for my current project(maybe not good here)
        return txt

    def getText(self):
        return self._text
