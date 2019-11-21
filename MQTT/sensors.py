
import random
import json
from MyMQTT import *
import time
from simplePublisher import *
class Sensor(MyPublisher):
	"""docstring for Sensor"""
	def __init__(self,buildingID,floorID,roomID,sensorID,broker):
		self.buildingID=buildingID
		self.floorID=floorID
		self.roomID=roomID
		self.sensorID=str(sensorID)
		self.topic='/'.join([self.buildingID,self.floorID,self.roomID,self.sensorID])
		MyPublisher.__init__(self,self.sensorID,self.topic,broker)
		self.message={
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
	def myPublish(self,topic,message):
		self._paho_mqtt.publish(topic,message,2)
	def sendData(self):
		self.message['e'][0]['value']=random.randint(10,30)
		self.message['e'][1]['value']=random.randint(50,90)
		self.message['e'][0]['timestamp']=str(time.time())
		self.message['e'][1]['timestamp']=str(time.time())
		self.myPublish(self.topic,json.dumps(self.message))

if __name__ == '__main__':
	Sensors=[]
	buildingID='IoT s.p.a.'
	floorIDs=[str(i)  for i in range(5)]
	roomIDs=[str(i+1) for i in range(3)]
	broker='127.0.0.1'
	s=0
	for floor in floorIDs:
		for room in roomIDs:
			sensor=Sensor(buildingID,floor,room,s,broker)
			Sensors.append(sensor)
			s+=1
	for sensor in Sensors:
		sensor.start()
	while True:
		for sensor in Sensors:
			sensor.sendData()
			time.sleep(1)
	