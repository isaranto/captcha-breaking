from __future__ import division
import numpy as np
import os
from PIL import Image,ImageFilter
from sklearn.feature_extraction import image


class Classifier:
    def __init__(self, train, test):
        #build train set
        #build test set
        #fit
        #predict
        pass

    def create_array(self, image):
        img = Image.open(image)
        return np.array(img)


path = 'data/sample/segments/0/'
"""
for im in os.listdir(path):
    img = Image.open(path+im)
    patches = image.extract_patches_2d(np.array(img), (2, 2), max_patches=2, random_state=0)
    print patches.shape
    reconstructed = image.reconstruct_from_patches_2d(patches, (2, 2,2))
    img = Image.fromarray(patches, 'L')
    img.save('my.png')
    img.show() """
img = Image.open(path+'0.png')
im_array = np.array(img)
print im_array.shape
patches = image.extract_patches_2d(im_array, (5, 5), max_patches=400, random_state=0)
print patches.shape
print patches
reconstructed = image.reconstruct_from_patches_2d(patches, (80, 35))
img = Image.fromarray(reconstructed, 'L')
img.save('my.png')
img.show()


