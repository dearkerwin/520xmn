# -*- coding: utf-8 -*-
"""
图形处理的 类

version 1.0
author kerwin
"""
import Image
import os, sys
import time

class PicHelper():
	def createThumbnails(self, file_path, img_name, save_path,  size):
		try:
			im = Image.open( file_path +  img_name)
			im.thumbnail(size)
			im.save(save_path + img_name, quality=85)
		except IOError:
			print "cannot create thumbnail for", img_name

	""" 
		生成指定宽度的图片，保持原来的长宽比
	"""
	def createWidthThumb( self, file_path, img_name, save_path, width, quality=85):
		print file_path + img_name
		im = Image.open( file_path + img_name)
		im_w, im_h = im.size
		if im_w <= width:
			return

		height = int((float(im_h)/im_w)* width)
		size = width, height
		im.thumbnail(size)
		im.save(save_path + img_name, quality=quality)
		

	""" 
		生成指定size的图片，会截取中间的一部分
	"""
	def createCutThumb(self, file_path, img_name, save_path, size):
		im = Image.open( file_path + img_name)
		width, height = im.size
		if width == height:
			region = im
		else:
			if width > height:
				delta = (width - height)/2
				box = (delta, 0, delta+height, height)
			else:
				delta = (height - width)/2
				box = (0, delta, width, delta+width) 
			region = im.crop(box)

		filename = save_path + img_name
		thumb = region.resize((size[0],size[1]), Image.ANTIALIAS)
		thumb.save(filename, quality=100)

	""" 获取图片的尺寸"""
	def getImageSize(self, file_path, img_name):
		if file_path[ len(file_path) - 1 ] != '/':
			file_path = file_path + "/"
		imagePath = file_path + img_name
		im = Image.open(imagePath)
		return im.size

def main():
	picHelper = PicHelper()
	file_path = "F:/www/pic/tmp/"
	img_name = "2012-12-06-10-46-58_fw554.jpg"
	save_path = "F:/www/pic/thumb/"
	picHelper.createWidthThumb(file_path, img_name, save_path,  260 )
	
	print(os.path.splitext(file_path + img_name))


if __name__ == '__main__':
	main()