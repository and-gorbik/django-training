from django.urls import path
from .views import articles, create_article, article

urlpatterns = [
    path('', articles, name='index'),
    path('articles/', articles, name='articles'),
    path('articles/new/', create_article, name='new_article'),
    path('articles/<int:id>/', article, name='article'),
]