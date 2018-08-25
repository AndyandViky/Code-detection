#coding=utf-8
from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random
import cv2

# 验证码中的字符, 就不用汉字了

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


# number=['0', '1', '2', '3', '4']
# alphabet =[]
# ALPHABET =[]


# 验证码一般都无视大小写；验证码长度4个字符
def random_captcha_text(char_set=number + alphabet + ALPHABET, captcha_size=4):
    captcha_text = []
    for i in range(captcha_size):
        c = random.choice(char_set)
        captcha_text.append(c)
    return captcha_text


# 生成字符对应的验证码
def gen_captcha_text_and_image():
    while(1):
        image = ImageCaptcha()

        captcha_text = random_captcha_text()
        captcha_text = ''.join(captcha_text)

        captcha = image.generate(captcha_text)
        # image.write(captcha_text, captcha_text + '.jpg')  # 写到文件

        captcha_image = Image.open(captcha)
        #captcha_image.show()
        captcha_image = np.array(captcha_image)
        if captcha_image.shape==(60,160,3):
            break

    return captcha_text, captcha_image


if __name__ == '__main__':

    # =========== use pytesseract start
    # 图片的处理过程
    # from pytesseract import *
    # import PIL.ImageOps
    #
    # def initTable(threshold=140):
    #     table = []
    #     for i in range(256):
    #         if i < threshold:
    #             table.append(0)
    #         else:
    #             table.append(1)
    #     return table
    # im = Image.open('./3223.jpg')
    # im = im.convert('L')
    # binaryImage = im.point(initTable(), '1')
    # im1 = binaryImage.convert('L')
    # im2 = PIL.ImageOps.invert(im1)
    # im3 = im2.convert('1')
    # im4 = im3.convert('L')
    # # 将图片中字符裁剪保留
    # box = (30, 10, 90, 28)
    # region = im4.crop(box)
    # # 将图片字符放大
    # out = region.resize((120, 38))
    # asd = pytesseract.image_to_string(im)
    # print asd
    # print (out.show())
    # =========== use pytesseract start

    text, im = gen_captcha_text_and_image()
    # images = Image.open("CheckCode.gif").save("CheckCode.png")
    # cvImage = cv2.imread("CheckCode.png")
    gray = np.mean(im, -1)
    print(gray)

    print(im.shape)
    print(gray.shape)
    f = plt.figure()
    ax = f.add_subplot(111)
    ax.text(0.1, 0.9, text, ha='center', va='center', transform=ax.transAxes)
    plt.imshow(im)

    plt.show()