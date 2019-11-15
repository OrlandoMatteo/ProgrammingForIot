from MyMQTT import *
import time
class exampleNotifier(object):
	"""docstring for exampleNotifier"""
	def __init__(self,notifierID):
		self.notifierID=notifierID
		self.mqttClient=MyMQTT(notifierID,"pc-orlando-lab4.polito.it",1883,self)

	def notify(self,topic, payload):

		print(topic)
		print(payload)

	def run(self):
		print("Connected to the broker")
		self.mqttClient.start()
		
	def subscribeToTopic(self,topic):
		print(f"Subscribing to {topic}")
		self.mqttClient.mySubscribe(topic)
		print("Subscribed!")

		


if __name__ == '__main__':
	notifier=exampleNotifier('2')
	notifier.run()
	notifier.subscribeToTopic("example")
	while True:
		time.sleep(60)
		

