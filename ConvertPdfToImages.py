import Config
from GenerateImages import GenerateImagesFromPdfFile
from FolderOps import CreateFolder, DeleteFilesInFolder
from FileOps import ZipFiles

def ConvertPdfToImages(imageFileExtension, filepath):
    DeleteFilesInFolder(Config.config['OutputDir'])
    CreateFolder(Config.config['OutputDir'])
    
    localImageFiles = GenerateImagesFromPdfFile(filepath, imageFileExtension, Config.config['OutputDir'])
    zippedFileStream = ZipFiles(localImageFiles)
    return zippedFileStream