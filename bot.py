from telegram import Update
from telegram.ext import (
    Application,  # جایگزین Updater در نسخه‌های جدید
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('سلام! ربات امضای من آماده است.\nفایل مورد نظر را برای امضا ارسال کنید.')

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    document = update.message.document
    await update.message.reply_text(
        f'فایل دریافت شد!\n'
        f'نام فایل: {document.file_name}\n'
        f'حجم فایل: {document.file_size} بایت\n'
        'در حال پردازش برای افزودن امضا...'
    )
    # اینجا می‌توانید عملیات امضا زدن به فایل را اضافه کنید

def main() -> None:
    application = Application.builder().token("7774050939:AAElUM4iRvmGi_6ayCk27Syp4XIu6fCcsJs").build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    
    application.run_polling()

if __name__ == '__main__':
    main()
