# ConvertPdfFileToImageFiles
Takes in a filestream and returns a stream containing a zip file.
This zip file contains an image of each page in the PDF file.

To deploy: RUN docker-compose
To Use: 
 - Send HTTP POST request to localhost:8081/ConvertPdfToImages?imageType={imageFileType}
 - Body should contain a PDF file (key "file")
