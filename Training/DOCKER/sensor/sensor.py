import cherrypy
import requests
import json
import random
import time
import threading


class SensorREST(threading.Thread):
    exposed = True

    def __init__(self, pi):
        threading.Thread.__init__(self)
        self.settings = json.load(open('settings.json'))
        self.settings['ID'] = random.randint(1, 1000)
        self.settings['commands'] = ['hum', 'temp']
        self.pingInterval = pi
        requests.put(self.settings['catalog'], data=json.dumps(self.settings))
        self.start()

    def GET(self, *uri, **params):
        if len(uri) != 0:
            if uri[0] == 'hum':
                value = random.randint(60, 80)
            if uri[0] == 'temp':
                value = random.randint(10, 25)
            output = {'deviceID': self.settings['ID'], str(uri[0]): value}
            return json.dumps(output)
        else:
            return json.dumps(self.settings)

    def run(self):
        while True:
            time.sleep(self.pingInterval)
            self.pingCatalog()

    def pingCatalog(self):
        requests.put(self.settings['catalog'], data=json.dumps(self.settings))


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tool.session.on': True
        }
    }
    s = SensorREST(15)
    cherrypy.config.update(
        {'server.socket_host': '0.0.0.0', 'server.socket_port': 80})
    cherrypy.tree.mount(s, '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
    cherrypy.engine.exit()
