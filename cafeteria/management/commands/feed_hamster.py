from django.core.management.base import BaseCommand

from cafeteria.tasks import feed_hamster


class Command(BaseCommand):
    help = "커맨드 설명"

    def handle(self, *args, **kwargs):
        a = feed_hamster.delay()
        print(a)
        print("aa")
