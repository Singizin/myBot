import telebot
from telebot.types import Message
from telebot import apihelper
from lego import do_lego
import os

def ReadUser():
    global USERS
    j=0
    f = open('Users.txt','r')
    line = f.readline()
    while line:
        print(line)
        print(int(line[0:9]))
        USERS.add(int(line[0:9]))
        line = f.readline()
    return

apihelper.proxy = {'https': 'https://149.56.102.220:3128'}
#TOKEN = '747611758:AAEpFP3iLMCbtmrLF0omSyTnjP7d7CCIaPY'
TOKEN='854025714:AAH9Wi3_rWfVJvjnbDgNWkL8hYCbH2Fr-wY'
bot = telebot.TeleBot(TOKEN)
i=0
USERS = set()
bot.send_message(260119686, "Go")


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    try:
        if message.caption!=None:
            if int(message.caption)>640or int(message.caption)<10:
                bot.send_message(message.chat.id, 'Размер должен быть в диапазоне от 10 до 640, Вы ввели \'{}\' =(\n\n'
                                                  'Если оставить поле пустым фото будет сжато в 32 раза\n\n'
                                                    'Попробуйте еще раз!\n'.format(message.caption))
                return
            else:
                N = int(message.caption)
        else:
            N=32
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        print('Новый файл - ', str(file_info.file_path))
        src = 'D:/Python/Charm/mymyBot/files/' + file_info.file_path;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "Хорошее фото, уже собираем!")
        name = file_info.file_path[7::]
        flag = do_lego(name, N)
        if flag:
            photo_lego = open('files/result/result_{}'.format(name),'rb')
            bot.send_photo(message.from_user.id, photo_lego)
            global i
            i+=1
            bot.send_message(260119686, "{} попробовал сделать фото. Всего: {}".format(message.from_user.first_name,i))
            photo_lego.close()
            os.remove('files/result/result_{}'.format(name))
            os.remove('files/photos/{}'.format(name))

    except Exception as e:
        bot.reply_to(message, e)

def AddUsers(s):
    f = open('Users.txt', 'a')
    f.write(s+'\n')
    f.close()

@bot.message_handler(commands=['start'])
def command_handler(message: Message):
    ReadUser()
    if message.from_user.id in USERS:
        bot.send_message(message.chat.id,'Уже знакомы, {} \n'
                                         'Можешь прислать мне фотографию и я соберу её и кубиков LEGO.\n'
                                         'Чтобы выбрать размер кубиков напиши число в описание фотографии (Добавить подпись)'
                                         'значение в диапазоне 10..640\n'
                                         'Если оставить поле пустым фото будет сжато в 32 раза.'.format(message.from_user.first_name))
    else:
        USERS.add(message.from_user.id)
        AddUsers(str(message.from_user.id) + '; name: ' + str(message.from_user.first_name)+' '+ str(message.from_user.last_name) + '; Зарегистрирован: '+str(message.date))
        bot.send_message(message.chat.id,'Привет 👋\n'
                                         'Можешь прислать мне фотографию и я соберу её и кубиков LEGO.\n'
                                         'Чтобы выбрать размер кубиков напиши число в описание фотографии (Добавить подпись)'
                                         'значение в диапазоне 10..640\n'
                                         'Если оставить поле пустым фото будет сжато в 32 раза.')
        bot.send_message(260119686, "Новый пользователь {} {}".format(message.from_user.first_name, message.from_user.id))

@bot.message_handler(commands=['sebek'])
def command_handler(message: Message):
    sebek= open('files/1.jpg','rb')
    bot.send_photo(message.chat.id, sebek )

@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    bot.send_message(260119686, "{}".format(message.text))
    bot.send_message(message.from_user.id, "Все текстовые сообщения попадут в базу ошибок, бот общаться не умеет\n\n"
                                           "Если обнаружился баг или ошибка,то напиши об этом текстом")

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        apihelper.proxy = {'https': 'https://149.56.102.220:3128'}
        TOKEN = '854025714:AAH9Wi3_rWfVJvjnbDgNWkL8hYCbH2Fr-wY'
        bot = telebot.TeleBot(TOKEN)
        continue
