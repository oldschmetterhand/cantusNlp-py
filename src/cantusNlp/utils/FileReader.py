
import os
from typing import List
from pathlib import Path

class FileReader:

    _path: str = ""

    def __init__(self, path: str):
        self._path = path

    def listFiles(self, dirPath = None):

        if dirPath is None:
            dirPath = self.getPath()

        fileList: List[str] = os.listdir(dirPath)
        return fileList

    def calcPath(self, file: object):
        p: Path = Path(file)
        return p


    def getPath(self):
        return self._path
