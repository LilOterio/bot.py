
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from random import randint
from pg import contas
STATE1 = 1
STATE2 = 2

def welcome(updater, context):
    message= 'Seja bem vindo ao jogo da bola de cristal \npara começar a jogar clique aqui -> /boladecristal <- !!!!'
    print(message)
    context.bot.send_message(chat_id=updater.effective_chat.id, text= message)

def bola_de_cristal(update,context):
    try:
        message = 'Faça uma pergunta que possa ser respondida com sim ou nao!!!! se quiser que a bola de cristal adivinhe a  idade de alguem  \npergunte algo do tipo (quantos anos eu tenho)\nSe você quizer saber alguma data de um acontecimento\npergunte algo do tipo (que dia.....)\nSe a sexualidade de alguem \npergunte algo do tipo (qual é a sexualidae do/da.....)\n Não esqueça de colocar ponto de interrogação no final de sua pergunta '
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True))
        return STATE1
    except Exception as e:
        print(str(e))

def inputPergunta(update,context):
    pergunta = update.message.text
    if '?'in pergunta:
        if 'anos' in pergunta:
            message = f'{randint(0,100)} anos '
            print(pergunta)
            print(message)
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        elif 'dia' in pergunta:
            mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
            num = randint(0,12)
            if mes == 'Fevereiro':
                dia =randint(0,28)
            else:
                dia =randint(0,31)
            message = f'{dia} de {mes[num]}'
            print(pergunta)
            print(message)
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        elif 'sexualidade' in pergunta :
            sex = ['Gayzasso','Bi','Pan','Sapata','Trouxa','Ninguem quer ksksk','traveco kk','Axessual','Hetero']
            num = randint(0,8)
            message = f'{sex[num]}'
            print(pergunta)
            print(message)            
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        else:
            message = ['sim...', 'não...', 'Mas é obvio ue kssksks', 'provavelmente ','pergunta sua mãe ue ',
                        'kskssks claro ','talvez', 'jamais', 'nunca', 'não sou capaz de responder']
            num = randint(0, 9)
            print(pergunta)
            print(message[num])
            context.bot.send_message(chat_id=update.effective_chat.id, text=message[num])
    elif pergunta != '/boladecristal':
        message = 'Digite sua pergunta com ponto de interrogação por favor!!!'
        print(pergunta)
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        
    else:
        message = 'Faça uma pergunta que possa ser respondida com sim ou nao!!!! \nNão esqueça de colocar ponto de interrogação no final de sua pergunta '
        print(pergunta)
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True))       

def inputPergunta2(update, context):
    try:
        pergunta = update.message.text
        message = "Foi um prazer advinhar "
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    except Exception as e:
        print(str(e))   
def cancel(update, context):
    return ConversationHandler.END

def main():
    token = '1165215955:AAES292Q4BwqUEcbddy5aC2uAXjCZFr6vQM'
    updater = Updater(token=token,use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome)) 

    conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('boladecristal',bola_de_cristal)],
        states={
            STATE1: [MessageHandler(Filters.text, inputPergunta)],
            STATE2: [MessageHandler(Filters.text, inputPergunta2)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])

    updater.dispatcher.add_handler(conversation_handler)
    updater.start_polling()
    print(str(updater))
    updater.idle()


if __name__ == '__main__':
    main()
    