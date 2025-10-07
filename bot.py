"""Telegram bot that responds with 'Hello, Codespeak + Telegram' to all DMs."""

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import get_telegram_bot_token


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle all incoming messages and respond with greeting."""
    # Only respond to private messages (DMs)
    if update.effective_chat.type == 'private':
        await update.message.reply_text("Hello, Codespeak + Telegram")


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command."""
    if update.effective_chat.type == 'private':
        await update.message.reply_text("Hello, Codespeak + Telegram")


def main() -> None:
    """Run the bot."""
    try:
        # Get bot token from configuration
        bot_token = get_telegram_bot_token()

        # Create the Application
        application = Application.builder().token(bot_token).build()

        # Add handlers
        application.add_handler(CommandHandler("start", start_command))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        # Run the bot
        logger.info("Starting Telegram bot...")
        application.run_polling(allowed_updates=Update.ALL_TYPES)

    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        print(f"Configuration error: {e}")
        exit(1)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
        exit(1)


if __name__ == '__main__':
    main()