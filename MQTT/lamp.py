import time
import json
from MyMQTT import * 
class Led():
    def __init__(self,clientID,topic):
        self.clientID=clientID
        self.topic=topic
        self.client=MyMQTT('Led','localhost',1883,self)
    def run(self):
        self.client.start()
        print('{} has started'.format(self.clientID))
    def end(self):
        self.client.stop()
        print('{} has stopped'.format(self.clientID))
    def notify(self,topic,msg):
        d=json.loads(msg)
        self.status=d['command']
        print('The led has been set to {}'.format(self.status))
    def publish(self,value):
        pass
    def subscribe(self):
        self.client.mySubscribe(self.topic)

if __name__ == "__main__":
    led=Led('Led','led')
    led.run()
    led.subscribe()
    while True:
        time.sleep(1)

