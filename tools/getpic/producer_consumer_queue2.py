from threading import Thread
from Queue import Queue
from time import sleep,ctime
from random import randint
 
class MyThread(Thread):
    def __init__(self,func,args,name=''):
        Thread.__init__(self)
        self.func=func
        self.name=name
        self.args=args
 
    def get_result(self):
        return self.res
 
    def run(self):
        print self.name,"starting at:",\
              ctime()
        self.res=apply(self.func,self.args)
        print self.name,"finished at:",\
              ctime()
 
 
def write_queue(queue):
    print "producing object to queue..."
    queue.put('xxx',1)
    print "size now",queue.qsize()
 
def read_queue(queue):
    print "consumed object from queue..."
    queue.get(1)
    print "size now",queue.qsize()
 
def writer(queue,loops):
    for i in range(loops):
        write_queue(queue)
        sleep(randint(1,3))
 
def reader(queue,loops):
    for i in range(loops):
        read_queue(queue)
        sleep(randint(3,5))
 
funcs=[writer,reader]
nfuncs=range(len(funcs))
 
def main():
    nloops=randint(2,5)
    q=Queue(32)
    threads=[]
    for i in nfuncs:
        t=MyThread(funcs[i],(q,nloops),\
                   funcs[i].__name__)
        threads.append(t)
 
    for i in nfuncs:
        threads[i].start()
 
    for i in nfuncs:
        threads[i].join()
 
    print "all down"
 
if __name__=="__main__":
    main()