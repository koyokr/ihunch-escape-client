import requests
import numpy as py
import cv2
from PyQt5 import QtGui, QtCore

import ssl

#print(ssl.OPENSSL_VERSION)

cam = cv2.VideoCapture(0)

# im = cv2.imread('C:/Users/user/Desktop/camera/20200811-093116.png')
# im_resize = cv2.resize(im, (500, 500))

ret, image = cam.read()

is_success, im_buf_arr = cv2.imencode(".jpg", image)
byte_im = im_buf_arr.tobytes()

s = requests.session()
r = s.post('http://api.ihunch.koyo.io/upload', files={'file': byte_im})

print(repr(r))
print(repr(r.text))