import copy
import time
import threading
import random
from helpingFunctions import *
from multiprocessing import Process
nOfArrays=3
VARIABLE=10**4
ARRAY=[[random.randint(1,VARIABLE) for i in range(VARIABLE)] for i in range ( nOfArrays )]
POSITIONS=[None for i in range(nOfArrays)]

def sortAndFind(array):
	tofind=random.choice(array)
	bubbleSort(array)
	position=array.index(tofind) 

class myThread(threading.Thread):
	def __init__(self, threadID, array):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.array=array
		
	def run(self):
		#print("Starting sorting")
		bubbleSort(self.array)
		toFind=random.choice(self.array)
		position=binarySearch(toFind,self.array)
		#print(f"Sorted array:\n{ARRAY}")

		

if __name__ == '__main__':
	array1=copy.deepcopy(ARRAY)
	array2=copy.deepcopy(ARRAY)
	Threads=[]
	for i in range(nOfArrays):
		Threads.append(myThread(i,ARRAY[i]))
	tic=time.time()
	for i in range(nOfArrays):
		Threads[i].start()
	for i in range(nOfArrays):
		Threads[i].join()
	toc=time.time()
	print(f"Execution time mt = {toc-tic}")

	processes=[]
	for i in range(nOfArrays):
		s=Process(target=sortAndFind,args=(array1[i],))
		processes.append(s)
	tic=time.time()
	for s in processes:
		s.start()
	for s in processes:
		s.join()

	toc=time.time()
	print(f"Execution time mt = {toc-tic}")



	tic=time.time()
	for i in range(nOfArrays):
		tofind=random.choice(array2[i])
		bubbleSort(array2[i])
		position=binarySearch(tofind,array2[i])

	toc=time.time()
	print(f"Execution time = {toc-tic}")

	
	


