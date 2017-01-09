# import libraries
import matplotlib
from PIL import Image
from numpy import *
import matplotlib.pyplot as plt
import cv2
import os
from scipy.cluster.vq import *

'''
This is the first experiment for the SIFT
'''
im_1 = cv2.imread('data/ant/image_0001.jpg',cv2.IMREAD_COLOR)
img1 = cv2.cvtColor(im_1,cv2.COLOR_BGR2GRAY)


plt.subplot(211)
plt.imshow(img1,cmap=plt.cm.gray);
plt.axis('off')

#SIFT
detector = cv2.SIFT()
keypoints_1,des1 = detector.detectAndCompute(img1,None)

img = cv2.drawKeypoints(img1,keypoints_1,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.subplot(212)
plt.imshow(img,cmap=plt.cm.gray);
plt.axis('off')
