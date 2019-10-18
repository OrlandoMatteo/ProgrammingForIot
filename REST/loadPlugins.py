import cherrypy
import os

class Example(object):
	"""docstring for Reverser"""
	exposed=True
	def __init__(self):
		self.id=1
	def GET(self):
		return open("index.html")


if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tools.staticdir.root': os.path.abspath(os.getcwd()),
			},
		###If you remove the content below you will have a nicer look and the functions for the html page
		# '/css':{
		# 'tools.staticdir.on': True,
		# 'tools.staticdir.dir':'./css'
		# },
		# '/js':{
		# 'tools.staticdir.on': True,
		# 'tools.staticdir.dir':'./js'
		# },
	}		
	cherrypy.tree.mount(Example(),'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()
