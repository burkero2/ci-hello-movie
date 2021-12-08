from django.shortcuts import render
from .models import Item

# Create your views here.
def get_movie_list(request):
    items = Item.objects.all()
    context = {
        'items' : items
    }
    return render(request, 'movie_app/movie_app_home.html', context)