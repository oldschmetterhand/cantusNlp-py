
import os

# in here the file / directory loop operations etc.
from typing import List


class FileReader:

    _path: str = ""

    def __init__(self, path: str):
        self._path = path


    def listFiles(self, dirPath = None):

        if dirPath is None:
            dirPath = self.getPath()

        fileList: List[str] = os.listdir(dirPath)
        return fileList

    def getPath(self):
        return self._path
