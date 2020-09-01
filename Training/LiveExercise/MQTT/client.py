import paho.mqtt.client as PahoMQTT
import json

class Client(object):
	"""docstring for Client"""
	def __init__(self,topic,broker):
		self._paho_mqtt=PahoMQTT.Client('ledClient',False)
		self._paho_mqtt.on_connect=self.myOnConnect
		self.topic=topic
		self.broker=broker

	def start(self):
		self._paho_mqtt.connect(self.broker,1883)
		self._paho_mqtt.loop_start()

	def myOnConnect(self,paho_mqtt, userData, flags, rc):
		print(f"Connected to {self.broker} with result {rc}")

	def myPublish(self,message):
		self._paho_mqtt.publish(self.topic,json.dumps(message))
		print("Published")
	def stop(self):
		self._paho_mqtt.loop_stop()
		self._paho_mqtt.disconnect()

if __name__ == '__main__':
	broker='127.0.0.1'
	c=Client('ledStatus',broker)
	c.start()
	c.myPublish({"command":"on"})
	c.myPublish({"command":"off"})

		
		