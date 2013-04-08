# -*- coding: utf-8 -*-
import time
import threading
import Queue

product = 0 #产品初始化时为0
lock = threading.Condition()
class Producer(threading.Thread):
	def __init__(self, lock, num):
		self._lock = lock
		threading.Thread.__init__(self)
		self.num = num
		print "create producer num: "+ str(num)
	def run(self):
		global product
		while True:
			if self._lock.acquire():
				if product >= 20:
					self._lock.wait()
				else:
					product += 1
					print  "producer num: "+ str(self.num) + " add 1, product count=" + str(product)
					self._lock.notify()
				self._lock.release()
				time.sleep(1)
class Consumer(threading.Thread):
	def __init__(self, lock, num):
		self._lock = lock
		threading.Thread.__init__(self)
		self.num = num
		print "create Consumer num: "+ str(num)
	def run(self):
		global product
		while True:
			if self._lock.acquire():
				if product <= 2:
					self._lock.wait()
				else:
					product -= 1
					print 'Consumer num: ' + str(self.num) +' del 1 , count=' + str(product)
					self._lock.notify()
				self._lock.release()
				time.sleep(1)
def test():
	queue = Queue.Queue()
	for i in range(5):
		p = Producer(lock, queue)
		p.setDaemon(True)
		p.start()
	for i in range(5):
		s = Consumer(lock, queue)
		s.setDaemon(True)
		s.start()

	time.sleep(10)
if __name__ == '__main__':
	test()