from telegram.ext import Application, CommandHandler, MessageHandler, filters
from datetime import datetime
import os

TOKEN = "7774050939:AAElUM4iRvmGi_6ayCk27Syp4XIu6fCcsJs"

async def start(update, context):
    user = update.effective_user
    await update.message.reply_text(
        f"سلام {user.first_name}!\n"
        "فایل APK را برای دریافت اطلاعات امضا ارسال کنید."
    )

async def handle_apk(update, context):
    file = await update.message.document.get_file()
    
    # ذخیره موقت فایل
    file_path = f"temp_{datetime.now().timestamp()}.apk"
    await file.download_to_drive(file_path)
    
    # اینجا می‌توانید از کتابخانه‌های قانونی برای تحلیل APK استفاده کنید
    # مانند:
    # from androguard.core import APK
    # a = APK(file_path)
    # signature = a.get_signature_name()
    
    await update.message.reply_text(
        "✅ فایل دریافت شد\n"
        "📦 نام فایل: " + update.message.document.file_name + "\n"
        "📏 حجم: " + str(update.message.document.file_size) + " بایت\n"
        "⚠️ توجه: این ربات فقط برای تحلیل فایل‌هاست\n"
        "برای نصب باید تنظیمات امنیتی دستگاه را موقتاً تغییر دهید"
    )
    
    # حذف فایل موقت
    os.remove(file_path)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.MIME_TYPE("application/vnd.android.package-archive"), handle_apk))

print("ربات تحلیلگر APK فعال شد...")
app.run_polling()
