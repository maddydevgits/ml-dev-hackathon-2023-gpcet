import telebot
import ast
import pickle

model=pickle.load(open('model.pkl','rb'))

botToken='5824896965:AAEIv2CfwVQmDo_hOrgvH7EO1e4SeYzZYHo'
bot=telebot.TeleBot(
    botToken,
    parse_mode=None)

# handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Welcome to my Bot\nEnter years of Experience")

@bot.message_handler(regexp="[a-zA-Z0-9_]")
def handle_message(message):
    print(message)
    message=str(message)
    k=ast.literal_eval(message)
    userid=k['from_user']['id']
    try:
        yoe=float(k['text'])
        print(yoe)
        result=model.predict([[yoe]])[0]
        bot.send_message(int(userid),'Your expected salary is '+str(result))
    except:
        print('Invalid')
        bot.send_message(int(userid),'Invalid input')




bot.polling()
