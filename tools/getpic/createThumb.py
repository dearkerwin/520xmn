# -*- coding: utf-8 -*-
import sys; 
if not "./lib" in sys.path:
    sys.path.append("./lib") 

import PicHelper
import os



def create(path, savePath): 
	if not os.path.isdir(path):
		print path + " is not exist"
		return False
	if not os.path.isdir(savePath):
		print savePath + " is not exist"
		return False

	picHelper = PicHelper.PicHelper()
	files = os.listdir(path)
	count = len(files)
	i = 0 
	for f in files:
		if os.path.isfile( path + f ):
			i = i + 1
			if picHelper.createWidthThumb(path, f , savePath,  260 , 85 ):
				print "( " + str(i) + "/" + str(count) + ")",

	if i == count:
		return True

	return False
			
		

	





def main():
	path =  'i:/kerwin_www/static/pic/2013/5/'
	savePath =  'i:/kerwin_www/static/thumb85_new/2013/5/'
	create(path, savePath)
	



if __name__ == '__main__':
	main()

