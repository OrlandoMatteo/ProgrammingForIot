import cherrypy
import json
class ParamsReverser(object):
	"""docstring for Reverser"""
	exposed=True
	def __init__(self):
		pass
	def GET(self, **params):
		reverse={}
		for key in params.keys():
			reverse[key]=params[key][::-1]
		return json.dumps(reverse)


if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tool.session.on':True
		}
	}		
	cherrypy.tree.mount(ParamsReverser(),'/',conf)
	cherrypy.engine.start()
	cherrypy.engine.block()
