import telebot
import config
import requests

filename = "innovation.xlsx"
bot = telebot.TeleBot(config.TOKEN)

# def send_photo_url(chat_id, img_url):
#     requests.get(f'{config.URL}{config.TOKEN}/sendPhoto?chat_id={config.CHAT_ID}&photo={filename}')

# def send_document(filename):
#      url = 'https://api.telegram.org/bot{config.TOKEN}/sendDocument'.format(config.TOKEN)
#      data = {'chat_id': config.CHAT_ID, 'caption': 'Результат парсинга'}
#      print("hello world")
#      with open(filename, 'rb') as f:
#          files = {'document': f}
#          print("filllelelelelelelelelle", files);
#          response = requests.post(url, data=data, files=files)
#          print(response.json())
 
    
@bot.message_handler(content_types=['text'])
def send_documentation(message):
    try:
        # bot.send_message(message.chat.id, message.text)
        # bot.send_message(message.chat.id, message.chat.id)
        
        doc = open('./innovation.xlsx', 'rb')
        bot.send_document(message.chat.id, doc)
        bot.send_document(message.chat.id, "FILEID") 
        # requests.post(f'{config.URL}{config.TOKEN}/sendPhoto?chat_id={config.CHAT_ID}&photo={"https://s1.1zoom.ru/big3/256/359188-svetik.jpg"}')
    except Exception as e:
        pass
        # bot.reply_to(message, e)
    
# RUN
bot.polling(none_stop=True, interval=0)
