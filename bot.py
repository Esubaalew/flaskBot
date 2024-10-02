from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler
import os

# Initialize Flask app
app = Flask(__name__)

# Initialize the Telegram Bot

bot = Bot(token=os.getenv('TOKEN'))

# Initialize dispatcher
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

# Define command handlers
def start(update: Update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text='''
    Hello there!!
    ''')


# Add handlers to dispatcher
dispatcher.add_handler(CommandHandler("start", start))

# Define webhook route
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    dispatcher.process_update(update)
    return "ok"

# Set webhook
@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    webhook_url = f"https://example.et/{TOKEN}"
    bot.set_webhook(webhook_url)
    return f"Webhook set to {webhook_url}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
