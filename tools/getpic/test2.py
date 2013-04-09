# -*- coding: utf-8 -*-
import sys; 
if not "./lib" in sys.path:
    sys.path.append("./lib")
if not "./page_rule" in sys.path:
    sys.path.append("./page_rule")  

import UrlParser
import re
import HtmlHelper
import Queue  
import GirlPareCn
# import ThreadHelper
import time
import threading


# def getPicAndTag( content ):
# 	rex = r'''[\s\S]*?column-post[\s\S]*?<img.*?src\s*=\s*["'\s]*([^"']+?)["'\s]+.*?>[\s\S]*?div[\s\S]*?span>([\s\S]*?)div[\s\S]*?div[\s\S]*?div'''
# 	#获取src 和 包含tag 的html代码
# 	url = re.findall(rex, content, re.S|re.I)
# 	items = []
# 	for u in url:
# 		src = u[0]
# 		tag = u[1]
# 		rex1 = r'''<a[^>]+?>([^<]+?)</a>'''
# 		#从tag的html代码 中 获取真正的tag
# 		t = re.findall(rex1, tag, re.S|re.I)
# 		item = [src,t]
# 		items.append(item)
# 	return items




# imgQueue = Queue.Queue()
# parser = GirlPareCn.GirlPareCn()
# htmlHelpr = HtmlHelper.HtmlHelper()
# beginLink = 'http://localhost/tmp/girl13.com.html';
# allLinks = []
# allowHost = []
# allowHost.append( htmlHelpr.getHost(beginLink) )
# allowHost.append("girl.pare.cn")
# allLinks.append(beginLink)



# html = htmlHelpr.gGetHtml(beginLink)
# parser.feed(beginLink,html)

# items  = parser.getItems()
# for item in items:
# 	imgQueue.put(item, 1)
# print str(imgQueue.qsize()) 



# links = parser.getLinks()
# # print links;
# for link in links:
# 	if link[-4:] != 'html' and link not in allLinks:
# 		host = htmlHelpr.getHost(link)
# 		if host not in allowHost:
# 			##纪录log
# 			continue
# 		allLinks.append(link)

# print allLinks

# print htmlHelpr.getHost("http://girl.pare.cn/page/4")


class Producer(threading.Thread):

	def __init__(self, lock, imgQueue, allLinks, allowHost,  maxSize = 100):
		self._lock = lock
		threading.Thread.__init__(self)
		self.imgQueue = imgQueue
		self.allLinks = allLinks
		self.maxSize = maxSize
		self.allowHost = allowHost



	def run(self):

		parser = GirlPareCn.GirlPareCn()
		htmlHelpr = HtmlHelper.HtmlHelper()

		for beginLink in self.allLinks:
			if self._lock.acquire():
				html = htmlHelpr.gGetHtml(beginLink)
				parser.feed(beginLink,html)

				if self.imgQueue.qsize() >= self.maxSize:  #超过最大限制
					print " producer stop ----size :" + str(self.imgQueue.qsize() )
					self._lock.wait()
				else:
					# add img to imgQueue
					items  = parser.getItems()
					for item in items:
						self.imgQueue.put(item, 1)
					print "producer add imgQueue ---- size :" +str(self.imgQueue.qsize()) 


					# add link to allLinks
					links = parser.getLinks()
					for link in links:
						if link[-4:] != 'html' and link not in self.allLinks:
							host = htmlHelpr.getHost(link)
							if host not in self.allowHost:
								##纪录log
								continue
							# self.allLinks.append(beginLink)	
							self.allLinks.append(link)
			
					print "producer add allLinks ---- size :" + str( len(self.allLinks) )
					self._lock.notify()
				self._lock.release()



		# while True:
		# 	if self._lock.acquire():
		# 		if self.queue.qsize() >= self.maxSize:  #超过最大限制
		# 			self._lock.wait()
		# 		else:
		# 			item = self.itemHelper.createItem()
		# 			self.queue.put(item, 1)
		# 			print 'producer ---- size :' + str(self.queue.qsize()) 
		# 			self._lock.notify()
		# 		self._lock.release()

class Consumer(threading.Thread):

	def __init__(self, lock, imgQueue):
		self._lock = lock
		threading.Thread.__init__(self)
		self.imgQueue = imgQueue


	def run(self):
		while True:
			if self._lock.acquire():
				if self.imgQueue.qsize() <= 0 :
					#queue is empty
					#介绍条件  当 allLink is empty break; 未完成，  (前提条件，把allLink 换成一个queue 或者增加一个变量)
					print " Consumer stop ----size :" + str(self.imgQueue.qsize() )
					self._lock.wait()
				else:
					item = self.imgQueue.get(1)
					# self.itemHelper.eatItem(item)
					print 'Consumer ---- size :' + str(self.imgQueue.qsize()) 
					# time.sleep(1)
					self._lock.notify()
				self._lock.release()


	def downloadPic( self, item ):









def test():
	lock = threading.Condition()
	imgQueue = Queue.Queue()  #队列
	htmlHelpr = HtmlHelper.HtmlHelper()
	beginLink = 'http://localhost/tmp/girl13.com.html';
	allLinks = []
	allowHost = []
	allowHost.append( htmlHelpr.getHost(beginLink) )
	allowHost.append("girl.pare.cn")
	allLinks.append(beginLink)

	#producer
	p = Producer(lock, imgQueue, allLinks, allowHost)
	p.setDaemon(True)
	p.start()

	#consumer
	for i in range(20):
		s = Consumer(lock, imgQueue)
		s.setDaemon(True)
		s.start()

	time.sleep(60)


if __name__ == '__main__':
	test()