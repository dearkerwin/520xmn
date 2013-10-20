# -*- coding: utf-8 -*-
"""
 针对 http://www.qiyigoo.com/xiaohua/list_14_1.html  建立的规则
"""

import HtmlParser
class qiyigooParser(HtmlParser.HtmlParser):

	""" 返回这个页面上符合规则的数据 """
	def getItems(self):

		items = []
		items.append("ssss")
		return items