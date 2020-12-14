import cherrypy
import requests
import json
import time
import threading


class Catalog(threading.Thread):
    def __init__(self, ri, rt):
        threading.Thread.__init__(self)
        self.catalog = {"users":[]}
        self.__userTemplate={"userID":"","devices":[]}
        self.__deviceTemplate={"userID":"","deviceID":"","ip":"","mqtt":[],"rest":[]}
        self.actualTime = time.time()
        self.removeInterval = ri
        self.removeThreshold = rt
        self.settings=json.load(open("settings.json"))
    def addDevice(self, devicesInfo):
        if not any(d['usedID']==devicesInfo['userID'] for d in self.catalog["users"]):
            user=self.__userTemplate.copy()
            user["ID"]=devicesInfo['userID']
            user["devices"].append(devicesInfo)
        else:
            user=next(u for u in self.catalog["users"] if u["userID"]==devicesInfo['userID'])
            user["devices"].append(devicesInfo)
        return json.dumps(self.settings)

    def updateDevice(self, devicesInfo):
        user=next(u for u in self.catalog["users"] if u["userID"]==devicesInfo['userID'])
        device=next(u for u in user["devices"] if u["deviceID"]==devicesInfo['deviceID'])
        device=devicesInfo


    def run(self):
        while True:
            time.sleep(self.removeInterval)
            self.removeInactive()

    def removeInactive(self):
        pass


class CatalogREST(object):
    exposed = True

    def __init__(self, clientID, ri, rt):
        self.ID = clientID
        self.catalog = Catalog(ri, rt)
        self.catalog.start()

    def GET(self, *uri, **params):
        return json.dumps(self.catalog.settings)


    def POST(self):
        body = cherrypy.request.body.read()
        last_update = time.time()
        json_body = json.loads(body.decode('utf-8'))
        json_body['last_update'] = last_update
        self.catalog.addDevice(json_body)
        return json.dumps(self.catalog.settings)


if __name__ == '__main__':
    catalogClient = CatalogREST('Catalog', 10, 5)
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tool.session.on': True
        }
    }
    cherrypy.config.update(
        {'server.socket_host': '0.0.0.0', 'server.socket_port': 80})
    cherrypy.tree.mount(catalogClient, '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
    cherrypy.engine.exit()
