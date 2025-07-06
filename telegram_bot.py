# DOCS: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot

import logging
import os

from dotenv import load_dotenv
from typing import Optional, Dict, Callable, Awaitable

from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()

class TelegramBot:
    def __init__(self, bot_name: str = ""):
        self.token = os.getenv("TG_TOKEN")
        self.application = ApplicationBuilder().token(self.token).build()
        self.bot_name = bot_name

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="I'm a bot, please talk to me!"  # You can customize this
        )

    def add_command_handlers(self, handlers: Optional[Dict[str, Callable[[Update, ContextTypes.DEFAULT_TYPE], Awaitable[None]]]] = None):
        start_handler = CommandHandler('start', self.start)
        self.application.add_handler(start_handler)

        if handlers:
            for name, func in handlers.items():
                self.application.add_handler(CommandHandler(name, func))

    def add_message_handler(self, func: Callable[[Update, ContextTypes.DEFAULT_TYPE], Awaitable[None]]):
        handler = MessageHandler(filters.TEXT & ~filters.COMMAND, func)
        self.application.add_handler(handler)

    def run(self):
        self.application.run_polling()





