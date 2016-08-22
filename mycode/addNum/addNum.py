# -*- coding :utf-8 -*-

from random import randint
from PIL import Image, ImageDraw, ImageFont

n = randint(1,99)
text = str(n)
im = Image.open('1.bpm')
w,h = im.size
font_size = h//4

draw = ImageDraw.Draw(im)
font = ImageFont.truetype("msyh.ttf",font_size)

text_w,text_h = draw.textsize(text,font=font)
draw.text((w-text_w,0), text, fill='black', font=font)

im.save('2.jpg')