from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class TrackList(ListView):
    pass

class TrackDetail(DetailView):
    pass

class TrackCreate(CreateView):
    pass

class TrackUpdate(UpdateView):
    pass

class TrackDelete(DeleteView):
    pass


class AlbumList(ListView):
    pass

class AlbumDetail(DetailView):
    pass

class MusicianList(ListView):
    pass

class MusicianDetail(DetailView):
    pass

class GenreList(ListView):
    pass

class GenreDetail(DetailView):
    pass

class TagList(ListView):
    pass

class TagDetail(DetailView):
    pass