from django.db import models
from django.urls import reverse


class Radical(models.Model):
    id = models.IntegerField(help_text='ID for the radical.', primary_key=True)
    character = models.CharField(max_length=2, help_text='The radical character.')
    strokes = models.IntegerField(help_text='Number of strokes.')
    meaning = models.CharField(max_length=200, help_text='The meaning of the radical.')
    japanese_reading = models.CharField(max_length=200, help_text='The japanese reading of the radical character.')
    romaji_reading = models.CharField(max_length=200, help_text='The romaji reading of the radical character.')

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.character}"

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('Radical-detail', args=[str(self.id)])


class Kanji(models.Model):
    id = models.IntegerField(help_text='ID for the kanji.', primary_key=True)
    character = models.CharField(max_length=2, help_text='The kanji character.')
    old_character = models.CharField(max_length=2, help_text='The old kanji character.')
    radical = models.ForeignKey('Radical', on_delete=models.SET_NULL, null=True)
    strokes = models.IntegerField(help_text='Number of strokes.')
    grade = models.CharField(max_length=200, help_text='Grade the kanji is taught.')
    jlpt = models.IntegerField(help_text='Level where this kanji appears on the Japanese Language Proficiency Test.')
    meaning = models.CharField(max_length=200, help_text='The meaning of the kanji.')
    kun_yomi = models.CharField(max_length=200, help_text='The kun yomi reading of the kanji.')
    kun_romaji = models.CharField(max_length=200, help_text='The kun yomi reading of the kanji in romaji.')
    on_yomi = models.CharField(max_length=200, help_text='The on yomi reading of the kanji.')
    on_romaji = models.CharField(max_length=200, help_text='The on yomi reading of the kanji in romaji.')
    klc_index = models.IntegerField(help_text="Index of the kanji in Kodansha's Kanji Learner's Course book.", null=True)

    class Meta:
        ordering = ['id', 'strokes', 'grade', 'klc_index']

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.character}"

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('kanji-dictionary-kanji-detail', args=[str(self.id)])
