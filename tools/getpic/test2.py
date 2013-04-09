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
# todoLinks = []
# allowHost = []
# allowHost.append( htmlHelpr.getHost(beginLink) )
# allowHost.append("girl.pare.cn")
# todoLinks.append(beginLink)



# html = htmlHelpr.gGetHtml(beginLink)
# parser.feed(beginLink,html)

# items  = parser.getItems()
# for item in items:
# 	imgQueue.put(item, 1)
# print str(imgQueue.qsize()) 



# links = parser.getLinks()
# # print links;
# for link in links:
# 	if link[-4:] != 'html' and link not in todoLinks:
# 		host = htmlHelpr.getHost(link)
# 		if host not in allowHost:
# 			##纪录log
# 			continue
# 		todoLinks.append(link)

# print todoLinks

# print htmlHelpr.getHost("http://girl.pare.cn/page/4")


class Producer(threading.Thread):

	def __init__(self, lock, imgQueue, todoLinks, allowHost, maxSize = 100):
		self._lock = lock
		threading.Thread.__init__(self)
		self.imgQueue = imgQueue
		self.todoLinks = todoLinks
		self.maxSize = maxSize
		self.allowHost = allowHost
		self.doneLinks = []  #记录已经出来过的links



	def run(self):

		parser = GirlPareCn.GirlPareCn()
		htmlHelpr = HtmlHelper.HtmlHelper()


		# for beginLink in self.todoLinks:
		while self.todoLinks.qsize() > 0:
			if self._lock.acquire():
				beginLink = self.todoLinks.get()
				self.doneLinks.append(beginLink)
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


					# add link to todoLinks
					links = parser.getLinks()
					for link in links:
						if link[-4:] != 'html' and link not in self.doneLinks:
							host = htmlHelpr.getHost(link)
							if host not in self.allowHost:
								##纪录log
								continue
							# self.todoLinks.put(beginLink)	#dev
							# self.todoLinks.put(link)		#真实
					print "producer add todoLinks ---- size : "+ str(len(self.doneLinks) ) +"/" + str( self.todoLinks.qsize() + len(self.doneLinks) )
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

	def __init__(self, lock, imgQueue, todoLinks ):
		self._lock = lock
		threading.Thread.__init__(self)
		self.imgQueue = imgQueue
		self.todoLinks = todoLinks


	def run(self):
		while True:
			if self._lock.acquire():
				if self.imgQueue.qsize() <= 0 :
					#queue is empty
					if( self.todoLinks.qsize() == 0):
						print " Consumer stop ---- "
						self._lock.release()
						break
					else :
						print "todoLinks size:" + str( self.todoLinks.qsize() )
						print " Consumer suspend ----size :" + str(self.imgQueue.qsize() )
						self._lock.wait()
				else:
					item = self.imgQueue.get(1)
					# self.itemHelper.eatItem(item)
					print 'Consumer ---- size :' + str(self.imgQueue.qsize()) 
					# time.sleep(1)
					self._lock.notify()
				self._lock.release()


	def downloadPic( self, item ):
		return;







def test():
	lock = threading.Condition()
	imgQueue = Queue.Queue()  #队列
	htmlHelpr = HtmlHelper.HtmlHelper()
	# beginLink = 'http://localhost/tmp/girl13.com.html';
	beginLink = 'http://girl.pare.cn';
	todoLinks = Queue.Queue()
	allowHost = []
	allowHost.append( htmlHelpr.getHost(beginLink) )
	allowHost.append("girl.pare.cn")
	todoLinks.put(beginLink)


	#producer
	p = Producer(lock, imgQueue, todoLinks, allowHost)
	p.setDaemon(True)
	p.start()

	#consumer
	for i in range(20):
		s = Consumer(lock, imgQueue, todoLinks)
		s.setDaemon(True)
		s.start()

	time.sleep(40)


if __name__ == '__main__':
	test()