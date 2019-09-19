import random
import json
from MyMQTT import *
import time

class DataCollector(object):
	"""docstring for Sensor"""
	def __init__(self,clientID):
		self.clientID=clientID
		self.client=MyMQTT(self.clientID,'localhost',1883,self)
	def run(self):
		self.client.start()
		print('{} has started'.format(self.clientID))
	
	def end(self):
		self.client.stop()
		print('{} has stopped'.format(self.clientID))
	def follow(self,topic):
		self.client.mySubscribe(topic)
	def notify(self,topic,msg):
		payload=json.loads(msg)
		print(json.dumps(payload,indent=4))

if __name__ == '__main__':
	coll=DataCollector('dc')
	coll.run()
	coll.follow('IoT s.p.a./3/#')
	while True:
		time.sleep(1)
		
