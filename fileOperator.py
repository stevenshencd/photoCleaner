import os
import shutil

class fileOperator:
    rootPath = ""
    processedFolder = ""
    count = 0
    def __init__(self, path):
        if not os.path.isdir(path):
            print "please input valid path"
            return
        self.rootPath = path
        self.findProcessedFolder()
        return

    def findProcessedFolder(self):
        objs = os.listdir(self.rootPath)
        for obj in objs:
            tmp = self.rootPath + os.sep + obj
            if os.path.isdir(tmp) and (obj.find("process") == 0 or obj.find("Process") == 0):
                self.processedFolder = tmp
                break
        return

    def clean(self):
        processedFiles = os.listdir(self.processedFolder)
        for f in processedFiles:
            extension = os.path.splitext(f)[1]
            fileName = f.rpartition("_")[0]
            src = self.rootPath + os.sep + fileName + extension
            self.count = self.count + 1
            shutil.copy(src,self.processedFolder)
        return str(self.count) + " files are copied to Processed folder\n Cleaning suceed"
