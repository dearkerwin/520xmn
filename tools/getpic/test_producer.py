# -*- coding: utf-8 -*-
import sys; 
if not "./lib" in sys.path:
    sys.path.append("./lib") 

import ThreadHelper
import time
import threading
import Queue


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
		p = ThreadHelper.Producer(lock1, queue, itemHelper)
		p.setDaemon(True)
		p.start()
	for i in range(5):
		s = ThreadHelper.Consumer(lock1, queue, itemHelper)
		s.setDaemon(True)
		s.start()
	time.sleep(5)


if __name__ == '__main__':
	test()