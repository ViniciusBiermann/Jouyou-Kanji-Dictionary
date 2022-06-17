import csv

from kanji_dictionary.models import Radical


def run():
    with open('scripts/csv_files/radicals.csv') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)

        Radical.objects.all().delete()

        for row in reader:
            print(row)
            radical_id = row[0]
            strokes = row[1]
            character = row[2]
            meaning = row[3]
            japanese_reading = row[4]
            romaji_reading = row[5]
            radical = Radical(id=radical_id, strokes=strokes, character=character, meaning=meaning,
                              japanese_reading=japanese_reading, romaji_reading=romaji_reading)
            radical.save()
