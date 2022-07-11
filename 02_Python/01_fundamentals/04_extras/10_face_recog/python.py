import cv2
import sys

# Get user supplied values
imagePath = "abba.png"
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)