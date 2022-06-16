from Kanji.kanji_site.kanji_dictionary.models import Radical
import csv
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kanji_site.settings')
django.setup()


def run():
    with open('Kanji/kanji_site/scripts/csv_files/radicals.csv') as file:
        reader = csv.reader(file, delimeter=',')
        next(reader)

        Radical.objects.all().delete()


if __name__ == '__main__':
    run()
