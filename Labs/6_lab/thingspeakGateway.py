import requests
import json
from MyMQTT import *
import uuid
import time

#https://api.thingspeak.com/update?api_key=KPK4N4XRALC9KLRM&field1=0
class ThingSpeakGateway():
    def __init__(self,clientID,broker,port,topic,apikey):
        self.apikey=apikey
        self.baseUrl="https://api.thingspeak.com/update?api_key="+self.apikey+"&"
        self.client=MyMQTT(clientID,broker,port,self)
        self.topic=topic
        self.client.start()
        self.client.mySubscribe(topic)
    def notify(self,topic,payload):
        jsonPayload=json.loads(payload)
        value=jsonPayload["e"][0]["v"]
        r=requests.get(self.baseUrl+"field1="+str(value))
        print(r.text)

if __name__ == "__main__":
    conf=json.load(open("settings.json"))
    broker=conf["broker"]
    apikey=conf["apikey"]
    port=conf["port"]
    topic=conf["baseTopic"]+"/#"
    tsa=ThingSpeakGateway(str(uuid.uuid1()),broker,port,topic,apikey)
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("TSA stopped")