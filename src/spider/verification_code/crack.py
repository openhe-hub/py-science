# %%
# -*- coding:utf8 -*-
import os
import math
import time
import hashlib
from PIL import Image

# %%
folder_path = './src/spider/verification_code/'
image = Image.open('captcha.gif')
image = image.convert('P')
print(image.histogram())  # 颜色直方图的每一位数字都代表了在图片中含有对应位的颜色的像素的数量

# %%
his = image.histogram()
values = {}

for i in range(256):
    values[i] = his[i]

for j, k in sorted(values.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(j, k)
# red 220,grey 227
# %%
red = 220
grey = 227
image2 = Image.new('P', image.size, 255)
# 图像的尺寸，按照像素数计算，它的返回值为宽度和高度的二元组（width, height）
for x in range(image2.size[1]):
    for y in range(image2.size[0]):
        pix = image.getpixel((y, x))
        if pix == red or pix == grey:
            image2.putpixel((y, x), 0)
image2.show()
# %%
inletter = False
foundletter = False
start = 0
end = 0

letters = []

for y in range(image2.size[0]):
    for x in range(image2.size[1]):
        pix = image2.getpixel((y, x))
        if pix != 255:
            inletter = True
    if foundletter == False and inletter == True:
        foundletter = True
        start = y

    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start, end))

    inletter = False
print(letters)
# %%

count = 1
for letter in letters:
    image3 = image2.crop((letter[0], 0, letter[1], image2.size[1]))
    with open(f"{count}.gif", 'wb') as fp:
        image3.save(fp)
    count += 1

# %%
# 比较两个 python 字典类型并输出它们的相似度


class VectorCompare:
    # 计算矢量大小
    def magnitude(self, concordance):
        total = 0
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    # 计算矢量之间的 cos 值
    def relation(self, concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


# %%
# 将图片转换为矢量


def buildvector(image):
    dict = {}
    count = 0
    for i in image.getdata():
        dict[count] = i
        count += 1
    return dict


v = VectorCompare()

iconset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 加载训练集
imageset = []
for letter in iconset:
    for img in os.listdir(f'./iconset/{letter}/'):
        temp = []
        if img != "Thumbs.db" and img != ".DS_Store":
            temp.append(buildvector(Image.open(f"./iconset/{letter}/{img}")))
        imageset.append({letter: temp})


count = 0
# 对验证码图片进行切割
for letter in letters:
    image3 = image2.crop((letter[0], 0, letter[1], image2.size[1]))

    guess = []

    # 将切割得到的验证码小片段与每个训练片段进行比较
    for image in imageset:
        for x, y in image.items():
            if len(y) != 0:
                guess.append((v.relation(y[0], buildvector(image3)), x))

    guess.sort(reverse=True)
    print(guess[0])
    count += 1

# %%
