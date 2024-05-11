import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))


        for phone in phones:
            Phone.objects.create(
                id=int(phone['id']),
                model=phone['name'],
                price=int(phone['price']),
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=bool(phone['lte_exists']),
                slug=phone['name'].lower().replace(' ', '_'),
            )
            # TODO: Добавьте сохранение модели

        self.stdout.write(self.style.SUCCESS('Успешно!'))
