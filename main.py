"""CodeSpeak Telegram Bot - Main application."""

import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from config import get_telegram_bot_token

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Hello, CodeSpeak + Telegram")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle all incoming messages with the greeting."""
    await update.message.reply_text("Hello, CodeSpeak + Telegram")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    logger.error("Exception while handling an update:", exc_info=context.error)


def main() -> None:
    """Start the bot."""
    try:
        # Get the bot token
        token = get_telegram_bot_token()

        # Create the Application
        application = Application.builder().token(token).build()

        # Register handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        # Register error handler
        application.add_error_handler(error_handler)

        logger.info("Starting CodeSpeak Telegram Bot...")

        # Run the bot until the user presses Ctrl-C
        application.run_polling(allowed_updates=Update.ALL_TYPES)

    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")
        exit(1)


if __name__ == '__main__':
    main()