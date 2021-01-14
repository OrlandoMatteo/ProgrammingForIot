import json
from MyMQTT import *
import numpy as np
import uuid
import time


class TempSensor:
    def __init__(self, sensorID, mu, sigma, broker, port,topic):
        self.mu = mu
        self.sigma = sigma
        self.topic=topic
        self.__message = {
            "bn": sensorID,
            "e": [
                {
                    "n": "temperature",
                    "u": "Cel",
                    "t": 0,
                    "v": 0
                }
            ]
            }
        self.client = MyMQTT(sensorID, broker, port, None)
        self.client.start()

    def getData(self):
        return np.random.normal(mu, sigma, 1)[0]
    
    def sendData(self):
        message=self.__message.copy()
        message["e"][0]["v"]=self.getData()
        message["e"][0]["t"]=time.time()
        self.client.myPublish(self.topic,message)

if __name__ == "__main__":
    conf=json.load(open("settings.json"))
    mu=15
    sigma=3
    topic=conf["baseTopic"]+"/Orlando/1"
    sensor=TempSensor(str(uuid.uuid1()),mu,sigma,conf["broker"],conf["port"],topic)
    try:
        while True:
            sensor.sendData()
            time.sleep(15)
    except KeyboardInterrupt:
        print("TempSimulator stopped")