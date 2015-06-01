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
from opencv.cv import *
from opencv.highgui import *
from shutil import copy
 
def detectObjects(image, imagefile):
  """Converts an image to grayscale and prints the locations of any
     faces found"""
  print "-------------- in detectObjects ----------------\n"
  grayscale = cvCreateImage(cvSize(image.width, image.height), 8, 1)
  print "-------------- after grayscale ----------------\n"
  cvCvtColor(image, grayscale, CV_BGR2GRAY)
  print "-------------- after cvtcolor ----------------\n"

  storage = cvCreateMemStorage(0)
  cvClearMemStorage(storage)
  cvEqualizeHist(grayscale, grayscale)
  cascade = cvLoadHaarClassifierCascade(
    '/home/madhu/ws/opencv-2.4.0/data/haarcascades/haarcascade_frontalface_default.xml',
    cvSize(1,1))
  print "-------------- after load haarclassified ----------------\n"
  if cascade is None:
      print "-------------- unable to load haarclassified ----------------\n"
      return 0

  faces = cvHaarDetectObjects(grayscale, cascade, storage, 1.2, 2,
                             CV_HAAR_DO_CANNY_PRUNING, cvSize(50,50))

  print("-------------- after haardetectobjects faces total: %d ----------------\n" % faces.total)
  if faces.total > 0:
    for f in faces:
        print("---- found a face: [(%d,%d) -> (%d,%d)]" % (f.x, f.y, f.x+f.width, f.y+f.height))
        #foundFace(imagefile, f)
  return faces.total
 
def foundFace(imagefile, f):
    outfilename = os.path.join(app.config['OUT_FOLDER'], imagefile)
    center = cvPoint(f.x+6, f.y)
    radius = f.y
    cvCircle(imagefile, center, radius,
                         cvScalar(34, 255, 255,255),
                         3, #thickness
                         -1, 0)
    #os.system("convert {image} -stroke red -fill red -draw \"rectangle {a},{b} {c},{d}\" {output}".format(
    #os.system("convert {image} -draw \"image SrcOver {a},{b} {c},{d} biglazer.png\" {output}".format(
    #                image=imagefile,
    #                a=f.x+6,
    #                b=f.y,
    #                c=f.width,
    #                d=f.height,
    #                output=outfilename));
 
#urls = (
#    '/upload', 'Upload',
#)

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
        #return redirect(url_for('uploaded_file',
        #                        filename=filename))
        # detect face
        image = cvLoadImage(uploadfilename);
        print "-------------- loaded in opencv ----------------\n"
        outfilename = os.path.join(app.config['OUT_FOLDER'], filename)
        if (detectObjects(image, uploadfilename) > 0):
            copy(uploadfilename, outfilename)
        else:
            return """No face found."""
    else:
        print "-------------- in else ----------------\n"

    return redirect('/uploads/%s'%filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == "__main__":
#   app = web.application(urls, globals(), True)
   app.run(debug=True)

