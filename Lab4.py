import threading
import time

def printTest(threadName,deleay):
    count=0
    while count<5:
        time.sleep(deleay)
        count += 1
        print(threadName,"-----------",time.time())

class MyThread(threading.Thread):
    def __init__(self,name,deelay):
        threading.Thread.__init__(self)
        self.name=name
        self.delay=deelay
    def run(self):
        printTest(self.name,self.delay)



if __name__=="__main__":
 t1=MyThread("a",1)
 t2=MyThread("b",2)
 t3=MyThread("c",3)

 t1.start()
 t2.start()
 t3.start()

 print(threading.currentThread())
 print(threading.enumerate())
 print(threading.activeCount())

 t1.join()
 t2.join()
 t3.join()
 print("done")