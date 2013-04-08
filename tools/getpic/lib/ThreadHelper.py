# -*- coding: utf-8 -*-
"""
初步简单线程控制类 包含 producer 和 Consumer
    注：需要指定 lock, queue, itemHelper
    ItemHelper 是一个类，负责item 的生产 和 处理 
     至少需要两个函数， 函数名为 createItem 和 eatItem

version 1.0
author kerwin
"""
import time
import threading
import Queue


class Producer(threading.Thread):

	def __init__(self, lock, queue, itemHelper, maxSize = 100):
		self._lock = lock
		threading.Thread.__init__(self)
		self.queue = queue
		self.itemHelper = itemHelper
		self.maxSize = maxSize


	def run(self):
		while True:
			if self._lock.acquire():
				if self.queue.qsize() >= self.maxSize:  #超过最大限制
					self._lock.wait()
				else:
					item = self.itemHelper.createItem()
					self.queue.put(item, 1)
					print 'producer ---- size :' + str(self.queue.qsize()) 
					self._lock.notify()
				self._lock.release()


class Consumer(threading.Thread):

	def __init__(self, lock, queue, itemHelper):
		self._lock = lock
		threading.Thread.__init__(self)
		self.queue = queue
		self.itemHelper = itemHelper


	def run(self):
		global queue
		while True:
			if self._lock.acquire():
				item = self.queue.get(1)
				self.itemHelper.eatItem(item)
				print 'Consumer ---- size :' + str(self.queue.qsize()) 
				self._lock.release()



class ItemHelper():
	def __init__(self):
		self.num = 0

	def createItem(self):
		self.num =  self.num + 1
		item = ["http://baidu.com/"+str(self.num), [ "a", "b", "c"]]
		return item

	def eatItem(self, item):
		src = item[0]
		tag = item[1]
		print "src: " + src + "; tag " 
		print tag


def test():
	lock1 = threading.Condition()
	queue = Queue.Queue()  #队列
	itemHelper  = ItemHelper()
	for i in range(5):
		p = Producer(lock1, queue, itemHelper)
		p.setDaemon(True)
		p.start()
	for i in range(5):
		s = Consumer(lock1, queue, itemHelper)
		s.setDaemon(True)
		s.start()
	time.sleep(5)

if __name__ == '__main__':
	test()