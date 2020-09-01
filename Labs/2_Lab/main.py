import cherrypy
import os
import json

class Server(object):
	exposed=True
	def __init__(self,name):
		self.name=name

	def GET(self):
		return open('login.html')

	def POST(self,*uri,**params):
		body=cherrypy.request.body.read()
		newUser=json.loads(body)
		print(newUser)
		with open('users.json','r') as fp:
			users=json.load(fp)
			users["usersList"].append(newUser)
		with open('users.json','w') as fp:
			json.dump(users,fp)

		return 'Logged!'


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
	cherrypy.engine.autoreload.files.add('login.html')
	cherrypy.tree.mount(Server('test'),'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()