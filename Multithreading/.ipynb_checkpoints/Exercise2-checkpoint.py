import random
import threading
import time
import numpy as np

cashDesks=[i for i in range(5)]
cashSpeed=[random.random() for i in range(len(cashDesks))]
served=[0 for i in range(len(cashDesks))]

class CustomerThread(threading.Thread):
	#cashDesks=[i for i in range(5)]
	#cashSpeed=[random.random() for i in range(len(cashDesks))]
	#served=[0 for i in range(len(cashDesks))]
	def __init__(self, customerID, semaphore):
		"Initialize the thread"
		threading.Thread.__init__(self,name=customerID)
		self.threadSemaphore=semaphore
	def run(self):
		#self.threadSemaphore.acquire()
		#servedBy=CustomerThread.cashDesks.pop()
		#CustomerThread.served[servedBy]+=1
		#time.sleep(CustomerThread.cashSpeed[servedBy])
		#CustomerThread.cashDesks.append(servedBy)
		#self.threadSemaphore.release()
		
		self.threadSemaphore.acquire()
		servedBy=cashDesks.pop()
		served[servedBy]+=1
		time.sleep(cashSpeed[servedBy])
		cashDesks.append(servedBy)
		self.threadSemaphore.release()
		
if __name__=="__main__":
	
	
	customers=[]
	threadSemaphore=threading.Semaphore(len(cashDesks))
	for i in range(20):
		customers.append(CustomerThread(i,threadSemaphore))
	for x in customers:
		x.start()
	for x in customers:
		x.join()
	print(served)
		