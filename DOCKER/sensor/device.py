import cherrypy
import requests
import json
import random
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
				value=random.randint(15,25)
			output={'deviceID':self.settings['ID'],str(uri[0]):value}
			return json.dumps(output)
		else:
			return json.dumps({})


if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tool.session.on':True
		}
	}
	s=SensorREST()
	cherrypy.config.update({'server.socket_host': '0.0.0.0','server.socket_port': s.settings['port']})	
	cherrypy.tree.mount(SensorREST(),'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()