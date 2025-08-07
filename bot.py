from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سلام! ربات امضای من آماده است.')

def handle_document(update: Update, context: CallbackContext) -> None:
    # اینجا کد پردازش فایل برای افزودن امضا قرار می‌گیرد
    update.message.reply_text('فایل شما امضا شد!')

def main():
    updater = Updater("7774050939:AAElUM4iRvmGi_6ayCk27Syp4XIu6fCcsJs", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.document, handle_document))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
