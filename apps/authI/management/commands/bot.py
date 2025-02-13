from django.core.management.base import BaseCommand
from ...views_bot import bot


class Command(BaseCommand):

    def handle(self, *args, **options):
        bot.polling()