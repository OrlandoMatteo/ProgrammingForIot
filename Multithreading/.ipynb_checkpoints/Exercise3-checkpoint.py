import time
import threading
import random
from helpingFunctions import *
nOfArrays
THREADLOCKS=[threading.Lock() for i in range(nOfArrays)]
VARIABLE=10**4
ARRAY=[random.randint(1,VARIABLE*10) for i in range(VARIABLE)]
POSITION=None

class SortThread(threading.Thread):
	def __init__(self, threadID, array):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.array=array
		
	def run(self):
		THREADLOCK.acquire()
		print("Starting sorting")
		bubbleSort(ARRAY)
		#print(f"Sorted array:\n{ARRAY}")
		THREADLOCK.release()

class BinarySearchThread(threading.Thread):
	"""docstring for BinarySearchThread"""
	def __init__(self, threadID,array):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.toFind=random.choice(array)
		self.startingPoint=len(array)//2
		
	def run(self):
		THREADLOCK.acquire()
		print(f"Finding {self.toFind}")
		POSITION=binarySearch(self.toFind,ARRAY)
		print(f"{self.toFind} found at position {POSITION}")	
		THREADLOCK.release()







		

if __name__ == '__main__':
	#print(f"Original array:\n{ARRAY}")
	s=SortThread(1,ARRAY)
	f=BinarySearchThread(2,ARRAY)
	s.start()
	f.start()
	f.join()


	
	


