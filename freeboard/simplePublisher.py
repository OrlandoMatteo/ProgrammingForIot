import paho.mqtt.client as PahoMQTT
import time
import random

class MyPublisher:
	def __init__(self, clientID):
		self.clientID = clientID

		# create an instance of paho.mqtt.client
		self._paho_mqtt = PahoMQTT.Client(self.clientID, False) 
		# register the callback
		self._paho_mqtt.on_connect = self.myOnConnect

		#self.messageBroker = 'iot.eclipse.org'
		self.messageBroker = 'mqtt.eclipse.org'

	def start (self):
		#manage connection to broker
		self._paho_mqtt.connect(self.messageBroker, 1883)
		self._paho_mqtt.loop_start()

	def stop (self):
		self._paho_mqtt.loop_stop()
		self._paho_mqtt.disconnect()

	def myPublish(self, topic, message):
		print('Published')
            # publish a message with a certain topic
		self._paho_mqtt.publish(topic, message, 2)

	def myOnConnect (self, paho_mqtt, userdata, flags, rc):
		print ("Connected to %s with result code: %d" % (self.messageBroker, rc))



if __name__ == "__main__":
    test = MyPublisher("MyPublisher")
    test.start()
    while True:
        message = ('{"speed":'+str(random.randint(1,100))+'}')
        test.myPublish ('IoT/Orlando/speed', message) 	
        time.sleep(5)

    test.stop()


