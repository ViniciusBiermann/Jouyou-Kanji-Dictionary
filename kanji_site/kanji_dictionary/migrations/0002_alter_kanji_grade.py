# Generated by Django 4.0.5 on 2022-06-16 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanji_dictionary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanji',
            name='grade',
            field=models.CharField(help_text='Grade the kanji is taught.', max_length=200),
        ),
    ]