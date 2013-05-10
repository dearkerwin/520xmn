# -*- coding: utf-8 -*-
import sys; 
if not "../lib" in sys.path:
    sys.path.append("../lib") 

import UrlParser
import re
import HtmlHelper
import Queue  

""" 针对http://girl.pare.cn/ 的规则"""
class GirlPareCn(UrlParser.UrlParser):

	""" 返回items ,格式如下：["imgsrc", ["tag1", "tag2"]]"""
	def getItems(self ):
		rex = r'''[\s\S]*?column-post[\s\S]*?<img.*?src\s*=\s*["'\s]*([^"']+?)["'\s]+.*?>[\s\S]*?div[\s\S]*?span>([\s\S]*?)div[\s\S]*?div[\s\S]*?div'''
		#获取src 和 包含tag 的html代码
		url = re.findall(rex, self.data, re.S|re.I)
		items = []
		for u in url:
			src = self.gGetAbslLink(u[0])
			tag = u[1]
			rex1 = r'''<a[^>]+?>([^<]+?)</a>'''
			#从tag的html代码 中 获取真正的tag
			t = re.findall(rex1, tag, re.S|re.I)
			pic = {"src":src}
			item = [pic,t]
			items.append(item)
		return items
