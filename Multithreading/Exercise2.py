import random
import threading
import time
import numpy as np

#CONFIG
N_OF_CUSTOMERS=30
NUM_OF_DESKS=5
CASH_DESKS=[i for i in range(NUM_OF_DESKS)]
CASH_SPEED=[np.random.poisson(5) for i in range(len(CASH_DESKS))]

#VARIABLE FOR STATS
SERVED=[0 for i in range(len(CASH_DESKS))]
TOTAL_SERVING_TIME=0
MEAN_SERVING_TIME=0


class CustomerThread(threading.Thread):
	def __init__(self, customerID, semaphore):
		"Initialize the thread"
		threading.Thread.__init__(self,name=customerID)
		self.threadSemaphore=semaphore

	def run(self):
		#Aquire the sempahore	
		self.threadSemaphore.acquire()
		#Pick the first available cash desk
		servedBy=CASH_DESKS.pop()
		#Increease the number of people served by that desk 
		SERVED[servedBy]+=1
		#Serve the customer
		time.sleep(CASH_SPEED[servedBy])
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
		customers.append(CustomerThread(i,threadSemaphore))
	#Start serving the customers
	start=time.time()
	for x in customers:
		x.start()
	for x in customers:
		x.join()
	end=time.time()

	#Calculate stats
	TOTAL_SERVING_TIME=end-start
	MEAN_SERVING_TIME=sum([SERVED[i]*CASH_SPEED[i] for i in range(NUM_OF_DESKS)])/N_OF_CUSTOMERS
	#Show stats
	print(f"STATS:\nClient served: {N_OF_CUSTOMERS}\nCustomer served by each desk: {SERVED}\nTotal serving time: {TOTAL_SERVING_TIME}\nMean serving time: {MEAN_SERVING_TIME}")

		
