from MyMQTT import *
import time
import json
class LedManager:
	def __init__(self, clientID, topic,broker,port):
		self.topic=topic
		self.__message={'client': clientID,'n':'switch','value':None, 'timestamp':'','unit':"bool"}

		self.client=MyMQTT(clientID,broker,port,None)
		self.statusToBool={"on":1,"off":0}


	def start (self):
		self.client.start()

	def stop (self):
		self.client.stop()

	def publish(self,value):
		message=self.__message
		message['timestamp']=str(time.time())
		message['value']=self.statusToBool[value]
		self.client.myPublish(self.topic,message)
		print("published")



if __name__ == "__main__":
	conf=json.load(open("settings.json"))
	broker=conf["broker"]
	port=conf["port"]
	ledManager = LedManager("LedCommander","IoT/Orlando/led",broker,port)
	ledManager.client.start()

	print('Welcome to the client to switch on/off the lamp\n')
	done=False
	command_list='Type:\n"on" to set the light on\n"off" to set it off\n"q" to quit\n'
	while not done:
		print(command_list)
		user_input=input()
		if user_input=="on" or user_input=="off":
			ledManager.publish(user_input)
		elif user_input=='q':
			done=True
		else:
			print('Unknown command')
	ledManager.client.stop()   


