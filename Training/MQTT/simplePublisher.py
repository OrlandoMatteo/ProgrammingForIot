import paho.mqtt.client as PahoMQTT
import time

class MyPublisher:
	def __init__(self, clientID,topic,broker):
		self.clientID = clientID
		self.topic = topic

		# create an instance of paho.mqtt.client
		self._paho_mqtt = PahoMQTT.Client(self.clientID,True) 
		# register the callback
		self._paho_mqtt.on_connect = self.myOnConnect
		#self.messageBroker = 'iot.eclipse.org'
		self.messageBroker = broker

	def start (self):
		#manage connection to broker
		self._paho_mqtt.connect(self.messageBroker, 1883)
		self._paho_mqtt.loop_start()

	def stop (self):
		self._paho_mqtt.loop_stop()
		self._paho_mqtt.disconnect()

	def myPublish(self,message):
		# publish a message with a certain topic
		self._paho_mqtt.publish(self.topic, message, 2)

	def myOnConnect (self, paho_mqtt, userdata, flags, rc):
		print ("Connected to %s with result code: %d" % (self.messageBroker, rc))




if __name__ == "__main__":
	test = MyPublisher("mypub 1","orlando/iot/1",'mqtt.eclipse.org')
	test.start()

	a = 0
	while (a < 30):
		a += 1
		test.myPublish(str(a))
		time.sleep(1)

	test.stop()