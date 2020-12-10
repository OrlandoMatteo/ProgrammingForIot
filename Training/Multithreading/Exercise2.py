import random
import threading
import time
import numpy as np
import json

#CONFIG
N_OF_CUSTOMERS=30
NUM_OF_DESKS=5
CASH_DESKS=[i for i in range(NUM_OF_DESKS)]
CUSTOMER_SPEED=[np.random.poisson(5) for i in range(N_OF_CUSTOMERS)]

#VARIABLE FOR STATS
SERVED=dict([[i,0] for i in range(len(CASH_DESKS))])
BUSY_FOR=dict([[i,0] for i in range(len(CASH_DESKS))])
TOTAL_SERVING_TIME=0
MEAN_SERVING_TIME=0


class CustomerThread(threading.Thread):
	def __init__(self, customerID,serving_time, semaphore):
		"Initialize the thread"
		threading.Thread.__init__(self,name=customerID)
		self.serving_time=serving_time
		self.threadSemaphore=semaphore

	def run(self):
		#Aquire the sempahore	
		self.threadSemaphore.acquire()
		#Pick the first available cash desk
		servedBy=CASH_DESKS.pop(0)
		#Increease the number of people served by that desk 
		SERVED[servedBy]+=1
		BUSY_FOR[servedBy]+=self.serving_time
		#Serve the customer
		time.sleep(self.serving_time)
		#Free the desk
		CASH_DESKS.append(servedBy)
		self.threadSemaphore.release()
		
if __name__=="__main__":
	#Empty queue
	customers=[]
	#Define the semaphore
	threadSemaphore=threading.Semaphore(len(CASH_DESKS))
	#Fill the queue
	for i in range(N_OF_CUSTOMERS):
		customers.append(CustomerThread(i,CUSTOMER_SPEED[i], threadSemaphore))
	#Start serving the customers
	start=time.time()
	for x in customers:
		x.start()
	for x in customers:
		x.join()
	end=time.time()

	#Calculate stats
	TOTAL_SERVING_TIME=end-start
	AVG_PER_DESK=[BUSY_FOR[i]/SERVED[i] for i in range(NUM_OF_DESKS)]
	print(f"STATS:Total serving time: {TOTAL_SERVING_TIME}")
	print (f"Customer per desk:{json.dumps(SERVED,indent=4)}")
	print (f"Average time per desk:{AVG_PER_DESK}")

		
