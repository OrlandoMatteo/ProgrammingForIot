import cherrypy
import os
import json
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
class Server(object):
	exposed=True
	def __init__(self,name,filename):
		self.filename = filename
		self.devicesList=json.load(open(filename))["devicesList"]
		self.name=name

	def GET(self):
		tmpl = env.get_template('index.html')
		return tmpl.render(devicesList=self.devicesList)

	def POST(self,*uri,**params):
		body=cherrypy.request.body.read()
		device=json.loads(body)
		self.devicesList.append(device)
		tmpl = env.get_template('index.html')
		return tmpl.render(devicesList=self.devicesList)
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