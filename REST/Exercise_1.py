import cherrypy
class UriReverser(object):
	"""docstring for Reverser"""
	exposed=True
	def __init__(self):
		pass
	def GET(self, *uri):
		reversed=uri[0]
		return reversed[::-1]


if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tool.session.on':True
		}
	}		
	cherrypy.tree.mount(UriReverser(),'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()
