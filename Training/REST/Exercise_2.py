import cherrypy
import json
class ParamsReverser(object):
	"""docstring for Reverser"""
	exposed=True
	def __init__(self):
		pass
	def GET(self, *uri,**params):
		if len(uri)==0:
			reverse={}
			for key in params.keys():
				reverse[key]=params[key][::-1]
			return json.dumps(reverse)
		else:
			raise cherrypy.HTTPError(status=402,message='opssssss')
		
def error_page_402(status, message, traceback, version):
       return "Error  - Well, I'm very sorry but you haven't paid!"


if __name__ == '__main__':
	conf={
		'/':{
				'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
				'tool.session.on':True
		}
	}		
	cherrypy.tree.mount(ParamsReverser(),'/',conf)
	cherrypy.config.update({'error_page.402': error_page_402})
	cherrypy.engine.start()
	cherrypy.engine.block()
