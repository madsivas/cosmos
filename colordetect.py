import os
from opencv.cv import *
#import cv2
from opencv.highgui import *
from shutil import copy
from pprint import pprint

purpleMin = cvScalar(128, 30, 45)
purpleMax = cvScalar(138, 180, 165)

pinkMin = cvScalar(139, 0, 0)
pinkMax = cvScalar(172, 180, 180)

blueMin = cvScalar(86, 60, 82)
blueMax = cvScalar(132, 180, 180)

redMin = cvScalar(173, 0, 0)
redMax = cvScalar(180, 180, 180)

color_chart = {"purple":{"min":purpleMin, "max":purpleMax},
               "pink":{"min":pinkMin, "max":pinkMax},
               "red":{"min":redMin, "max":redMax}}

imagefilepath = "/home/madhu/ws/cosmos/cosmos/static/uploads"
pink_tulips = "P1050310.JPG"
red_poppies = "P1060140.JPG"
blue_asters = "P1060143.JPG"
purple_lupine = "P1100172.JPG"
infile = blue_asters

def detect_color(imagefilename):
    imagefile = os.path.join(imagefilepath, imagefilename)
    #outfile = os.path.join('/home/madhu/ws/cosmos/cosmos/static/out/', imagefilename)
    outpath = '/home/madhu/ws/cosmos/cosmos/static/out/'
    
    #copy(imagefile, outfile)
    
    image = cvLoadImage(imagefile)
    grayscale = cvCreateImage(cvSize(image.width, image.height), 8, 1)
    imgHSV = cvCreateImage(cvSize(image.width, image.height), 8, 3)
    cvCvtColor(image, imgHSV, CV_BGR2HSV)
    
    # check for purple:
    imgThreshed = cvCreateImage(cvSize(image.width, image.height), 8, 1) # output image that will be returned
    # do the thresholding
    cvInRangeS(imgHSV, purpleMin, purpleMax, imgThreshed)
    colorPath = os.path.join(outpath, "purple")
    outfile = os.path.join(colorPath, imagefilename)
    cvSaveImage(outfile,imgThreshed)
    
    # check for pink:
    imgThreshed = cvCreateImage(cvSize(image.width, image.height), 8, 1) # output image that will be returned
    # do the thresholding
    cvInRangeS(imgHSV, pinkMin, pinkMax, imgThreshed)
    colorPath = os.path.join(outpath, "pink")
    outfile = os.path.join(colorPath, imagefilename)
    cvSaveImage(outfile,imgThreshed)
    
    # check for red:
    imgThreshed = cvCreateImage(cvSize(image.width, image.height), 8, 1) # output image that will be returned
    # do the thresholding
    cvInRangeS(imgHSV, redMin, redMax, imgThreshed)
    colorPath = os.path.join(outpath, "red")
    outfile = os.path.join(colorPath, imagefilename)
    cvSaveImage(outfile,imgThreshed)
    
    
    # check for blue:
    imgThreshed = cvCreateImage(cvSize(image.width, image.height), 8, 1) # output image that will be returned
    # do the thresholding
    cvInRangeS(imgHSV, blueMin, blueMax, imgThreshed)
    colorPath = os.path.join(outpath, "blue")
    outfile = os.path.join(colorPath, imagefilename)
    cvSaveImage(outfile,imgThreshed)
    
    #pprint(imgThreshed)
    #storage = cvCreateMemStorage()
    
    #purpleColor = (138, 100, 100) # HSV color purpl-ish
    
    #contours = cvFindContours(grayscale, storage, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE)
    #cvDrawContours(imgThreshed, contours, purpleColor, purpleColor, 3, thickness=1, lineType=8, offset=(0, 0))



# uncomment to run stand-alone
#detect_color(infile)

