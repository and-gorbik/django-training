from django.urls import path
# from .views import article, articles, create_article
# from .views import update_article, delete_article

# urlpatterns = [
#     path('', articles, name='index'),
#     path('articles/', articles, name='articles'),
#     path('articles/new/', create_article, name='new_article'),
#     path('articles/<str:slug>/', article, name='article'),
#     path('articles/<str:slug>/update/', update_article, name='update_article'),
#     path('articles/<str:slug>/delete/', delete_article, name='delete_article'),
# ]

from .views import ArticleDetail, ArticleList, ArticleCreate
from .views import ArticleUpdate, ArticleDelete

urlpatterns = [
    path('', ArticleList.as_view(), name='index'),
    path('articles/', ArticleList.as_view(), name='articles'),
    path('articles/new/', ArticleCreate.as_view(), name='new_article'),
    path('articles/<str:slug>/', ArticleDetail.as_view(), name='article'),
    path('articles/<str:slug>/update/', ArticleUpdate.as_view(), name='update_article'),
    path('articles/<str:slug>/delete/', ArticleDelete.as_view(), name='delete_article'),
]