from MyMQTT import *

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
		
	def publishMessage(self,topic,message):
		
		print(f"publishing {message} to topic {topic}")
		self.mqttClient.myPublish(topic,message)
		print("published!")		

		


if __name__ == '__main__':
	notifier=exampleNotifier('1')
	notifier.run()
	notifier.publishMessage("example","test")
		

