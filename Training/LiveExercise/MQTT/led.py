import paho.mqtt.client as PahoMQTT
import json
import time
class Led(object):
	"""docstring for Led"""
	def __init__(self,topic, broker):

		self._paho_mqtt=PahoMQTT.Client('led',False)
		self._paho_mqtt.on_connect=self.myOnConnect
		self._paho_mqtt.on_message=self.myMessageReceived

		self.topic=topic
		self.broker=broker
		self.status="off"

	def start(self):
		self._paho_mqtt.connect(self.broker,1883)
		self._paho_mqtt.loop_start()
		self._paho_mqtt.subscribe(self.topic,2)

	def myOnConnect(self,paho_mqtt, userData, flags, rc):
		print(f"Connected to {self.broker} with result {rc}")

	def myMessageReceived(self,paho_mqtt,userData,msg):
		message=json.loads(msg.payload)
		self.status=message['command']
		print(f"Status set to {message}")

	def stop(self):
		self._paho_mqtt.unsubscribe(self.topic)
		self._paho_mqtt.loop_stop()
		self._paho_mqtt.disconnect()

if __name__ == '__main__':
	broker='127.0.0.1'
	myLed=Led('ledStatus',broker)
	myLed.start()
	while True:
		time.sleep(1)
	myLed.stop()

		