import os
from opencv.cv import *
from opencv.highgui import *
from shutil import copy
from pprint import pprint

imagefilepath = "/home/madhu/ws/cosmos/cosmos/static/uploads"
imagefilename = "P1100172.JPG"

imagefile = os.path.join(imagefilepath, imagefilename)
outfile = os.path.join('/home/madhu/ws/cosmos/cosmos/static/out/', imagefilename)
copy(imagefile, outfile)

image = cvLoadImage(imagefile)
grayscale = cvCreateImage(cvSize(image.width, image.height), 8, 1)
cvCvtColor(image, grayscale, CV_BGR2GRAY)
storage = cvCreateMemStorage(0)
cvClearMemStorage(storage)
cvEqualizeHist(grayscale, grayscale)
cascade = cvLoadHaarClassifierCascade(
            '/home/madhu/ws/opencv-2.4.0/data/haarcascades/haarcascade_frontalface_default.xml',
            cvSize(1,1))
pprint(cascade)
faces = 0
if (cascade is not None):
    faces = cvHaarDetectObjects(grayscale, cascade, storage, 1.2, 2, CV_HAAR_DO_CANNY_PRUNING, cvSize(50,50))
    print("-------------- after haardetectobjects faces total: %d ----------------\n" % faces.total)
else:
    print("----- unable to load haarcascades")


pprint(image)

if faces.total > 0:
  for f in faces:
      print("---- found a face: [(%d,%d) -> (%d,%d)]" % (f.x, f.y, f.x+f.width, f.y+f.height))
      #foundFace(imagefile, f)
#def foundFace(imagefile, f):
      os.system("convert {image} -stroke red -fill none -draw \"rectangle {a},{b} {c},{d}\" {output}".format(
      #os.system("convert {image} -draw \"image SrcOver {a},{b} {c},{d} biglazer.png\" {output}".format(
                    image=outfile,
                    a=f.x+6,
                    b=f.y,
                    c=f.width,
                    d=f.height,
                    output=outfile))
      #center = cvPoint(f.x+f.width/2, f.y+f.height/2)
      #radius = f.height/2
      #pprint("drawing a circle with center: %s and radius: %d" % (center, radius))
      #cvCircle(image, center, radius,
      #                   cvScalar(34, 255, 255,255),
      #                   -1, # negative thickness means fill
      #                   8, 0)

