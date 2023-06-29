import Config
from fitz import fitz
from FolderOps import GetFilenameFromFilepath

def GenerateImagesFromPdfFile(pdfFile, imageFileExtension, outputDir):
    document = fitz.Document(pdfFile)
    fileList = []
    for page in document:
        pixmap = page.get_pixmap()
        file = Config.config['OutputDir'] + GetFilenameFromFilepath(pdfFile).replace(".pdf", f"_{page.number+1}.{imageFileExtension}")
        fileList.append(file)
        pixmap.save(file)
    return fileList