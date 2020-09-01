import time
from MyMQTT import *
import json

class Client():
    def __init__(self,user,chat):
        self.clientID=user
        self.answer=False
        self.topic=chat
        self.client=MyMQTT(self.clientID,'localhost',1883,self)
    def notify(self,topic,msg):
        payload=json.loads(msg)
        sent_from=payload['user']
        text=payload['text']
        if sent_from!= self.clientID:
            self.answer=True
            print('{}: {}'.format(sent_from,text))
    def publish(self,text):
        message={'user':self.clientID,'text':text}
        self.answer=False
        self.client.myPublish(self.topic,json.dumps(message))
    def run(self):
        self.client.start()
        print('{} has started'.format(self.clientID))
    
    def end(self):
        self.client.stop()
        print('{} has stopped'.format(self.clientID))
    def subscribe(self):
        self.client.mySubscribe(self.topic)

def main():
    username=input('Your name:')
    client=Client(username,'Chat')
    client.run()
    client.subscribe()
    answer=False
    while True:
        text=input(client.clientID+': ')
        client.publish(text)
        while not client.answer:
            time.sleep(0.5)
if __name__ == "__main__":
    main()        
