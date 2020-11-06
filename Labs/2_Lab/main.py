import cherrypy
import os
import json
class Server(object):
	exposed=True
	def __init__(self,name,filename):
		self.filename = filename
		self.devicesList=json.load(open(filename))["devicesList"]
		self.name=name

	def GET(self, *uri):
		if len(uri)==0:
			return (open('index.html'))
		elif uri[0]=="devicesList":
			return self.devicesList
		else:
			return "404"

	def POST(self,*uri,**params):
		body=cherrypy.request.body.read('')
		print(body)
		device=json.loads(body)
		print(device)
		self.devicesList.append(device)
		self.save()
		return json.dumps({"devicesList":self.devicesList})
	
	def save(self):
		with open(self.filename,'w') as fp:
			json.dump({"devicesList":self.devicesList},fp)


if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tool.session.on':True,
				'tools.staticdir.root': os.path.abspath(os.getcwd())
		},
		 '/css':{
		 'tools.staticdir.on': True,
		 'tools.staticdir.dir':'./css'
		 },
		 '/js':{
		 'tools.staticdir.on': True,
		 'tools.staticdir.dir':'./js'
		 },
	}
	s=Server('deviceManager','devices.json')
	cherrypy.tree.mount(s,'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()
	s.save()