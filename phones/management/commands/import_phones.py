import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from datetime import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                phone_model = Phone()
                phone_model.name = line[1]
                phone_model.price = int(line[3])
                phone_model.image = line[2]
                phone_model.release_date = datetime.strptime(line[4], '%Y-%m-%d').date()
                phone_model.lte_exists = bool(line[5])
                slug_text = phone_model.name
                slug_text = slug_text.lower()
                slug_text = slug_text.replace(' ', '-')
                phone_model.slug = slug_text
                phone_model.save()
                pass
