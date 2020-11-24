import cherrypy
import requests
import json 
import time
class Catalog(object):
    def __init__(self):
        self.content=json.load(open("catalog.json"))

    def getUserInfo(self,userID):
        user=[user for user in self.content["users"] if user["ID"]==userID][0]
        print(user)
        return user

class CatalogREST(object):
    exposed=True
    def __init__(self,clientID):
        self.ID=clientID
        self.catalog=Catalog()
    def GET(self,*uri,**params):
        if uri[0]=="node-red":
            output=self.catalog.content.copy()
            output["users"]=[]
        if uri[0]=="user":
            userID=params["ID"]
            output=self.catalog.getUserInfo(userID)
        return json.dumps(output)


if __name__ == '__main__':
    catalogClient=CatalogREST('Catalog')
    conf={
        '/':{
                'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on':True
        }
    }
    cherrypy.config.update({'server.socket_host': '0.0.0.0','server.socket_port': 8080})
    cherrypy.tree.mount(catalogClient,'/',conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
    

