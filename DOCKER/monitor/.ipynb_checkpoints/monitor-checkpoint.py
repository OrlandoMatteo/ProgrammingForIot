import requests
import json
import time
class Viewer(object):
	"""docstring for Viewer"""
	def __init__(self):
		self.catalogInfo=json.load(open("settings.json"))
		self.devices=self.getDevices()
	
	def getDevices(self):
		response=requests.get(self.catalogInfo['catalogURL']).json()
		print('List of available devices obtained')
		return  response['devices']
	
	def listDevices(self):
		print('This are the available devices:')
		for device in self.devices:
			print(device['ID'])
		idSelected=input("Which device to you want to monitor (r to refresh  q to quit)\n")
		if idSelected!='q':
			if idSelected=='r':
				self.getDevices()
				self.listDevices()
			else:
				idSelected=int(idSelected)
				self.monitor([x for x in self.devices if x['ID']==idSelected][0])
		else:
			exit()
	
	def monitor(self,device):
		print("Temp (C)\tHum(%)")
		end_time=time.time()+4
		while time.time()<end_time:
			temp=requests.get(device["IP"]+':'+str(device['port'])+'/temp').json()['temp']
			hum=requests.get(device["IP"]+':'+str(device['port'])+'/hum').json()['hum']
			print(str(temp)+'\t\t'+str(hum),end="\r")
			time.sleep(0.5)
		self.listDevices()

if __name__ == '__main__':
	v=Viewer()
	v.listDevices()