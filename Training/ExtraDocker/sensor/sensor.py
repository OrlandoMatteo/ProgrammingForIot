import cherrypy
import requests
import json
import random
import time
import os
from MyMQTT import *
import threading


class SensorREST(threading.Thread):
    exposed = True

    def __init__(self):
        threading.Thread.__init__(self)
        self.__deviceTemplate = {
            "userID": "", "deviceID": "", "ip": "", "mqtt": [], "rest": []}
        self.userID = os.getenv("userID")
        self.deviceID = os.getenv("deviceID")
        self.settings = json.load(open('settings.json'))
        self.topic=self.userID+"/"+"/"+"temp"
        self.__deviceTemplate = {
            "userID": self.userID, "deviceID": self.deviceID, "ip": "", "mqtt": self.topic, "rest": ["/temp"]}
        self.__message = {
            'bn': self.deviceID,
            'e':
                [
                    {'n': 'temperature', 'value': '', 'timestamp': '', 'unit': 'C'}
                ]
            }
        
        time.sleep(10)
        infoFromCatalog=requests.post(self.settings['catalog'], data=json.dumps(self.__deviceTemplate)).json()
        self.client=MyMQTT(self.userID+"_"+self.deviceID,infoFromCatalog["brokerIP"],infoFromCatalog["brokerPort"],None)
        self.start()

    def sendData(self):
        message = self.__message
        message['e'][0]['value'] = random.randint(10, 30)
        message['e'][0]['timestamp'] = str(time.time())
        self.lastMessage=message
        self.client.myPublish(self.topic,message)

    def startMQTT (self):
        self.client.start()

    def stop (self):
        self.client.stop()

    def run(self):
        while True:
            time.sleep(5)
            s.sendData()

    def GET(self, *uri, **params):
        return json.dumps(self.lastMessage)


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tool.session.on': True
        }
    }
    s = SensorREST()
    cherrypy.config.update(
        {'server.socket_host': '0.0.0.0', 'server.socket_port': 80})
    cherrypy.tree.mount(s,'/', conf)
    cherrypy.engine.start()
    s.startMQTT()
    cherrypy.engine.block()
    cherrypy.engine.exit()
