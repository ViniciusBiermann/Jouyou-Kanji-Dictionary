import csv

from kanji_dictionary.models import Kanji
from kanji_dictionary.models import Radical


def run():
    with open('scripts/csv_files/kanji_table.csv') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)

        Kanji.objects.all().delete()

        for row in reader:
            print(row)
            kanji_id = row[0]
            character = row[1]
            old_character = row[2]
            radical_character = row[3]
            radical_entry = Radical.objects.get(character=radical_character)
            print(radical_entry)
            strokes = row[4]
            grade = row[5]
            meaning = row[6]
            kun_yomi = row[7]
            kun_romaji = row[8]
            on_yomi = row[9]
            on_romaji = row[10]
            kanji = Kanji(id=kanji_id, character=character, old_character=old_character, strokes=strokes, grade=grade,
                          meaning=meaning, kun_yomi=kun_yomi, kun_romaji=kun_romaji, on_yomi=on_yomi, on_romaji=on_romaji)
            kanji.save()
