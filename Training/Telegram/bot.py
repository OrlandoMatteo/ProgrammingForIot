import telepot
from telepot.loop import MessageLoop
import json
import requests
import time
from MyMQTT import *
class EchoBot:
    def __init__(self,token):
        # Local token
        self.tokenBot=token
        # Catalog token
        #self.tokenBot=requests.get("http://catalogIP/telegram_token").json()["telegramToken"]
        self.bot=telepot.Bot(self.tokenBot)
        MessageLoop(self.bot,{'chat': self.on_chat_message}).run_as_thread()
        self.client=MyMQTT("telegramBot",broker,port,None)

    def on_chat_message(self,msg):
        content_type, chat_type ,chat_ID = telepot.glance(msg)
        message=msg['text']

        self.bot.sendMessage(chat_ID,text="You sent:\n"+message)

class SimpleSwitchBot:
    def __init__(self,token,broker,port,topic):
        # Local token
        self.tokenBot=token
        # Catalog token
        #self.tokenBot=requests.get("http://catalogIP/telegram_token").json()["telegramToken"]
        self.bot=telepot.Bot(self.tokenBot)
        self.client=MyMQTT("telegramBot",broker,port,None)
        self.client.start()
        self.topic=topic
        self.__message={'bn':"telegramBot",
			'e':
				[
					{'n':'switch','v':'', 't':'','u':'bool'},
					]
			}
        MessageLoop(self.bot,{'chat': self.on_chat_message}).run_as_thread()

    def on_chat_message(self,msg):
        content_type, chat_type ,chat_ID = telepot.glance(msg)
        message=msg['text']
        if message=="/switch-on":
            payload=self.__message.copy()
            payload['e'][0]['v']="on"
            payload['e'][0]['t']=time.time()
            self.client.myPublish(self.topic,payload)
            self.bot.sendMessage(chat_ID,text="Led switched on")
        elif message=="/switch-off":
            payload=self.__message.copy()
            payload['e'][0]['v']="on"
            payload['e'][0]['t']=time.time()
            self.client.myPublish(self.topic,payload)
            self.bot.sendMessage(chat_ID,text="Led switched off")
        else:
            self.bot.sendMessage(chat_ID,text="Command not supported")


if __name__=="__main__":
    conf=json.load(open("settings.json"))
    token=conf["telegramToken"]

    # Echo bot
    #bot=EchoBot(token)

    # SimpleSwitchBot
    broker=conf["brokerIP"]
    port=conf["brokerPort"]
    topic=conf["mqttTopic"]
    ssb=SimpleSwitchBot(token,broker,port,topic)


    while True:
        time.sleep(3)