import cherrypy
from Exercise1 import *
class LightREST(object):
    exposed=True
    def __init__(self):
        self.led_client=LedClient('LED','led')
        self.led_client.run()
    def GET(self):
        return open('index.html')
    def PUT(self, *uri):
        self.led_client.publish(uri)
        

if __name__ == '__main__':
    conf={
    	'/':{
    			'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
    			'tool.session.on':True
    	}
    }		
    cherrypy.tree.mount(LightREST(),'/',conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
