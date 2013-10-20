# -*- coding: utf-8 -*-
import sys; 
if not "./core" in sys.path:
	sys.path.append("./core")
import config
import c
import DownloadHelper
import MySQLHelper
import qiyigooParser


def getJoke():
	url = 'http://www.qiyigoo.com/xiaohua/list_14_2.html';
	downloadHelper = DownloadHelper.DownloadHelper(c.PROXY);
	html = downloadHelper.gGetHtml(url)

	htmlPrase = qiyigooParser.qiyigooParser()
	htmlPrase.feed(url,html)
	links = htmlPrase.getItems()
	print links;

def main():
	getJoke();

if __name__ == '__main__':
    main()  

