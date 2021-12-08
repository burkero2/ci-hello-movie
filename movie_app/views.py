from django.shortcuts import render, redirect
from .models import Item
from .forms import MovieForm

# Create your views here.
def get_movie_list(request):
    items = Item.objects.all()
    context = {
        'items' : items
    }
    return render(request, 'movie_app/movie_app_home.html', context)

def add_movie(request):
    if request.method=='POST':
        title = request.POST.get('movie_title')
        director = request.POST.get('movie_director')
        genre = request.POST.get('movie_genre')
        summary = request.POST.get('movie_summary')
        score = request.POST.get('movie_score')
        watched='watched' in request.POST

        Item.objects.create(title=title, director=director, genre=genre, summary=summary, score=score, watched=watched)
        return redirect('get_movie_list')

    form = ItemForm()
    context = {
        'form':form
    }
    return render(request, 'movie_app/movie_app_add.html', context)