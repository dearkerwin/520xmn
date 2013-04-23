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
import time
import threading


try:
    from mysql_setting import DBCONFIG
except:
    print "import dbConfig failure!"




class Producer(threading.Thread):

	def __init__(self, lock, imgQueue, todoLinks, allowHost, picDownloadHelper, maxSize = 100):
		self._lock = lock
		threading.Thread.__init__(self)
		self.imgQueue = imgQueue
		self.todoLinks = todoLinks
		self.maxSize = maxSize
		self.allowHost = allowHost
		self.doneLinks = []  #记录已经出来过的links
		self.picDownloadHelper = picDownloadHelper



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
								self.picDownloadHelper.saveHost(host)
								continue
							else:
								# self.todoLinks.put(beginLink)	#dev
								self.todoLinks.put(link)		#真实
					print "producer add todoLinks ---- size : "+ str(len(self.doneLinks) ) +"/" + str( self.todoLinks.qsize() + len(self.doneLinks) )
					self._lock.notify()
				self._lock.release()


class Consumer(threading.Thread):

	def __init__(self, lock, imgQueue, todoLinks, picDownloadHelper ):
		self._lock = lock
		threading.Thread.__init__(self)
		self.imgQueue = imgQueue
		self.todoLinks = todoLinks
		self.picDownloadHelper = picDownloadHelper

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
					self.picDownloadHelper.saveItem(item)
					print 'Consumer ---- size :' + str(self.imgQueue.qsize()) 
					self._lock.notify()
				self._lock.release()




def test():
	

	savePath = 'I:/kerwin_www/tmp'
	beginLink = 'http://girl.pare.cn'
	picHelper = PicDownloadHelper.PicDownloadHelper(savePath,DBCONFIG)


	lock = threading.Condition()
	imgQueue = Queue.Queue()  #队列
	htmlHelpr = HtmlHelper.HtmlHelper()
	todoLinks = Queue.Queue()
	allowHost = []
	allowHost.append( htmlHelpr.getHost(beginLink) )
	allowHost.append("girl.pare.cn")
	todoLinks.put(beginLink)


	#producer
	p = Producer(lock, imgQueue, todoLinks, allowHost, picHelper)
	# p.setDaemon(True)
	p.start()

	#consumer
	for i in range(20):
		s = Consumer(lock, imgQueue, todoLinks, picHelper)
		# s.setDaemon(True)
		s.start()

	# time.sleep(200)


if __name__ == '__main__':
	test()