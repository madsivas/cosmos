import os

from flask import Flask
from flask import request
from flask import redirect, url_for
from werkzeug import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = '/home/madhu/ws/cosmos/cosmos/static/uploads'
OUT_FOLDER = '/home/madhu/ws/cosmos/cosmos/static/out'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'JPG'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUT_FOLDER'] = OUT_FOLDER

import sys, os, subprocess, uuid
import cv
#from opencv.cv import *
#from opencv.highgui import *
from shutil import copy

@app.route('/')
def hello_world():
  return '<h2><i>Welcome to Cosmos!</i></h2>'

def get_upload():
    return """<html><head><link rel="shortcut icon" href="/static/favicon_flower.ico"
type="image/x-icon"></head><body>
<h1>Upload flower pic</h1>
<img src='static/uploads/P1050294.JPG' width='250px' height='200px'/>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        return post_upload()
    else:
        return get_upload()

def post_upload():
    print "-------------- start post ----------------\n"
    file = request.files['myfile']
    from pprint import pprint
    pprint(file)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        uploadfilename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(uploadfilename)
        print "-------------- saved file ----------------\n"
        #outfilename = os.path.join(app.config['OUT_FOLDER'], filename)
        #file.save(outfilename)
        from colordetect import detect_color
        detect_color(filename)

    return redirect('/uploads/%s'%filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == "__main__":
#   app = web.application(urls, globals(), True)
   app.run(debug=True)

