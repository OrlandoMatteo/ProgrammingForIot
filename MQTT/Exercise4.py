import cherrypy
import time
from MyMQTT import *
import json
users=[]
class Client():
    def __init__(self,user,chat):
        self.clientID=user
        self.topic=chat
        self.client=MyMQTT(self.clientID,'localhost',1883,self)
    def notify(self,topic,msg):
        payload=json.loads(msg)
        sent_from=payload['user']
        text=payload['text']
        #print('{}: {}'.format(sent_from,text))
    def publish(self,text):
        message={'user':self.clientID,'text':text}
        self.client.myPublish(self.topic,json.dumps(message))
    def run(self):
        self.client.start()
        print('{} has started'.format(self.clientID))
    
    def end(self):
        self.client.stop()
        print('{} has stopped'.format(self.clientID))
    def subscribe(self):
        self.client.mySubscribe(self.topic)
       
class ChatREST(object):
    exposed=True
    def __init__(self):
        pass
    def GET(self,**params):
        return open('chat.html')
    def PUT(self, *uri, **params):
        global users
        d=params.keys()
        if uri=='user':
            t=Client(d['user'],'chat')
            t.run()
            t.subscribe()
            users.append(t)
        else:
            user=[u for i in users if u.clientID==d['user']]
            user.publish(d['text'])

        

if __name__ == '__main__':
    conf={
    	'/':{
    			'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
    			'tool.session.on':True
    	}
    }		
    cherrypy.tree.mount(ChatREST(),'/',conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
