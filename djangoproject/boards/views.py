from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create a view that shows Hello World! when receive a Http request


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
