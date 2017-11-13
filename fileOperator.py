import os
import shutil

class fileOperator:
    rootPath = ""
    processedFolder = "no folder with name of Processed or processed"
    count = 0
    hasValidFolder = 0
    def __init__(self, path):
        self.rootPath = path
        return

    def findProcessedFolder(self):
        objs = os.listdir(self.rootPath)
        for obj in objs:
            tmp = self.rootPath + os.sep + obj
            if os.path.isdir(tmp) and (obj.find("process") == 0 or obj.find("Process") == 0):
                self.processedFolder = tmp
                return 0
        return 1

    def clean(self):
        if not os.path.isdir(self.rootPath):
            return "Please input valid path\n"
        if self.findProcessedFolder() != 0 :
            return "here is no processed folder\n"
        processedFiles = os.listdir(self.processedFolder)
        for f in processedFiles:
            extension = os.path.splitext(f)[1]
            fileName = f.rpartition("_")[0]
            src = self.rootPath + os.sep + fileName + extension
            self.count = self.count + 1
            shutil.copy(src,self.processedFolder)
        return str(self.count) + " files are copied to Processed folder\nCleaning suceed\n"
