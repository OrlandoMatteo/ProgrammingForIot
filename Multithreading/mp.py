
import time
from multiprocessing import Process
import random
from helpingFunctions import *
nOfArrays=4
VARIABLE=1000
ARRAY=[[random.randint(1,VARIABLE) for i in range(VARIABLE)] for i in range ( nOfArrays )]
POSITIONS=[None for i in range(nOfArrays)]

	
def sortAndFind(array):
	tofind=random.choice(array)
	bubbleSort(array)
	position=array.index(tofind) 

	

if __name__ == '__main__':
	
	processes=[]
	for i in range(nOfArrays):
		s=Process(target=sortAndFind,args=(ARRAY[i],))
		processes.append(s)
	tic=time.time()
	for s in processes:
		s.start()
	for s in processes:
		s.join()

	toc=time.time()
	print(f"Execution time mt = {toc-tic}")



	array2=ARRAY.copy()
	tic=time.time()
	for i in range(nOfArrays):
		sortAndFind(array2[i])

	toc=time.time()
	print(f"Execution time = {toc-tic}")

	
	


