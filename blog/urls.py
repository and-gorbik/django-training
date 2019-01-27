from django.urls import path
from .views import article, articles, create_article
from .views import update_article, delete_article

urlpatterns = [
    path('', articles, name='index'),
    path('articles/', articles, name='articles'),
    path('articles/new/', create_article, name='new_article'),
    path('articles/<str:slug>/', article, name='article'),
    path('articles/<str:slug>/update/', update_article, name='update_article'),
    path('articles/<str:slug>/delete/', delete_article, name='delete_article'),
]