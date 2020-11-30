---
marp: true
autoscale: true
paginate: true
footer: 'programming for iot'
theme: dracula
size: 16:9
autoscaling : true
style: |
  section h1{
  color: orange
  }
  section li,ul,p{
  margin: 0 0 0 0;
  }
  section ul > li > p,
  ol > li > p {
  margin: 0.2em 0 0 0;
  }
---

# Telegram bot ![width:50](https://web.telegram.org/img/logo_share.png)

Bots are third-party applications that run inside Telegram. Users can interact with bots by sending them messages, commands and inline requests. You control your bots using HTTPS requests to our Bot API.

[What can be done with bots?](https://core.telegram.org/bots#1-what-can-i-do-with-bots)

---

# Telegram-bot and IoT
![bg right:30%](images/examplebot.png)

For this course telegram-bots will essentially take the place of an app that is usually developed for commercial project.

We will see the basics step to do in order to create a bot, communicate with it and using it to retrieve information and interact with our systems

---

# Requirements

Before starting to code we need two things

* Install the python library called **telepot**
  ```pip install telepot```
* Contact [Botfather](https://telegram.me/BotFather) to obtain a token for our bot

Once we have the token we can save it in a json file but in case of the project we could even store it on the Catalog

![bg right:30% width:300px](https://core.telegram.org/file/811140763/1/PihKNbjT8UE/03b57814e13713da37)

---

# Simple echo bot
## Bot initialization

```python
import telepot
from telepot.loop import MessageLoop
import json
import requests

class MyBot:
    def __init__(self,token):
        # Local token
        self.tokenBot=token
        # Catalog token
        #self.tokenBot=requests.get("http://catalogIP/telegram_token").json()["telegramToken"]
        self.bot=telepot.Bot(self.tokenBot)
        MessageLoop(self.bot,{'chat': self.on_chat_message}).run_as_thread()
```

---

# Simple echo bot

## on_chat_message callback

```python
    def on_chat_message(self,msg):
        content_type, chat_type ,chat_ID = telepot.glance(msg)
        message=msg['text']

        self.bot.sendMessage(chat_ID,text="You sent:\n"+message)
```

---

# Commands

Usually Telegram bot accept some specific commands in the chat given in the format **/command**. With BotFather we can add some hints for the user but then we need to specify inside the code how this command will be handled

![bg right:30%](https://core.telegram.org/file/811140029/1/s5zv4fbWdhw/a04aefa0ee0557f16a)

---
<!--code:invert -->
# Bot + actuation via MQTT

Now we will see how to send command using MQTT to switch on/off the simulated led we used in the previous exercises.

<div style="font-size:20px">

```python
class Led:
	def __init__(self, clientID, topic,broker,port):
		self.client=MyMQTT(clientID,broker,port,self)
		self.topic=topic
		self.status=None

	def start (self):
		self.client.start()
		self.client.mySubscribe(self.topic)

	def stop (self):
		self.client.stop()
			
	def notify(self,topic,msg):
		d=json.loads(msg)
		self.status=d['e'][0]['v']
		client=d['bn']
		timestamp=d['e'][0]['t']
		print(f'The led has been set to {self.status} at time {timestamp} by the client {client}')

```
</div>

---
# Bot + actuation via MQTT

The steps we need to success are 2:

1. Adding an instance of the class *MyMQTT* to enable our bot to be a publisher
2. Handle the command sent from the user to switch the led on or off
   
---
# Bot + actuation via MQTT
## enable MQTT

``` python
class SimpleSwitchBot:
        #....
        self.client=MyMQTT("telegramBot",broker,port,None)
        self.client.start()
        self.topic=topic
        self.__message={'bn':"telegramBot",
			'e':
				[
					{'n':'switch','v':'', 't':'','u':'bool'},
					]
			}
      #....
```

---
# Bot + actuation via MQTT
## Manage commands

<div style="font-size:24px">

``` python
    def on_chat_message(self,msg):
        content_type, chat_type ,chat_ID = telepot.glance(msg)
        message=msg['text']
        if message=="/switchOn":
            payload=self.__message.copy()
            payload['e'][0]['v']="on"
            payload['e'][0]['t']=time.time()
            self.client.myPublish(self.topic,payload)
            self.bot.sendMessage(chat_ID,text="Led switched on")
        elif message=="/switchOff":
            payload=self.__message.copy()
            payload['e'][0]['v']="off"
            payload['e'][0]['t']=time.time()
            self.client.myPublish(self.topic,payload)
            self.bot.sendMessage(chat_ID,text="Led switched off")
        else:
            self.bot.sendMessage(chat_ID,text="Command not supported")
```
</div>

---

# Bot callback and keyboards
## Keyboard tools

```python
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
```
## query callback
```python
MessageLoop(self.bot, {'chat': self.on_chat_message,
                  'callback_query': self.on_callback_query}).run_as_thread()
```

---

# Bot callback and keyboards
In the method to handle the incoming messages we need to create the keyboard and set the callback data which will be used to determine the behaviour of the buttons

```python
def on_chat_message(self, msg):
        content_type, chat_type, chat_ID = telepot.glance(msg)
        message = msg['text']
        if message == "/switch":
            buttons = [[InlineKeyboardButton(text=f'ON 🟡', callback_data=f'on'), 
                    InlineKeyboardButton(text=f'OFF ⚪', callback_data=f'off')]]
            keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
            self.bot.sendMessage(chat_ID, text='What do you want to do', reply_markup=keyboard)
        else:
            self.bot.sendMessage(chat_ID, text="Command not supported")
```

---

# Bot callback and keyboards
In the callback query we will define the behaviour to follow according to the value of **callback_data**

```python
    def on_callback_query(self,msg):
        query_ID , chat_ID , query_data = telepot.glance(msg,flavor='callback_query')

        
        payload = self.__message.copy()
        payload['e'][0]['v'] = query_data
        payload['e'][0]['t'] = time.time()
        self.client.myPublish(self.topic, payload)
        self.bot.sendMessage(chat_ID, text=f"Led switched {query_data}")
```