import threading
import time
class TimeStamper(threading.Thread):
	def __init__(self,threadID):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.sleepingTime=self.threadID
	def run(self):
		print (f"{self.threadID} -before- {time.time()}")
		time.sleep(self.sleepingTime)
		print (f"{self.threadID} -after- {time.time()}")


if __name__ == '__main__':
	a=TimeStamper(1)
	b=TimeStamper(2)
	a.start()
	b.start()

	a.join()
	b.join()
	print("Something")