from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import os
import requests

bot=ChatBot("test")
#bot.set_trainer(ListTrainer)
trainer = ListTrainer(bot)
for file in os.listdir('corpus'):
    conv=open('corpus/'+file,'r').read().splitlines()
    trainer.train(conv)

words = ['ta9s','fi','casa']

while True:
    try:
        message=input('\t\t\tYou:')
        reply = bot.get_response(message)
        if all(x in message.split() for x in words) :
            resp=requests.get("http://api.openweathermap.org/data/2.5/weather?q=casablanca&appid=50b8f29881482c8f59b3e73615e4dd38")
            if resp.status_code==200:
                data=resp.json()
                tem=data.get('main')
                tem=tem.get('temp')
                reply=tem
            else:
                reply="sir chouf nachra"
        print('Rebot : ',reply)
    except(KeyboardInterrupt,EOFError,SyntaxError):
        break