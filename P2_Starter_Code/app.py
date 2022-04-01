from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from commonregex import CommonRegex
import PyPDF2

from werkzeug.utils import secure_filename
import os
from os import abort

app = Flask(__name__)
bootstrap = Bootstrap(app)

user = {}

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024  # max file size is 1MB
app.config['UPLOAD_EXTENSIONS'] = ['.pdf']  # allows for pdf files
app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            return redirect('display')
    return render_template("upload.html")

@app.route("/display")
def display():
    # Open file
    pdfFileObj = open('static/sample_resume.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    number_of_pages = pdfReader.numPages
    parsed_text = ''

    # Loop for reading all the Pages
    for i in range(number_of_pages):
        # Creating a page object and append text to variable
        pageObj = pdfReader.getPage(i)
        parsed_text += pageObj.extractText()

    parsed_text = CommonRegex(parsed_text)

    # Trying CommonRegex out. These will parse the text of pdf and 
    # return an array with any values associated with respective parsed_text.attribute 
    # Documentation - https://github.com/madisonmay/CommonRegex
    address = parsed_text.street_addresses or ""
    email = parsed_text.emails or ""

    # closing the pdf file object
    pdfFileObj.close()

    # Render Template and pass in values for form fields if present
    return render_template('display.html', first_name="Not_parsed", last_name="Not_parsed", address=address[0], email=email[0])

if __name__ == '__main__':
    app.run(debug=True)
