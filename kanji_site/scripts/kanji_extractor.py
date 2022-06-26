import re
import bs4.element
import requests
from bs4 import BeautifulSoup
import unicodedata
import csv

page = requests.get('https://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji').text
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table', class_="sortable")


def clean_value(value):
    return re.sub(r'[[0-9]+]', '', value).strip()


def remove_tags(reading_field):
    for item in reading_field[:]:
        if type(item) is bs4.element.Tag:
            reading_field.remove(item)


def extract_readings(reading_field: list):
    remove_tags(reading_field)
    all_readings = {'kun': [], 'kun_romaji': [], 'on': [], 'on_romaji': []}
    japanese_readings = reading_field[0].split('、')
    english_readings = reading_field[1][0:-1].split(',')
    for read_index, field in enumerate(japanese_readings):
        if any('KATAKANA' in unicodedata.name(character) for character in field):
            all_readings['on'].append(field)
            all_readings['on_romaji'].append(english_readings[read_index].replace('ō', 'ou').replace('ū', 'uu'))
        else:
            all_readings['kun'].append(field)
            all_readings['kun_romaji'].append(english_readings[read_index].replace('ō', 'ou').replace('ū', 'uu'))
    return all_readings


with open('Kanji/kanji_site/scripts/csv_files/kanji_table.csv', 'w', encoding='UTF8') as csv_file, \
        open('Kanji/kanji_site/scripts/csv_files/Kanji_database_table.csv', 'r', encoding='UTF8') as kanji_db:
    header = ['id', 'Kanji', 'Old Kanji', 'Radical', 'Strokes', 'Grade', 'JLPT', 'Meanings',
              'Kun yomi', 'Kun romaji', 'On yomi', 'On romaji']
    writer = csv.writer(csv_file)
    writer.writerow(header)
    reader = csv.DictReader(kanji_db)

    for tr, db_kanji_line in zip(table.find_all('tr')[1:], reader):
        tds = tr.find_all('td')
        index = tds[0].text.strip()
        kanji = unicodedata.normalize('NFKC', clean_value(tds[1].text))
        old_kanji = unicodedata.normalize('NFKC', clean_value(tds[2].text))
        if index == '1814':
            radical = unicodedata.normalize('NFKC', '廾')
        else:
            radical = unicodedata.normalize('NFKC', tds[3].text.strip())
        strokes = tds[4].text.strip()
        grade = tds[5].text.strip()
        meaning = tds[7].text.strip()
        readings = extract_readings(tds[8].contents)
        jlpt_level = db_kanji_line.get('JLPT-test', '--')
        row = [index, kanji, f"{', '.join(old_kanji)}", radical, strokes, grade, jlpt_level, f"{meaning}", f"{', '.join(readings['kun'])}",
               f"{', '.join(readings['kun_romaji'])}", f"{', '.join(readings['on'])}", f"{', '.join(readings['on_romaji'])}"]
        writer.writerow(row)
