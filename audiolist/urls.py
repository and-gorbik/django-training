from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="audiolist/index.html"), name='index'),
    path('tracks/', views.TrackList.as_view(), name='tracks'),
    path('tracks/<int:pk>/', views.TrackDetail.as_view(), name='track'),
    path('tracks/add/', views.TrackCreate.as_view(), name='create_track'),
    path('tracks/<int:pk>/edit/', views.TrackUpdate.as_view(), name='update_track'),
    path('tracks/<int:pk>/delete/', views.TrackDelete.as_view(), name='delete_track'),
    path('albums/', views.AlbumList.as_view(), name='albums'),
    path('albums/<int:pk>/', views.AlbumDetail.as_view(), name='album'),
    path('musicians/', views.MusicianList.as_view(), name='musicians'),
    path('musicians/<str:slug>/', views.MusicianDetail.as_view(), name='musician'),
    path('genres/', views.GenreList.as_view(), name='genres'),
    path('genres/<str:slug>/', views.GenreDetail.as_view(), name='genre'),
    path('tags/', views.TagList.as_view(), name='tags'),
    path('tags/<str:slug>/', views.TagDetail.as_view(), name='tag'),
]