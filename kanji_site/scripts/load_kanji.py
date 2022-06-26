import csv
import unicodedata

from kanji_dictionary.models import Kanji
from kanji_dictionary.models import Radical


def run():
    with open('scripts/csv_files/kanji_table.csv', 'r', encoding='UTF8') as file:
        reader = csv.DictReader(file)
        Kanji.objects.all().delete()

        for row in reader:
            kanji_id = row.get('id')
            character = unicodedata.normalize('NFKC', row.get('Kanji'))
            old_character = unicodedata.normalize('NFKC', row.get('Old Kanji'))
            radical_character = unicodedata.normalize('NFKC', row.get('Radical'))
            radical_entry = Radical.objects.get(character=radical_character)
            strokes = row.get('Strokes')
            grade = row.get('Grade')
            jlpt = row.get('JLPT')
            meaning = row.get('Meanings')
            kun_yomi = row.get('Kun yomi')
            kun_romaji = row.get('Kun romaji')
            on_yomi = row.get('On yomi')
            on_romaji = row.get('On romaji')
            kanji = Kanji(id=kanji_id, character=character, old_character=old_character, radical=radical_entry, strokes=strokes,
                          grade=grade, jlpt=jlpt, meaning=meaning, kun_yomi=kun_yomi, kun_romaji=kun_romaji, on_yomi=on_yomi,
                          on_romaji=on_romaji)
            kanji.save()
