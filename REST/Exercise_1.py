import cherrypy
class UriReverser(object):
	"""docstring for Reverser"""
	exposed=True
	def __init__(self):
		pass
	def GET(self, *uri):
		if len(uri)!=0:
			reverse=uri[0]
			return reverse[::-1]
		else:
			return ''


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
