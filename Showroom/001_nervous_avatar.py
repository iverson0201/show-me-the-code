# -*- coding: utf-8 -*-  
## 描述：在图像的右上角增加一个小圆点，里面包含数字，即某用户有未读消息的效果。
### 引用：一张图片；一个字体的ttf（True Type Font）文件。

import os
from PIL import Image,ImageDraw,ImageFont

def be_nervous(path,num):
	ava = Image.open(path)
	(w,h)= ava.size	#获取尺寸
	drawer = ImageDraw.Draw(ava)
	drawer.setink("#ff0000")	#设置颜色
	div = 0.1
	fontsize = (int)((w if w<=h else h)*0.1/len(num))
	font = ImageFont.truetype("wryh.ttf", fontsize)	#使用字体
	drawer.text((w*9*div, 0), num, font=font)	#
	ava.save(os.getcwd()+"//nervous_ava.jpg", "JPEG")
	del drawer
	print "Done."

if __name__ == "__main__":
	path = raw_input("Please the path of the image:")
	num = raw_input("What\'s num you want to add?")
	be_nervous(path,num)