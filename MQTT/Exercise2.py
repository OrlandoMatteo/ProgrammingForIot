import cherrypy
import os
from Exercise1 import *
class LightREST(object):
	exposed=True
	def __init__(self):
		self.led_client=LedClient('LED','led')
		self.led_client.run()
	def GET(self):
		return open('index.html')
	def PUT(self, *uri):
		command=uri[0]
		self.led_client.publish(command)
		

if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tool.session.on':True,
				'tools.staticdir.root': os.path.abspath(os.getcwd())
		},
		#You need to include the part below if you want to activate the css and gice to the button a nicer look
		#'/css':{
		#		'tools.staticdir.on': True,
		#		'tools.staticdir.dir':'./css'
		#}
	}		
	cherrypy.tree.mount(LightREST(),'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()
