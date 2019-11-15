import json
from MyMQTT import *
import time
class LedClient():
    def __init__(self,clientID,topic):
        self.clientID=clientID
        self.topic=topic
        self.client=MyMQTT('LedClient','mqtt.eclipse.org',1883,self)
        self.message={'client': clientID,'n':'switch','value':'', 'timestamp':''}
    def run(self):
        self.client.start()
        print('{} has started'.format(self.clientID))
    
    def end(self):
        self.client.stop()
        print('{} has stopped'.format(self.clientID))
    def notify(self,topic,msg):
        pass
    def publish(self,value):
        self.message['timestamp']=str(time.time())
        self.message['value']=value
        self.client.myPublish(self.topic,str(self.message))

def main():
    led_client=LedClient('ledClient','Led') 
    led_client.run()
    print('Welcome to the client to switch on/off the lamp\n')
    done=False
    command_list='Type:\n"on" to set the light on\n"off" to set it off\n"q" to quit\n'
    while not done:
        print(command_list)
        user_input=input()
        if user_input=="on":
            led_client.publish(user_input)
        elif user_input=="off":
            led_client.publish(user_input)
        elif user_input=='q':
            done=True
        else:
            print('Unknown command')
    led_client.end()
        
if __name__ == "__main__":
   main() 
