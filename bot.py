import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("سلام! من ربات زیبـاشـو هستم.")

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
