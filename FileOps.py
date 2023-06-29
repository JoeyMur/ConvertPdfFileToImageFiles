from io import BytesIO
import os
import zipfile as ZipFile

def ZipFiles(files):
    stream = BytesIO()
    with ZipFile.ZipFile(stream, 'w', compression=ZipFile.ZIP_STORED) as zf:
        for file in files:
            zf.write(file, os.path.basename(file), compress_type=None, compresslevel=None)
    stream.seek(0)
    return stream

def DeleteFile(file):
    try:
        os.remove(file)
    except:
        pass