from django.shortcuts import render, get_object_or_404
from .models import Board

# Create a view that shows Hello World! when receive a Http request


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
