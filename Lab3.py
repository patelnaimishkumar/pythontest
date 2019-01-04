import threading
import time

def printTest(threadName,deleay):
    count=0
    while count<5:
        time.sleep(deleay)
        count += 1
        print(threadName,"-----------",time.time())


if __name__=="__main__":
 t1=threading.Thread(target=printTest,args=("a",1))
 t2=threading.Thread(target=printTest,args=("b",2))
 t1.start()
 t2.start()

 t1.join()
 t2.join()
 print("done")