import paho.mqtt.client as PahoMQTT
import time
import json

class Led:
	def __init__(self, clientID,topic,broker):
		self.clientID = clientID
		# create an instance of paho.mqtt.client
		self._paho_mqtt = PahoMQTT.Client(clientID, False) 

		# register the callback
		self._paho_mqtt.on_connect = self.myOnConnect
		self._paho_mqtt.on_message = self.myOnMessageReceived

		self.topic = topic
		self.messageBroker =broker 

		self.status=""

	def start (self):
		#manage connection to broker
		self._paho_mqtt.connect(self.messageBroker, 1883)
		self._paho_mqtt.loop_start()
		# subscribe for a topic
		self._paho_mqtt.subscribe(self.topic, 2)

	def stop (self):
		self._paho_mqtt.unsubscribe(self.topic)
		self._paho_mqtt.loop_stop()
		self._paho_mqtt.disconnect()

	def myOnConnect (self, paho_mqtt, userdata, flags, rc):
		print ("Connected to %s with result code: %d" % (self.messageBroker, rc))

	def myOnMessageReceived (self, paho_mqtt , userdata, msg):
		# A new message is received
		#print ("Topic:'" + msg.topic+"', QoS: '"+str(msg.qos)+"' Message: '"+str(msg.payload) + "'")
		d=json.loads(msg.payload)
		self.status=d['value']
		client=d['client']
		timestamp=d['timestamp']
		print(f'The led has been set to {self.status} at time {timestamp} by the client {client}')


if __name__ == "__main__":
	broker=json.load(open("mosquitto.json"))['broker']
	test = Led("MyLed","ledCommand",'127.0.0.1')
	test.start()

	while True:
		time.sleep(1)

	test.stop()
