# -*- coding: utf-8 -*-
import sys; 
if not "./lib" in sys.path:
    sys.path.append("./lib")
if not "./page_rule" in sys.path:
    sys.path.append("./page_rule")
if not "./core" in sys.path:
    sys.path.append("./core")  

import UrlParser
import re
import HtmlHelper
import Queue  
import GirlPareCn
import PicDownloadHelper
import datetime
import threading


try:
    from mysql_setting import DBCONFIG
except:
    print "import dbConfig failure!"


def getPicByUrl( url, savePath, thumbPath ):
	picHelper = PicDownloadHelper.PicDownloadHelper(savePath,thumbPath,DBCONFIG)
	parser = GirlPareCn.GirlPareCn()
	htmlHelpr = HtmlHelper.HtmlHelper()
	print "begin : [" + url + "]"
	html = htmlHelpr.gGetHtml(url)
	parser.feed(url,html)
	items  = parser.getItems()
	for item in items:
		picHelper.saveItem(item)
	print "--end : [" + url + "]"

			
def main():
	from config import savePath
	from config import thumbPath
	# savePath = 'I:/kerwin_www/tmp'
	# thumbPath = 'I:/kerwin_www/tmp'
	print "begin-----"+ str(datetime.date.today())
	url  = "http://girl.pare.cn"
	pageBaseUrl = "http://girl.pare.cn/page/"

	getPicByUrl( url, savePath , thumbPath)
	for i in range(2, 3):
		url = pageBaseUrl + str(i);
		getPicByUrl( url, savePath, thumbPath)
	print "end-----"+str(datetime.date.today())
	

if __name__ == '__main__':
	main()