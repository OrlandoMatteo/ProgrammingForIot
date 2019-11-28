import random
import json
from MyMQTT import *
import time

class DataCollector():
	"""docstring for Sensor"""
	def __init__(self,clientID,broker):
		self.clientID=clientID
		self.baseTopic='IoT s.p.a.'
		self.client=MyMQTT(clientID,broker,1883, self)
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
	coll=DataCollector('dc'+str(random.randint(1,10**5)),'127.0.0.1')
	coll.run()
	print(f'This is the client to follow the data coming from the sensors of the building of {coll.baseTopic}')
	choice=''
	while choice!='q':
		print("What kind of data you want to retrieve")
		print("\ta: data from all the building")
		print("\tf: data from a particular floor")
		print("\tr: data from a particular room")
		print("\tc: to go back to this menu")
		print("\tq: to quit")
		choice=input()
		if choice=='q':
			break
		while choice!='c':		
			if choice=='a':
				coll.client.unsubscribe()
				coll.follow(coll.baseTopic+'/#')
			elif choice=='f':
				print('Type the floor [0-->4]')
				floor=str(input())
				coll.client.unsubscribe()
				coll.follow(coll.baseTopic+'/'+floor+'/#')
			elif choice=='r':
				print('Type the floor [0-->4]')
				floor=str(input())
				print('Type the room [1-->3]')
				room=str(input())
				coll.client.unsubscribe()
				coll.follow(coll.baseTopic+'/'+floor+'/'+room+'/#')
			choice=input()
		coll.client.unsubscribe()
		
	coll.client.unsubscribe()
	coll.end()


		
