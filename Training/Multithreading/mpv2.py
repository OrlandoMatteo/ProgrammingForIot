import random
import multiprocessing
import time

def list_append(count, id, out_list):
	"""
	Creates an empty list and then appends a 
	random number to the list 'count' number
	of times. A CPU-heavy operation!
	"""
	for i in range(count):
		out_list.append(random.random())

if __name__ == "__main__":
	size = 10000000   # Number of random numbers to add
	procs = 8   # Number of processes to create

	# Create a list of jobs and then iterate through
	# the number of processes appending each process to
	# the job list 
	jobs = []
	for i in range(0, procs):
		out_list = list()
		process = multiprocessing.Process(target=list_append, 
										  args=(size, i, out_list))
		jobs.append(process)
	tic=time.time()
	# Start the processes (i.e. calculate the random number lists)      
	for j in jobs:
		j.start()

	# Ensure all of the processes have finished
	for j in jobs:
		j.join()
	toc=time.time()
	print(f"Execution time = {toc-tic}")


	tic=time.time()
	for i in range(0, procs):
		out_list = list()
		list_append(size,i,out_list)

	toc=time.time()
	print(f"Execution time = {toc-tic}")