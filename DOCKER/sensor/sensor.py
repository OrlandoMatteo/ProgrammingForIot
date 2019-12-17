import cherrypy
import requests
import json
import random
import time
class SensorREST(object):
	exposed=True
	def __init__(self):
		self.settings=json.load(open('settings.json'))
		self.settings['commands']=['hum','temp']
		requests.put(self.settings['catalog'],data=json.dumps(self.settings))
	def GET(self,*uri,**params):
		if len(uri)!=0:
			if uri[0]=='hum':
				value=random.randint(60,80)
			if uri[0]=='temp':
				value=random.randint(10,25)
			output={'deviceID':self.settings['ID'],str(uri[0]):value}
			return json.dumps(output)
		else:
			return json.dumps(self.settings)
	def pingCatalog(self):
		requests.put(self.settings['catalog'],data=json.dumps(self.settings))


if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tool.session.on':True
		}
	}
	s=SensorREST()
	cherrypy.config.update({'server.socket_host': '0.0.0.0','server.socket_port': s.settings['port']})	
	cherrypy.tree.mount(s,'/',conf)
	cherrypy.engine.start()
	while True:
		print('sleeping')
		time.sleep(10)
		s.pingCatalog()
	cherrypy.engine.exit()
