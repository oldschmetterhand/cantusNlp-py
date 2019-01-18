
import os

# in here the file / directory loop operations etc.
from typing import List


class FileReader:

    path: str = ""

    def __init__(self, path: str):
        self.path = path


    def listFiles(self):
        fileList: List[str] = os.listdir(self.path)
        return fileList

