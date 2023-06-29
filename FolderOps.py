import os
import sys

def CreateFolder(folder):
    try:
        os.mkdir(folder)
    except:
        pass
        
def DeleteFilesInFolder(directory):
    try:
        files = GetFilesInDirectory(directory)
        for file in files:
            os.remove(f"{directory}/{file}")
    except:
        pass
        
def GetFilenameFromFilepath(filepath):
    return os.path.basename(filepath)
    
def GetFilesInDirectory(directory):
    return os.listdir(directory)