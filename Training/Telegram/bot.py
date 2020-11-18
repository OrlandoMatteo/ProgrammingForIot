import telepot
from telepot.loop import MessageLoop
import json
import requests
import time

class MyBot:
    def __init__(self):
        # Local token
        self.tokenBot=json.load(open("settings.json"))["telegramToken"]
        # Catalog token
        #self.tokenBot=requests.get("http://catalogIP/telegram_token").json()["telegramToken"]
        self.bot=telepot.Bot(self.tokenBot)
        MessageLoop(self.bot,{'chat': self.on_chat_message}).run_as_thread()

    def on_chat_message(self,msg):
        content_type, chat_type ,chat_ID = telepot.glance(msg)
        message=msg['text']

        self.bot.sendMessage(chat_ID,text="You sent:\n"+message)

if __name__=="__main__":
    bot=MyBot()
    while True:
        time.sleep(3)