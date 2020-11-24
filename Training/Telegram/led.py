from MyMQTT import *
import time
import json

class Led:
	def __init__(self, clientID, topic,broker,port):
		self.client=MyMQTT(clientID,broker,port,self)
		self.topic=topic
		self.status=None

	def start (self):
		self.client.start()
		self.client.mySubscribe(self.topic)

	def stop (self):
		self.client.stop()
			
	def notify(self,topic,msg):
		d=json.loads(msg)
		self.status=d['e'][0]['v']
		client=d['bn']
		timestamp=d['e'][0]['t']
		print(f'The led has been set to {self.status} at time {timestamp} by the client {client}')


if __name__ == "__main__":
	conf=json.load(open("settings.json"))
	broker=conf["brokerIP"]
	port=conf["brokerPort"]
	topic=conf["mqttTopic"]
	test = Led("MyLed",topic,broker,port)
	test.start()

	while True:
		time.sleep(1)

	test.stop()
