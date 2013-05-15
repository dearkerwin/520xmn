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

	""" 
		@param lock :同步锁
		@param imgQueue: 图片队列
		@param todoLinks: 需要去处理的 link
		@param allowHost: 允许抓取的host
		@param picDownloadHelper : 图片下载helper （obj）
		@param maxImgQueueSize : 图片队列中允许最多的图片数量
		@param allowLinkSize : 允许抓取的页面的数量
	"""
	def __init__(self, lock, imgQueue, todoLinks, allowHost, picDownloadHelper, maxImgQueueSize = 100, allowLinkSize = 5000):
		self._lock = lock
		threading.Thread.__init__(self)
		self.imgQueue = imgQueue
		self.todoLinks = todoLinks
		self.maxImgQueueSize = maxImgQueueSize
		self.allowLinkSize = allowLinkSize
		self.allowHost = allowHost
		self.allLinks = []  #记录已经所有的links
		self.picDownloadHelper = picDownloadHelper



	def run(self):

		parser = GirlPareCn.GirlPareCn()
		htmlHelpr = HtmlHelper.HtmlHelper()


		# for beginLink in self.todoLinks:
		while self.todoLinks.qsize() > 0:
			if self._lock.acquire():
				beginLink = self.todoLinks.get()
				print "parse : [" + beginLink + "]"
				# self.allLinks.append(beginLink)
				html = htmlHelpr.gGetHtml(beginLink)
				parser.feed(beginLink,html)

				if self.imgQueue.qsize() >= self.maxImgQueueSize:  #超过最大限制
					print " producer stop ----size :" + str(self.imgQueue.qsize() )
					self._lock.wait()
				else:
					# add img to imgQueue
					items  = parser.getItems()
					for item in items:
						self.imgQueue.put(item, 1)
					print "producer add imgQueue ---- size :" +str(self.imgQueue.qsize()) 


					# add link to todoLinks
					if  self.todoLinks.qsize() + len(self.allLinks) <= self.allowLinkSize:
						links = parser.getLinks()
						for link in links:
							if link[-4:] != 'html' and link not in self.allLinks :
								host = htmlHelpr.getHost(link)
								if host not in self.allowHost:
									##纪录log
									self.picDownloadHelper.saveHost(host)
									continue
								else:
									
									if  len(self.allLinks) <= self.allowLinkSize:
										self.todoLinks.put(link)
										self.allLinks.append(link)		#真实
										# self.todoLinks.put(beginLink)	#dev
					print "producer add --todoLinks size : "+  str( self.todoLinks.qsize() ) + "--alllink size:" + str(len(self.allLinks))
					self._lock.notify()
				self._lock.release()


class Consumer(threading.Thread):
	""" 
		@param lock :同步锁
		@param imgQueue: 图片队列
		@param todoLinks: 需要去处理的 link
		@param picDownloadHelper : 图片下载helper （obj）
	"""
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




def main():
	
	from config import savePath
	from config import thumbPath
	# savePath = 'I:/kerwin_www/tmp'
	# thumbPath = 'I:/kerwin_www/tmp'
	beginLink = 'http://girl.pare.cn'
	picHelper = PicDownloadHelper.PicDownloadHelper(savePath,thumbPath,DBCONFIG)


	lock = threading.Condition()
	imgQueue = Queue.Queue()  #队列
	htmlHelpr = HtmlHelper.HtmlHelper()
	todoLinks = Queue.Queue()
	allowHost = []
	allowHost.append( htmlHelpr.getHost(beginLink) )
	allowHost.append("girl.pare.cn")
	todoLinks.put(beginLink)


	#producer
	p = Producer(lock, imgQueue, todoLinks, allowHost, picHelper, allowLinkSize = 1000)
	# p.setDaemon(True)
	p.start()

	#consumer
	for i in range(20):
		s = Consumer(lock, imgQueue, todoLinks, picHelper)
		# s.setDaemon(True)
		s.start()

	# time.sleep(200)


if __name__ == '__main__':
	main()