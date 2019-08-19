import requests
import time
import threading
import json

hosts = "http://yahoo.com", "http://google.com", "http://amazon.com",
"http://ibm.com", "http://apple.com","https://www.microsoft.com","https://www.youtube.com/" ,"https://www.polito.it/" ,"http://www.wikipedia.org","https://www.reddit.com/","https://www.adobe.com/","https://wordpress.org/","https://github.com/","https://www.google.com/maps/"

start = time.time()
for host in hosts:
	url = requests.get(host)
stop=time.time()
x=stop-start
print ("Elapsed Time: {}".format(x))


class MyThread(threading.Thread):
	def __init__(self, threadID, host):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.host = host
		self.execTime=0
		
	def run(self):
		url = requests.get(host)
	
		
		

threads=[]
i=0
for host in hosts:
	threads.append(MyThread(i,host))
	i+=1
start = time.time()
for t in threads:
	t.start()
for t in threads:
	t.join()
stop=time.time()
x=stop-start

print("Elapsed Time: {}".format(x))






