
import os

# in here the file / directory loop operations etc.
from typing import List


class FileReader:

    _path: str = ""

    def __init__(self, path: str):
        self._path = path


    def listFiles(self):
        fileList: List[str] = os.listdir(self._path)
        return fileList
