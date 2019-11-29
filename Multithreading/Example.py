import time
import threading
import random
from helpingFunctions import *
nOfArrays=4
THREADLOCKS=[threading.Lock() for i in range(nOfArrays)]
VARIABLE=10**4
ARRAY=[[random.randint(1,VARIABLE) for i in range(VARIABLE)] for i in range ( nOfArrays )]
POSITIONS=[None for i in range(nOfArrays)]

class SortThread(threading.Thread):
	def __init__(self, threadID, array):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.array=array
		
	def run(self):
		THREADLOCKS[self.threadID].acquire()
		#print("Starting sorting")
		bubbleSort(self.array)
		#print(f"Sorted array:\n{ARRAY}")
		THREADLOCKS[self.threadID].release()

class BinarySearchThread(threading.Thread):
	"""docstring for BinarySearchThread"""
	def __init__(self, threadID,array):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.toFind=random.choice(array)
		self.startingPoint=len(array)//2
		
	def run(self):
		THREADLOCKS[self.threadID].acquire()
		#print(f"Finding {self.toFind}")
		POSITIONS[self.threadID]=binarySearch(self.toFind,ARRAY[self.threadID])
		#print(f"{self.toFind} found at position {POSITIONS[self.threadID]}")	
		THREADLOCKS[self.threadID].release()







		

if __name__ == '__main__':
	#print(f"Original array:\n{ARRAY}")
	#s=SortThread(0,ARRAY[0])
	#f=BinarySearchThread(0,ARRAY[0])
	#s.start()
	#f.start()
	#f.join()
        array2=ARRAY.copy()
        sortThreads=[]
        searchThreads=[]
        for i in range(nOfArrays):
            sortThreads.append(SortThread(i,ARRAY[i]))
            searchThreads.append(BinarySearchThread(i,ARRAY[i]))
        tic=time.time()
        for i in range(nOfArrays):
            sortThreads[i].start()
            searchThreads[i].start()
            searchThreads[i].join()
        toc=time.time()
        print(f"Execution time mt = {toc-tic}")
        
        tic=time.time()
        for i in range(nOfArrays):
            tofind=random.choice(array2[i])
            bubbleSort(array2[i])
            position=binarySearch(tofind,array2[i])

        toc=time.time()
        print(f"Execution time = {toc-tic}")

	
	


