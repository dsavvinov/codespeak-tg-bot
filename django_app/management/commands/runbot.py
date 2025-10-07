"""Django management command to run the Telegram bot."""

from django.core.management.base import BaseCommand
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from bot import main


class Command(BaseCommand):
    help = 'Run the Telegram bot'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting Telegram bot...'))
        try:
            main()
        except KeyboardInterrupt:
            self.stdout.write(self.style.SUCCESS('Bot stopped.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error running bot: {e}'))
            raise