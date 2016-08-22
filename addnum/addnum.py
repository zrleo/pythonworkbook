#-*- coding:utf-8 -*-
"""
给头像右上角增加数字提示，ex：微信头像出现的未读消息
"""
import random
from PIL import Image,ImageDraw,ImageFont

num = random.randint(1,99)
text = str(num)#随机生成1-99之间的整数，并将整数转化为string类型，因为在图片中填充颜色时只能填充string类型的


im = Image.open('1.bmp')
w,h = im.size
font_size = h//5 #字体大小

draw = ImageDraw.Draw(im)
font = ImageFont.truetype("Arial.ttf",font_size)

text_w,text_h = draw.textsize(text,font = font)
draw.text((w-text_w,1000),text,fill = 'green',font=font)#第一个参数代表填充数字的位置，
#第二个参数  fill代表填充颜色，第四个参数代表要填充的字体内容和字体样式

im.save('2.bmp')
