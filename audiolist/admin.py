from django.contrib import admin
from .models import Album, Musician, Track, Tag, Genre

# Register your models here.
admin.site.register(Album)
admin.site.register(Musician)
admin.site.register(Track)
admin.site.register(Tag)
admin.site.register(Genre)