from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import config
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

chat_id = config.CHAT_ID


def start_handler(update, context):
    text = 'Привет! В каком формате прислать данные?'
    keyboard = [
        [InlineKeyboardButton(text='Получить JSON', callback_data='get_json'), ],
        [InlineKeyboardButton(text='Получить XLSX', callback_data='get_xlsx'), ]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(text=text, reply_markup=markup)


def callback_handler(update, context):
    query = update.callback_query
    query.answer()
    filenames = {
        'get_json': "./shop_parser/shop_parser/dump2.json",
        'get_xlsx': "./shop_parser/shop_parser/innovation2.xlsx",
        
    }
    if query.data in ('get_xlsx', 'get_json'):
        filename = filenames[query.data]
        with open(filename, 'rb') as f:
            context.bot.send_document(query.message.chat_id, document=f)

 
updater = Updater(config.TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start_handler))
updater.dispatcher.add_handler(CallbackQueryHandler(callback_handler))

# RUN
updater.start_polling()
updater.idle()
