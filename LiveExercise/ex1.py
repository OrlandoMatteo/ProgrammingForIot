import threading
import time
import requests
website_list= ["http://yahoo.com",
"http://google.com",
"http://amazon.com",
"http://ibm.com",
"http://apple.com",
"https://www.microsoft.com",
"https://www.youtube.com/" ,
"https://www.polito.it/" ,
"http://www.wikipedia.org",
"https://www.reddit.com/",
"https://www.adobe.com/",
"https://wordpress.org/",
"https://github.com/",
"https://www.google.com/maps/"]

class MyThread(threading.Thread):
	def __init__(self,website):
		threading.Thread.__init__(self)
		self.website=website

	def run(self):
		r=requests.get(self.website)


if __name__ == '__main__':
	
	threads=[]
	for website in website_list:
		threads.append(MyThread(website))

	start=time.time()
	for thread in threads:
		thread.start()

	for thread in threads:
		thread.join()

	end=time.time()
	print (f"Execution time = {end-start}")


	start=time.time()
	for website in website_list:
		requests.get(website)
	end=time.time()
	print (f"Execution time = {end-start}")




