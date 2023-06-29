from flask import Flask, send_file, request
from FileOps import DeleteFile
from ConvertPdfToImages import ConvertPdfToImages

app = Flask(__name__)

@app.route('/ConvertPdfToImages', methods=['POST'])
def ConvertPdfToImageFiles():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename) #Save input file locally
        imageType = request.args.get('imageType')
        zippedFileStream = ConvertPdfToImages(imageType, f.filename)
        DeleteFile(f.filename) #Delete local input file
        return send_file(
            zippedFileStream,
            as_attachment=True,
            download_name='imageFiles.zip'
        )
    return ""
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)

