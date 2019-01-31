from django_hash_field import HashField
from django.db import models, IntegrityError
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
from . import managers
from hashlib import sha1
from django.core.exceptions import ValidationError

class Musician(models.Model):
    name = models.CharField(max_length=100, unique=True, default="unknown")
    slug = models.SlugField(max_length=150, default="", editable=False)
    objects = managers.MusicianManager()

    def get_absolute_url(self):
        return reverse('musician', kwargs={'pk': self.pk})

    def __str__(self):
        return self.slug


def default_musician():
    return Musician.objects.get_or_create(name='unknown')[0].pk

class Album(models.Model):
    name = models.CharField(max_length=100, default="unknown")
    published_at = models.DateField(null=True, blank=True)
    musician = models.ForeignKey(Musician, on_delete=models.SET_DEFAULT, default=default_musician, blank=True)
    objects = managers.AlbumManager()

    class Meta:
        unique_together = ('name', 'musician')

    def get_absolute_url(self):
        return reverse('album', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name.lower()


def default_album():
    return Album.objects.get_or_create(name='unknown', musician__name='unknown')[0].pk

class Track(models.Model):
    name = models.CharField(max_length=100)
    filehash = HashField(editable=False, db_index=True)
    data = models.FileField(upload_to='audiolist/music/')
    album = models.ForeignKey(Album, on_delete=models.SET_DEFAULT, default=default_album, blank=True)
    genres = models.ManyToManyField('Genre', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    objects = managers.TrackManager()

    def get_absolute_url(self):
        return reverse('track', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name.lower()

class Genre(models.Model):
    POP = 'po'
    INDIE = 'in'
    ROCK = 'ro'
    METAL = 'me'
    ALTERNATIVE = 'al'
    ELECTRONIC = 'el'
    DANCE = 'da'
    RAP = 'ra'
    RNB = 'rb'
    JAZZ = 'ja'
    BLUES = 'bl'
    REGGAE = 're'
    SKA = 'sk'
    PUNK = 'pu'
    CLASSICAL = 'cl'
    RETRO = 'rt'
    CHANSON = 'ch'
    COUNTRY = 'co'
    BARD = 'ba'
    SOUNDTRACK = 'so'
    ETHNIC = 'et'
    CHILDREN = 'ci'

    GENRES = (
        (POP, 'pop'),
        (INDIE, 'indie'),
        (ROCK, 'rock'),
        (METAL, 'metal'),
        (ALTERNATIVE, 'alternative'),
        (ELECTRONIC, 'electronic'),
        (DANCE, 'dance'),
        (RAP, 'rap'),
        (RNB, 'rnb'),
        (JAZZ, 'jazz'),
        (BLUES, 'blues'),
        (REGGAE, 'reggae'),
        (SKA, 'ska'),
        (PUNK, 'punk'),
        (CLASSICAL, 'classical'),
        (RETRO, 'retro'),
        (CHANSON, 'chanson'),
        (COUNTRY, 'country'),
        (BARD, 'bard'),
        (SOUNDTRACK, 'soundtrack'),
        (ETHNIC, 'ethnic'),
        (CHILDREN, 'children\'s'),
    )

    name = models.CharField(max_length=2, choices=GENRES)
    objects = managers.GenreManager()

    def get_absolute_url(self):
        return reverse('genre', kwargs={'slug': self.name})

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, default="", editable=False)
    objects = managers.TagManager()

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    def __str__(self):
        return self.slug


@receiver(pre_save, sender=Track)
def set_file_hash(sender, instance, **kwargs):
    instance.filehash = sha1(instance.data.read()).hexdigest()

@receiver(pre_save, sender=Musician)
def set_track_slug_field(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)

@receiver(pre_save, sender=Tag)
def set_tag_slug_field(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
