from __future__ import division
from PIL import ImageFilter, Image
import numpy as np
import os

class ImageCleaner:
    def __init__(self, path, image_name):
        self.path = path
        self.image_name = image_name
        self.im = Image.open(path+"initial/"+image_name)

    def clean_captcha(self):
        self.im = self.im.convert('L').filter(ImageFilter.GaussianBlur(radius = 2))
        self.im = self.im.point(lambda x: 255 if x > 190 or x == 0 else x)
        self.im = self.im.point(lambda x: 0 if x < 255 else 255)
        w, h = self.im.size
        data = self.im.load()
        jcolors = [sum(data[i, j] for j in range(h)) for i in range(w)]
        for i in range(w):
            if jcolors[i]/(80*255) > 0.95:
                jcolors[i] = 0
        nonzero = np.nonzero(np.array(jcolors))[0]
        begin = True
        intervals = []
        for i in range(len(nonzero)):
            try:
                if begin:
                    if nonzero[i+1]-nonzero[i] == 1:
                        start = nonzero[i]
                        begin = False
                else:
                    if nonzero[i+1]-nonzero[i] > 1:
                        end = nonzero[i]
                        intervals.append([start,end])
                        begin = True
            except IndexError:
                if not begin:
                    intervals.append((start, nonzero[-1]))
        print intervals
        intervals = self.segmentation(intervals)
        print intervals
        os.mkdir(self.path+"segments/"+self.image_name[-5])
        for i, s in enumerate(intervals):
            img2 = self.im.crop((s[0], 0, s[1], 80))
            img2.save(self.path+"segments/"+self.image_name[-5]+"/"+str(i)+".png")
        self.im.save(self.path+"clean/"+self.image_name)

    def segmentation(self, intervals):
        new_intervals = []
        for s in intervals:
            if s[1] - s[0] < 8:
                continue
            if s[1] - s[0] > 110:
                part = (s[1]-s[0])/4
                new_intervals.append((s[0], s[0]+part))
                new_intervals.append((s[0]+part, s[0]+2*part))
                new_intervals.append((s[0]+2*part, s[0]+3*part))
                new_intervals.append((s[0]+3*part, s[1]))
            elif s[1] - s[0] > 90:
                part = (s[1]-s[0])/3
                new_intervals.append((s[0], s[0]+part))
                new_intervals.append((s[0]+part, s[0]+2*part))
                new_intervals.append((s[0]+2*part, s[1]))
            elif s[1] - s[0] > 40:
                part = (s[1]-s[0])/2
                new_intervals.append((s[0], s[0]+part))
                new_intervals.append((s[0]+part, s[1]))
            else:
                new_intervals.append((s[0], s[1]))
        return new_intervals


if __name__ == "__main__":
    """images_path = 'data/images/'
    captchas = os.listdir(images_path+"initial/")
    for captcha in captchas:
        cleaner = ImageCleaner(images_path, captcha)
        cleaner.clean_captcha()"""
    #train_files = ['data/images/initial/%d.png' % (i,) for i in range(10)]
    cleaner = ImageCleaner('data/sample/', '1.png')
    cleaner.clean_captcha()