from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# توکن ربات از محیط گرفته می‌شود (از طریق تنظیمات Render)
TOKEN = os.getenv("BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! به ربات زیبـاشو خوش اومدی.")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # دستور /start
    dp.add_handler(CommandHandler("start", start))

    # راه‌اندازی ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
