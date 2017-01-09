import cv2
from scipy.cluster.vq import *

class Vocabuary(object):
    def __init__(self,name):
        self.name = name
        self.voc = []
        self.features = []
        self.descriptors = None
        self.nbr_words = 0
        self.nbr_image = 0

    def extract_SIFT(self,im):
        detector = cv2.SIFT()
        keypoints,des = detector.detectAndCompute(im,None)
        return des

    def get_descriptors(self,data):
        '''Train a bag of words'''

        #features = []
        nbr_image = 0

        #read the features from the dir
        for path in data:
            im = cv2.imread(path,cv2.IMREAD_COLOR)
            gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

            des = self.extract_SIFT(gray)
            feature = whiten(des)
            self.features.append(feature)

            self.nbr_image += 1

        self.descriptors = vstack(tuple(self.features))

    def train(self,k):

        '''k-means'''
        self.voc,dicstortion = kmeans(self.descriptors,k)
        self.nbr_words = self.voc.shape[0]

        imwords = zeros((self.nbr_image,self.nbr_words))
        for i in range(self.nbr_image):
            imwords[i] = self.project(features[i])

        return imwords

    def project(self,descriptors):
        '''Project descriptors on the vocabulary
        to creat a histogram of words'''

        imhist = zeros((self.nbr_words))
        words,distance = vq(descriptors,self.voc)

        for w in words:
            imhist[w] += 1

        return imhist
