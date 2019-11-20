import paho.mqtt.client as PahoMQTT
import time
import json
from simpleSubscriber import *
class Led(MySubscriber):
    def __init__(self, clientID,topic,broker):
        MySubscriber.__init__(self,clientID,topic,broker)
        self.status=""
    def myOnMessageReceived(self,paho_mqtt,userdata,msg):
        d=json.loads(msg.payload)
        self.status=d['value']
        client=d['client']
        timestamp=d['timestamp']
        print(f'The led has been set to {self.status} at time {timestamp} by the client {client}')

if __name__ == "__main__":
    broker=json.load(open("settings1.json"))['broker']
    test = Led("MyLed","ledCommand",broker)
    test.start()

    while True:
        time.sleep(1)

    test.stop()