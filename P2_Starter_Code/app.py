from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import PyPDF2
import re

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
    with open(abs_file_path, mode='rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        for i in range(reader.numPages):
            page = reader.getPage(i)
            rawText += page.extractText()

    emails = re.findall('''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])''', rawText)
    zipcodes = re.findall('''^\d{5}-\d{4}|\d{5}|[A-Z]\d[A-Z] \d[A-Z]\d$''', rawText)
    streets = re.findall('''\d+[ ](?:[A-Za-z0-9.-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr|Rd|Blvd|Ln|St)\.?''', rawText)
    states = re.findall('''(Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|Mississippi|Missouri|Montana|Nebraska|Nevada|New[ ]Hampshire|New[ ]Jersey|New[ ]Mexico|New[ ]York|North[ ]Carolina|North[ ]Dakota|Ohio|Oklahoma|Oregon|Pennsylvania|Rhode[ ]Island|South[ ]Carolina|South[ ]Dakota|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West[ ]Virginia|Wisconsin|Wyoming)''', rawText)
    
    email = emails[0] if len(emails) > 0 else ''
    zipcode = zipcodes[0] if len(zipcodes) > 0 else ''
    street = streets[0] if len(streets) > 0 else ''
    state = states[0] if len(states) > 0 else ''

    # Render Template and pass in values for form fields if present
    return render_template('display.html', email=email, zipcode=zipcode, address=street, state=state)


if __name__ == '__main__':
    app.run(debug=True)
