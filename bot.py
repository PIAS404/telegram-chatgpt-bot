import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import openai

# লোড এনভায়রনমেন্ট ভ্যারিয়েবল
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# OpenAI সেটআপ
openai.api_key = OPENAI_API_KEY

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('হ্যালো! আমি ChatGPT-এর সাথে কানেক্টেড। কিছু জিজ্ঞাসা করুন!')

async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    try:
        # OpenAI-এ পাঠান
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response['choices'][0]['message']['content']
        await update.message.reply_text(bot_reply)
    except Exception as e:
        await update.message.reply_text(f'এরর: {str(e)}')

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()
