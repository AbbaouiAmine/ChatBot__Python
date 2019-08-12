from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('test') #creation de mon chatbot
conv = open('corpus/f1.txt','r').readlines()	#charger le dataset
trainer = ListTrainer(bot) #model d entrainement
trainer.train(conv) #entrainement

while True:
    try :
        request = input('you : ')
        response = bot.get_response(request)
        print('kabour : '+ response)
    except(KeyboardInterrupt,EOFError,SyntaxError):
        break