import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Открываем файл с телефонами
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # Создаем новый объект модели Phone
            phone_obj = Phone(
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'] == 'True',  # Преобразуем строку в логическое значение
                slug=slugify(phone['name'])  # Генерируем slug на основе name
            )
            # Сохраняем объект в базе данных
            phone_obj.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported phones'))