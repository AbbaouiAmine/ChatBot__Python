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



while True:
    message=input('\t\t\tYou:')
    #print(message)
    if message.strip()!='baslama':
        reply=bot.get_response(message)
        print('Bot:',reply)
    if message.strip()=='baslama':
        print('Bot: thalaaa')
        break
