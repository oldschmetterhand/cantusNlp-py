
import os
from typing import List
from pathlib import Path

class FileReader:

    _path: str = ""

    def __init__(self, path: str = None):

        if path is None:
            path = self.calcPath(__file__)

        self._path = path

    def listFiles(self, dirPath: str = None):
        """
        Lists all files of optionally given directory.
        :param dirPath: optional specifies which folder should be listed.
        Otherwise will access path given at instantiation.
        :return: List of strings with file and folder-names inside (e.g. XYZ.xml).
        """

        if dirPath is None:
            dirPath = self.getPath()

        fileList: List[str] = os.listdir(dirPath)
        return fileList

    def calcPath(self, file: object):
        """
        Returns the given file's path as Path object from pathlib.
        Further operation like .name are therefore possible ..> see
        doc from pathlib.
        :param file: best is to give __file__ as input param.
        :return: Given file's path as Path instance from pathlib.
        """
        p: Path = Path(file)
        return p


    def getPath(self):
        return self._path
