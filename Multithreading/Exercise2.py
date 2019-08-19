import requests
import time
import threading
import random

def factorial(n):
	f=1
	for i in range(1,n+1):
		f=f*n
	return f
start = time.time()

numbers=[random.randint(80,150) for i in range(120)]
for n in numbers:
	f=factorial(n)
stop=time.time()
x=stop-start
print ("Elapsed Time: {}".format(x))


class MyThread(threading.Thread):
	def __init__(self, threadID, host):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.host = host

		
	def run(self):
		f=factorial(n)


threads=[]
i=0
for n in numbers:
	threads.append(MyThread(i,n))
	i+=1
start = time.time()
for t in threads:
	t.start()
for t in threads:
	t.join()
stop=time.time()
x=stop-start

print("Elapsed Time: {}".format(x))






