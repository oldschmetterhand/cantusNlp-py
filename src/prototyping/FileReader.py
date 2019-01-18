
import os

# in here the file / directory loop operations etc.

class FileReader:

    path: str = ""

    def __init__(self,path):
        self.path = path


    def listFiles(self):
        return os.listdir(self.path)

