import cherrypy
import requests
import json
class Catalog(object):
	def __init__(self):
		self.devices=[]
	def addDevice(self,devicesInfo):
		self.devices.append(devicesInfo)
	def updateDevice(self,deviceID,devicesInfo):
		for i in range(len(self.devices)):
			device=self.devices[i]
			if device['ID']==deviceID:
				self.devices[i]=devicesInfo
	def removeDevices(self,deviceID):
		for i in range(len(self.devices)):
			device=self.devices[i]
			if device['ID']==deviceID:
				self.devices.pop(i)
class CatalogREST(object):
	exposed=True
	def __init__(self,clientID):
		self.ID=clientID
		self.catalog=Catalog()
	def GET(self,*uri,**params):
		output={'devices':self.catalog.devices}
		return json.dumps(output)
	def PUT(self):
		body=cherrypy.request.body.read()
		json_body=json.loads(body.decode('utf-8'))
		if not any(d['ID']==json_body['ID'] for d in self.catalog.devices):
			self.catalog.addDevice(json_body)
			output=f"Device with ID {json_body['ID']} has been added"
			print (output)
			return output
		else:
			output=f"Device with ID {json_body['ID']} already in list"
			print (output)
			return output

	def POST(self):
		body=cherrypy.request.body.read()
		json_body=json.loads(body.decode('utf-8'))
		self.catalog.updateDevice(json_body['ID'],json_body)
		output=f"Device with ID {json_body['ID']} has been updated"
		print (output)
		return output

	def DELETE(self,*uri):
		self.catalog.removeDevices(uri[0])
		output=f"Device with ID {uri[0]} has been removed"
		print (output)


if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tool.session.on':True
		}
	}
	cherrypy.config.update({'server.socket_host': '0.0.0.0','server.socket_port': 8080})
	cherrypy.tree.mount(CatalogREST('Catalog'),'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()

