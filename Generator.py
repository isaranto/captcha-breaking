from io import BytesIO
from captcha.image import ImageCaptcha
import random, string
import json
from string import ascii_lowercase


class LetterGenerator:
    def __init__(self, num_of_letters):
        self.image = ImageCaptcha(fonts=['data/fonts/Ubuntu-B.ttf'], height=80, width=80, font_sizes=[70])
        self.num_of_letters = num_of_letters

    def make_images(self):
        ground_truth={}
        for i in range(self.num_of_letters):
            for c in ascii_lowercase:
                #data = self.image.generate(c)
                self.image.write(c, "data/letters/initial/"+c+"_"+str(i)+'.png')
            ground_truth[i] = c
        with open('data/letters_ground_truth.txt', 'w') as fp:
            for i, c in ground_truth.iteritems():
                fp.write(str(i) + ","+c+"\n")

    def randomword(self, length):
       return ''.join(random.choice(string.lowercase) for i in range(length))


class CaptchaGenerator:
    def __init__(self, length, num_of_images):
        self.image = ImageCaptcha(fonts=['data/fonts/Ubuntu-B.ttf'], height=80, width=200, font_sizes=[70])
        self.length = length
        self.num_of_images = num_of_images

    def make_images(self):
        ground_truth={}
        for i in range(self.num_of_images):
            word = self.randomword(self.length)
            #data = self.image.generate(word)
            self.image.write(word, "data/images/initial/"+str(i)+'.png')
            ground_truth[i] = word
        with open('data/ground_truth.txt', 'w') as fp:
            for i, word in ground_truth.iteritems():
                fp.write(str(i) + ","+word+"\n")

    def randomword(self, length):
       return ''.join(random.choice(string.lowercase) for i in range(length))


if __name__=="__main__":
    generator = CaptchaGenerator(5, 2000)
    generator.make_images()
    gen = LetterGenerator(1000)
    gen.make_images()