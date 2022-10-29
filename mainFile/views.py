from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def fighters(request):
    return render(request, 'fighters.html')

def artists(request):
    return render(request, 'artists.html')

def youngsters(request):
    return render(request, 'youngsters.html')

# Fighter
def create_fighter(request):
    return render(request, 'add_fighter.html')

def edit_fighter(request):
    return render(request, 'edit_fighter.html')

def remove_fighter(request):
    return render(request, 'remove_fighter.html')

def show_fighter(request):
    return render(request, 'show_fighter.html')

# Artist
def edit_artist(request):
    return render(request, 'edit_artist.html')

def remove_artist(request):
    return render(request, 'remove_artist.html')

def show_artist(request):
    return render(request, 'show_artist.html')

def create_artist(request):
    return render(request, 'add_artist.html')

# youngster
def edit_youngster(request):
    return render(request, 'edit_youngster.html')

def remove_youngster(request):
    return render(request, 'remove_youngster.html')

def show_youngster(request):
    return render(request, 'show_youngster.html')

def create_youngster(request):
    return render(request, 'add_youngster.html')
