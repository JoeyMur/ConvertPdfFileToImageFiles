FROM python:3.9
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pymupdf
RUN pip install flask

COPY Main.py .
COPY ConvertPdfToImages.py .
COPY FolderOps.py .
COPY FileOps.py .
COPY GenerateImages.py .
COPY Config.py .

CMD ["python", "./Main.py"]