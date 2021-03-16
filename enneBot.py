from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Enne')

bot = ChatBot(
    'Enne',
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    database_uri = 'sqlite:///database.sqlite3'
    )

conversation = ListTrainer(bot)
conversation.train([
    'Oi'
    'Óla mestre!'
    'Tudo bem?'
    'Tudo bem e você?'
    'Que dia é hoje?'
    'Não sei'
    'O que está fazendo?'
    'Servindo o meu mestre!'
])

while True:
    try:
        answer = bot.get_response(input("User: "))
        if float(answer.confidence) > 0.5:
            print("Enne: ",answer)
        else:
            print("Não entendi!")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
