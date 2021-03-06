# Generated by Django 4.0.5 on 2022-06-16 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Radical',
            fields=[
                ('id', models.IntegerField(help_text='ID for the radical.', primary_key=True, serialize=False, unique=True)),
                ('character', models.CharField(help_text='The radical character.', max_length=2)),
                ('strokes', models.IntegerField(help_text='Number of strokes.')),
                ('meaning', models.CharField(help_text='The meaning of the radical.', max_length=200)),
                ('japanese_reading', models.CharField(help_text='The japanese reading of the radical character.', max_length=200)),
                ('romaji_reading', models.CharField(help_text='The romaji reading of the radical character.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Kanji',
            fields=[
                ('id', models.IntegerField(help_text='ID for the kanji.', primary_key=True, serialize=False, unique=True)),
                ('character', models.CharField(help_text='The kanji character.', max_length=2)),
                ('old_character', models.CharField(help_text='The old kanji character.', max_length=2)),
                ('strokes', models.IntegerField(help_text='Number of strokes.')),
                ('grade', models.IntegerField(help_text='Grade the kanji is taught.')),
                ('meaning', models.CharField(help_text='The meaning of the kanji.', max_length=200)),
                ('kun_yomi', models.CharField(help_text='The kun yomi reading of the kanji.', max_length=200)),
                ('kun_romaji', models.CharField(help_text='The kun yomi reading of the kanji in romaji.', max_length=200)),
                ('on_yomi', models.CharField(help_text='The on yomi reading of the kanji.', max_length=200)),
                ('on_romaji', models.CharField(help_text='The on yomi reading of the kanji in romaji.', max_length=200)),
                ('klc_index', models.IntegerField(help_text="Index of the kanji in Kodansha's Kanji Learner's Course book.")),
                ('radical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kanji_dictionary.radical')),
            ],
            options={
                'ordering': ['id', 'strokes', 'grade', 'klc_index'],
            },
        ),
    ]
