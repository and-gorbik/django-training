from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='index'),
    path('profiles/', views.profiles, name='profiles'),
    path('profiles/<int:pk>/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),

    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]