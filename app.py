# DOCS: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot

import logging
from telegram import Update
from telegram.ext import ContextTypes
from telegram_bot import TelegramBot
from langchain_integration import LangchainModel

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Create model instance
model = LangchainModel(bot_name='Raya')

# Message handler that uses the model
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    bot_reply = model.reply(user_message)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=bot_reply)

# Command handlers
commands = {
}


if __name__ == '__main__':
    bot  = TelegramBot(bot_name='Raya')

    # Add commands
    bot.add_command_handlers(handlers=commands)

    # ---- NORMAL MESSAGES --- #
    bot.add_message_handler(func=handle_message)

    # Start polling
    bot.run()

