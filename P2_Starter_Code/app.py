from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from commonregex import CommonRegex
import PyPDF2

from werkzeug.utils import secure_filename
import os
from os import abort

app = Flask(__name__)
bootstrap = Bootstrap(app)
script_dir = os.path.dirname(__file__)

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
            uploaded_file.save(os.path.join(
                app.config['UPLOAD_PATH'], filename))
            return redirect('display/' + filename)
    return render_template("upload.html")


@app.route("/display/<filename>")
def display(filename: str):
    relativePath = 'uploads/' + filename
    abs_file_path = os.path.join(script_dir, relativePath)

    rawText = ''
    # Open file
    with open(abs_file_path, mode='rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        for i in range(reader.numPages):
            page = reader.getPage(i)
            rawText += page.extractText()

    parsed_text = CommonRegex(rawText)

    # Trying CommonRegex out. These will parse the text of pdf and
    # return an array with any values associated with respective parsed_text.attribute
    # Documentation - https://github.com/madisonmay/CommonRegex
    address = parsed_text.street_addresses[0]
    email = parsed_text.emails[0]

    # Render Template and pass in values for form fields if present
    return render_template('display.html', first_name='Hi', last_name='there', address=address, email=email)


if __name__ == '__main__':
    app.run(debug=True)
