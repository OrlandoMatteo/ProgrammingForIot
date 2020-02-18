import cherrypy
import json
import random
import os
import cherrypy_cors

class DataServer(object):
    exposed=True
    
    def __init__(self,name):
        self.name=name
    def GET(self,*uri, **params):
        output={"x":random.randint(10,80),"y":random.randint(150,200)}
        return json.dumps(output)

if __name__ == '__main__':
    cherrypy_cors.install()
    cherrypy.config.update({
        "server.socket_port": 8088,
        })
    conf = {
        '/':{
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
            'cors.expose.on': True,
        }
    }
    cherrypy.tree.mount(DataServer('Test'),'/',conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
