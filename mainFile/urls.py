"""RunForGenertion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # Fighters
    path('fighters', views.fighters, name='fighters'),
    path('edit_fighter', views.edit_fighter, name='edit_fighter'),
    path('remove_fighter', views.remove_fighter, name='remove_fighter'),
    path('show_fighter', views.show_fighter, name='show_fighter'),
    path('create_fighter', views.create_fighter, name='create_fighter'),
    # Artists
    path('artists', views.artists, name='artists'),
    path('edit_artist', views.edit_artist, name='edit_artist'),
    path('remove_artist', views.remove_artist, name='remove_artist'),
    path('show_artist', views.show_artist, name='show_artist'),
    path('create_artist', views.create_artist, name='create_artist'),
    # youngster
    path('youngsters', views.youngsters, name='youngsters'),
    path('edit_youngster', views.edit_youngster, name='edit_youngster'),
    path('remove_youngster', views.remove_youngster, name='remove_youngster'),
    path('show_youngster', views.show_youngster, name='show_youngster'),
    path('create_youngster', views.create_youngster, name='create_youngster'),

]
