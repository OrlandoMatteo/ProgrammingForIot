
import random
import json
from MyMQTT import *
import time
from simplePublisher import *
class Sensor(MyPublisher):
	"""docstring for Sensor"""
	def __init__(self,buildingID,floorID,roomID,sensorID,broker,port):
		self.buildingID=buildingID
		self.floorID=floorID
		self.roomID=roomID
		self.sensorID=str(sensorID)
		self.topic='/'.join([self.buildingID,self.floorID,self.roomID,self.sensorID])
		self.client=MyMQTT(self.sensorID,broker,port,None)
		self.__message={
			'buildingID':self.buildingID,
			'floorID':self.floorID,
			'roomID':self.roomID,
			'bn':self.sensorID,
			'e':
				[
					{'n':'temperature','value':'', 'timestamp':'','unit':'C'},
					{'n':'humidity','value':'', 'timestamp':'','unit':'%'}
					]
			}


	def sendData(self):
		message=self.__message
		message['e'][0]['value']=random.randint(10,30)
		message['e'][1]['value']=random.randint(50,90)
		message['e'][0]['timestamp']=str(time.time())
		message['e'][1]['timestamp']=str(time.time())
		self.client.myPublish(self.topic,message)

	def start (self):
		self.client.start()

	def stop (self):
		self.client.stop()

if __name__ == '__main__':
	conf=json.load(open("settings.json"))
	Sensors=[]
	buildingID=conf["baseTopic"]
	floorIDs=[str(i)  for i in range(5)]
	roomIDs=[str(i+1) for i in range(3)]
	broker=conf["broker"]
	port=conf["port"]
	s=0
	for floor in floorIDs:
		for room in roomIDs:
			sensor=Sensor(buildingID,floor,room,s,broker,port)
			Sensors.append(sensor)
			s+=1
	for sensor in Sensors:
		sensor.start()
	while True:
		for sensor in Sensors:
			sensor.sendData()
			time.sleep(1)
	